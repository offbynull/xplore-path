import hashlib
import pickle
from collections import OrderedDict
from pathlib import Path
from typing import Any


class Cache:
    def __init__(self, path: Path, mem_cache_capacity: int = 256):
        self._disk_cache_path = path
        self._disk_cache_path.mkdir(parents=True, exist_ok=True)
        self._mem_cache = OrderedDict()  # tried use WeakValueDictionary but if val isn't a strong ref it always vacates
        self._mem_cache_capacity = mem_cache_capacity

    def _to_hash(self, key: Any) -> str:
        key_bytes = pickle.dumps(key)
        return hashlib.sha256(key_bytes).hexdigest()

    def to_path(self, key: Any) -> Path:
        return self._disk_cache_path / self._to_hash(key)

    def load(self, key: Any) -> tuple[bool, Any]:
        key_hash = self._to_hash(key)
        # try loading it from in-memory cache
        if key_hash in self._mem_cache:
            # print('from mem')
            value = self._mem_cache.get(key_hash)
            self._mem_cache.move_to_end(key_hash)
            return True, value
        # if fail - try loading it from disk cache
        cache_path = self._disk_cache_path / key_hash
        if cache_path.exists():
            try:
                # print('from disk')
                value = pickle.loads(cache_path.read_bytes())
                self._mem_cache[key_hash] = value  # its loaded, save it in-memory
                if len(self._mem_cache) > self._mem_cache_capacity:
                    self._mem_cache.popitem(last=False)
                return True, value
            except Exception as e:
                cache_path.unlink(missing_ok=True)
        return False, None

    def cache(self, key: Any, value: Any) -> None:
        key_hash = self._to_hash(key)
        if key_hash in self._mem_cache:
            self._mem_cache.move_to_end(key_hash)
        self._mem_cache[key_hash] = value
        if len(self._mem_cache) > self._mem_cache_capacity:
            self._mem_cache.popitem(last=False)
        cache_path = self._disk_cache_path / key_hash
        if cache_path.exists():
            cache_path.unlink()
        try:
            cache_path.write_bytes(pickle.dumps(value))
        except Exception as e:
            ...  # do nothing
