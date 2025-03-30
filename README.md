# Xplore Path

Xplore Path is a tool for quick-and-dirty data exploration, built for messy, untidy data scattered across disparate files and formats.

 * **Simple syntax**: Query data with an intuitive, XPath-like syntax.
 * **Broad format support**: Search through CSVs, XLSXs, JSONs, YAMLs, DOCXs, PDFs, XMLs, HTMLs, ...
 * **Fuzzy search support**: Search using globs, regexs, fuzzy strings, numeric tolerances, ...
 * **Unified environment**: Search through disparate files and formats within a single context.
 * **Extendable**: Add formats and functions for your custom use cases (e.g. 3D scene graphs, flow cytometry, ...).

Xplore Path aims to be the first tool you reach for when exploring reasonably-sized data "thrown over the fence" by a colleague or partner. It does not aim to be a database or a storage engine.

To get started, jump to [REPL Usage Guide](#repl-usage-guide).

<!-- TOC -->
* [Xplore Path](#xplore-path)
  * [REPL Usage Guide](#repl-usage-guide)
  * [Library Usage Guide](#library-usage-guide)
  * [Xplore Path vs XPath](#xplore-path-vs-xpath)
    * [Fuzzy Search](#fuzzy-search)
    * [Variables](#variables)
    * [Joining](#joining)
  * [Extension Guide](#extension-guide)
    * [Custom Formats](#custom-formats)
    * [Custom Functions](#custom-functions)
  * [TODOs](#todos)
<!-- TOC -->

## REPL Usage Guide

To use the Xplore Path REPL, install it and launch `xplore-path` executable using one of the methods below.

<details><summary>Install and launch</summary>

1. Ensure Python is installed.

   ```bash
   python --version
   ```

2. Install xplore-path dependency.

   ```bash
   pip install git+https://github.com/offbynull/xplore-path.git@main#egg=xplore_path[data_repl]
   ```
  
3. Download xplore-path repository as zip and pull out the playground directory.

   ```bash
   wget https://github.com/offbynull/xplore-path/archive/refs/heads/main.zip -O xplore-path-main.zip
   unzip xplore-path-main.zip "xplore-path-main/playground/*" -d extracted
   ```

4. Launch Xplore Path REPL.

   ```bash
   xplore-path --path extracted/xplore-path-main/playground
   ```

</details>
  
<details><summary>Install and launch in development mode</summary>

The following commands install Xplore Path in development mode, as if you're developing Xplore Path. Installing in development mode is best if you're planning on extending Xplore Path's functionality.

1. Ensure Python and Poetry are installed.

   ```bash
   python --version
   poetry --version
   ```

2. Clone the repository.

   ```bash
   git clone https://github.com/offbynull/xplore-path.git
   cd xplore-path
   ```

3. Install Xplore Path

   ```bash
   poetry install --all-extras
   ```

4. Launch Xplore Path REPL

   ```bash
   # Launch Xplore Path REPL
   poetry run xplore-path --path playground
   ```

</details>

Regardless of the installation method, the last step launches the REPL with the active directory set to `playground`. 

![Screenshot of REPL interface](repl_example.png)

The `playground` directory contains a mix of fabricated biological and general-purpose data, spread across many file formats. Xplore Path lets you query this data as if it were a single unified hierarchy.  Try running a few of the example queries shown below. If you've used XPath before, the queries below should feel familiar as Xplore Path's query language is heavily inspired by XPath.

<details><summary>Walking hierarchy</summary>

* `/*` - List top-level files.
* `//*` - List all data.
* `/mouse_assays.zip/*` - List mouse assays.
* `/mouse_assays.zip/Mouse_Assay_001.csv//*` - List first mouse assay's data.
* `/mouse_assays.zip/r'.*001.csv'//*` - List first mouse assay's data, but using regex to identify the first assay.
* `/mouse_assays.zip/g'*001.csv'//*` - List first mouse assay's data, but using glob to identify the first assay.
* `/mouse_assays.zip/*/0/Plate_Type` - List plate type for each mouse assay.
* `/mouse_assays.zip/Mouse_Assay_001.csv/0/Plate_Type` - List plate type for first mouse assay.
* `/goslim_mouse.json//*` - List mouse gene ontology entries.
* `/goslim_mouse.json//(id, lbl)` - List mouse gene ontology IDs and labels.
* `/goslim_mouse.json//r'id|lbl'` - List mouse gene ontology IDs and labels, but using regex.

</details>

<details><summary>Walking hierarchy, with filters</summary>

* `/mouse_assays.zip/*[.//g'*Gene*' = g'*Cd40*']` - List mouse assays targeting gene Cd40.
* `/mouse_assays.zip//*/GO_Term[. = g'GO:*']` - For each mouse assay, list the gene ontology terms used.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//*` - List mouse gene ontology entries related to neuro.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//id` - List mouse gene ontology entries related to neuro, IDs only.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//lbl` - List mouse gene ontology entries related to neuro, labels only.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//(id, lbl)` - List mouse gene ontology entries related to neuro, IDs and labels.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//r'id|lbl'` - List mouse gene ontology entries related to neuro, IDs and labels using regex.

</details>

<details><summary>Walking hierarchy, with filters and functions</summary>

* `$count(/*)` - Count top-level files.
* `$distinct(/mouse_assays.zip//*/GO_Term[. = g'GO:*'])` - Across all mouse assays, list distinct gene ontology terms used.
* `$frequency_count(/mouse_assays.zip//*/GO_Term[. = g'GO:*'])//*` - Across all mouse assays,  count how often each gene ontology term appears.
* `$regex_extract(/goslim_mouse.json//*[./meta//val = g'*neuro*']//id, '\d{7}')` - List mouse gene ontology related to neuro, cleaned IDs only.

</details>

<details><summary>Joining hierarchy</summary>

* `($distinct(/mouse_assays.zip/*/0/GO_Term) inner join /goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*'] on [$regex_extract(.//l, '\d{7}') = $regex_extract(.//r//id, '\d{7}')])` - Across all mouse assays, list gene ontology terms in the mouse assay that are related to neuro

The query above is made up of the two sub-queries `$distinct(/mouse_assays.zip/*/0/GO_Term)` and `/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']`. The former lists the distinct gene ontology terms used across all mouse assays and the latter pulls out gene ontology terms related to neuro. The results are then inner joined.

:warning: **Xplore Path joins are currently slow.** At the moment, the joining logic hasn't been optimized. Expect joins to be incredibly slow: O(n^2).

</details>

As highlighted in a few of the above examples, Xplore Path's syntax enhances basic XPath syntax in several helpful ways. For a list of major differences, jump to [Xplore Path vs XPath](#xplore-path-vs-xpath).

## Library Usage Guide

To use XplorePath as a library, install it directly from GitHub using whatever your build management tool of choice is (e.g. pip, poetry, ...). For example, to install via pip ...

```bash
# Install xplore-path (standalone)
pip install git+https://github.com/offbynull/xplore-path.git@main
# Install xplore-path (with REPL and file type support)
pip install git+https://github.com/offbynull/xplore-path.git@main#egg=xplore_path[data_repl]
```

The `Evaluator` class allows you to use an Xplore Path expression to walk a hierarchy. A hierarchy is represented using the `Node` class. In the example below, `PythonObjectNode` is a sub-class of `Node` that represents nested Python collections (`dict`, `list`, `tuple`, ...) as a hierarchy.

```python
from xplore_path.node import Node
from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


# Evaluate expression
evaluator = Evaluator()
result = evaluator.evaluate(
    root=PythonObjectNode(
        parent=None,
        value={'a': {'b': ['c', 'd', 'e', 'f']}, 'y': {3, 4}, 'z': (5, 6)}
    ),
    expr='//*'
)

# Print results
for v in result.unpack:
    if isinstance(v, Node):
        print(f'{v.full_label()}: {v.value()}')
    else:
        print(f'{v}')
```


## Xplore Path vs XPath

While Xplore Path's query language is heavily inspired by XPath, it deviates in several important ways. If you're coming here as someone experienced with XPath, here are the key differences between XPath and Xplore Path to be mindful of:

 * <details><summary>0-based indexing.</summary>

   XPath indexing is 1-based, whereas Xplore Path indexing is 0-based. Most programming languages and querying languages use 0-based indexing, and so Xplore Path sticks to that convention.

   Examples:

   ```xpath
   /apple[1]    # XPath: Get first "apple" under root.
   /apple[0]    # Xplore Path: Get first "apple" under root.
   ```
   
   </details>
 * <details><summary>Query must start with a path separator or relative path indicator.</summary>

   XPath queries have the option of starting with just a path element (e.g. `a/b/c`, treated as querying relative to the current context node). whereas Xplore Path requires that queries start with either a path separator (`/` or `//`) or a relative path indicator (e.g. `.` or `..`).

   ```xpath
   a/b/c     # NOT ALLOWED - Valid in XPath only
   /a/b/c    # Allowed - Valid in both XPath and Xplore Path
   //a/b/c   # Allowed - Valid in both XPath and Xplore Path
   ./a/b/c   # Allowed - Valid in both XPath and Xplore Path
   ../a/b/c  # Allowed - Valid in both XPath and Xplore Path
   ```
   
   </details>
 * <details><summary>Subset of directives / operations / functions supported.</summary>

   Xplore Path supports a subset of the directives / operations / functions present in XPath. Many were left out because Xplore Path gives the user the ability to plug in their own [custom functions](#custom-functions).

   Those supported include ...

   * `not`
   * `position`
   * `label` (synonym for XPath's `name`)
   * `intersect`
   * `except`
   * `union`
   * `|`

   </details>
 * <details><summary>No concept of namespaces/attributes.</summary>

   XPath is specific to XML, and as such supports the concept of XML namespaces and attributes. Since Xplore Path's intent is to be more abstract (in that it can represent any type of hierarchical data, not just XML data), it doesn't have a concept of XML namespaces or attributes.

   </details>
 * <details><summary>Node can have both children and a value.</summary>

   In XPath / XML, it isn't possible for a node to have both a value and children. With Xplore Path, it is possible. If the underlying hierarchy supports nodes that have both a value and children, Xplore Path has the capability to directly represent those nodes.

   </details>

In addition to the above points, the following subsections detail helpful additions provided by Xplore Path.

The full Xplore Path grammar is available at [XplorePathGrammar.g4](src/xplore_path/XplorePathGrammar.g4).

### Fuzzy Search

Xplore Path adds support for various types of fuzzy matching through the use of custom literals:

* `i~value` / `i'value'` for case-insensitive matching (e.g. `i'HeLLo'`) 
* `g~value` / `g'value'` for glob matching (e.g. `g'hello*'`) 
* `r~value` / `r'value'` for regex matching (e.g. `r'hello.*'`) 
* `f~value` / `f'value'` for fuzzy matching (e.g. `f'hello'`) 
* `a~value` / `a'value'` for camelcase/snakecase/titlecase acronym matching (e.g. `a~IBM`)
* `~number:number` for number ranges, optionally using brackets to define open/closed-ness (e.g. `~[4:9)`)
* `~number@tolerance` for number within some tolerance (e.g. `~3.14@0.0001`)

Examples:   

```xpath
/mouse_assays.zip/g~*001.csv//*
/mouse_assays.zip/g'*001.csv'//*
/mouse_assays.zip//*/GO_Term[. = g'GO:*']
/mouse_assays.zip//*/GO_Term[. = g~GO:*]
```

### Variables

Xplore Path adds support for variables. Variables are denoted by a word prefixed with `$` (e.g. `$distinct`), and may be ...

* included in a query.
* invoked as a function (assuming the variable contains something that's invocable).

Examples:

```xpath
/a/$my_variable/c         # Inject into path element
/a/b/c[. = $my_variable]  # Inject into condition
$my_variable()            # Invoke
```

### Joining

Xplore Path adds experimental support for joining queries. Queries are joinable using `inner join`, `left join`, and `right join`.

Example:

```xpath
($distinct(/mouse_assays.zip/*/0/GO_Term) inner join /goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*'] on [$regex_extract(.//l, '\d{7}') = $regex_extract(.//r//id, '\d{7}')])` - Across all mouse assays, list gene ontology terms in the mouse assay that are related to neuro
```

The example above is made up of the two sub-queries `$distinct(/mouse_assays.zip/*/0/GO_Term)` and+ `/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']`. The former lists the distinct gene ontology terms used across all mouse assays and the latter pulls out gene ontology terms related to neuro. The results are then inner joined.

:warning: **Xplore Path joins are currently slow.** At the moment, the joining logic hasn't been optimized. Expect joins to be incredibly slow: O(n^2).

## Extension Guide

The subsections below describe how to extend Xplore Path's functionality via custom functions and hierarchy formats. Ensure you've gone through both the [REPL Usage Guide](#repl-usage-guide) and [Library Usage Guide](#library-usage-guide) before continuing. 

### Custom Formats

The easiest way to support your custom hierarchy is to simply convert it to a set of nested collections and expose it via `PythonObjectNode`.

```python
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


node = PythonObjectNode(
    parent=None,
    value={'a': {'b': ['c', 'd', 'e', 'f']}, 'y': {3, 4}, 'z': (5, 6)}
)
```

Otherwise, a hierarchy can be exposed by implementing it as sub-classes of `Node`. Each `Node` sub-class must include the method `children()`, which returns the children of that `Node` instance. In the example below, the `CustomNode` class exposes a set of nested collections as a hierarchy accessible by Xplore Path (similar to `PythonObjectNode` above).

```python
from xplore_path.null import Null
from xplore_path.node import Node, ParentBlock


class CustomNode(Node):
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            value: dict | set | list | tuple
    ):
        if value is None:
            value = Null()
        super().__init__(parent, value if type(value) in {bool, int, float, str, Null} else None)
        self._data = value

    def children(self) -> list[Node]:
        this = self._data
        ret = []
        if isinstance(this, dict):
            for i, k in enumerate(this.keys()):
                ret += [CustomNode(ParentBlock(self, i, k), this[k])]
        elif isinstance(this, set):
            for i, v in enumerate(this):
                return [CustomNode(ParentBlock(self, i, i), v)]
        elif isinstance(this, (list, tuple)):
            for i, v in enumerate(this):
                ret += [CustomNode(ParentBlock(self, i, i), v)]
        return ret
```

If working with the REPL, chances are you want to add support for custom file formats to show up in the hierarchy. To support a new file format, a custom `FileLoader` for that format must be included in the context of the  `FileSystemNode` that gets generated within the REPL (see `xplore_path.repl` package). A `FileLoader` identifies if a file is of the expected file format, loads that file, and transforms the loaded data into a `Node` hierarchy. In the example below, `CustomFileLoader` loads up JSON data as a hierarchy (similar to the built-in `JsonFileLoader` provided by XplorePath).

```python
import json
from typing import Any
from pathlib import Path
from xplore_path.nodes.filesystem.filesystem_node import FileSystemNode
from xplore_path.nodes.filesystem.context import FileSystemContext
from xplore_path.nodes.filesystem.file_loader import FileLoader, NODE_CREATOR


class CustomFileLoader(FileLoader):
    def is_loadable(self, p: Path) -> bool:
        return p.suffix == '.json'

    def load(self, p: Path) -> Any:
        return json.loads(p.read_text())
    
    def node_creator(self, p: Path) -> NODE_CREATOR:
        return CustomNode


node = FileSystemNode(
    None,
    fs_path=Path('~').expanduser(),
    ctx=FileSystemContext(
        file_loader=FileSystemContext.DEFAULT_FILE_LOADER
            .include(CustomFileLoader())
    )
)
```

The Xplore Path codebase has many other built-in examples of `FileLoader` that you can reference. 

### Custom Functions

An Xplore Path function is a class that inherits from `xplore_path.invocable.Invocable`. The class must include the method `invoke()`, which ...

* takes a single parameter of a type `list[Collection]` that holds the arguments passed into the function. 
* returns a `Collection` containing the result of the function.

The example `Invocable` below counts the numbers of items within the first argument.

```python
from xplore_path.invocable import Invocable
from xplore_path.collection import Collection
from xplore_path.collections_.single_value_collection import SingleValueCollection


class CountInvocable(Invocable):
    def invoke(self, args: list[Collection]) -> Collection:
        return SingleValueCollection(sum(1 for _ in args[0]))
```

To make the function available for use by expressions, it must be passed into the constructor of the `Evaluator` running those expressions as a variable.

```python
from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode
from xplore_path.collections_.single_value_collection import SingleValueCollection


evaluator = Evaluator(
    variables={'count': SingleValueCollection(CountInvocable())}
)
result = evaluator.evaluate(
    root=PythonObjectNode(
        parent=None,
        value={'a': {'b': ['c', 'd', 'e', 'f']}, 'y': {3, 4}, 'z': (5, 6)}
    ),
    expr='$count(//*)'
)
```

## TODOs

* TODO: extend the language to somehow handle cycles
  * examples of cycles:
    * python objects/collections may have cycles  
    * goslim_mouse.json is actually a graph - it has nodes and edges - possibly withcycles?
  * mark edges leading to cycle as a "weak" link that's traversed only once?
    * // operator will stop when it's seen a node more than once?
    * // operator takes an optional parameter for how many times to step over the same weak edge before stopping? 
* TODO: best effort output to ~~CSV~~/JSON/YAML/XML/HTML?
* TODO: path should have metadata?
  * e.g. shell looks for a key that means that it hides the child in the output?
  * e.g. shell looks for a key that means it can preview children in the output? (e.g. if there is no value, show first 3 children inline where value should be? or display that it has children / is terminal?)
* TODO: filesystem path - for each parsed file, inject invocations that can re-work the file
* TODO: change syntax so keywords must be followed by ::, ENFORCE IN LEXER (so people can still use the keywords as-is)
* TODO: add callback that notifies of what's happening when evaluation is running 
* TODO: test complex math (order of operations)
* TODO: cache all_children() in PythonObjectPath + stream all_children() in other paths + take in max argument to cap number of children
* TODO: make use of variables in REPL - store results in var names and use those var names in queries
* TODO: Cache results for each call to expr(), reset it every time xplore() called
    this doesn't work because ./b and ./b will hit the same cache, but the result may be different depending on context
    how to work around this?
      rather than just caching on expr().getText(), cache on the full path the parser took? - that wont work /a/b/c[./d=5] - ./d=5 part wil
    factor in self.context somehow to disambiguate? pickle it and mix it with expr().getText() to get cache key?
    NEW PLAN:
      cache based on the operation being performed WITH full paths as operands
          - if operation is happening on a root path, cache it - it'll always be hte same
          - if operation is happening on a context path, convert it to a root path and cache it
       e.g. /a/b/c/*[./e = /x/f]
         for each child of c, the cache key predicate expands ./e to full pat
            /a/b/c/d1 and what gets cached is key '/a/b/c/d1/e = /x/e'
            /a/b/c/d2 and what gets cached is key '/a/b/c/d2/e = /x/e'
         once that's complete, /a/b/c/*[./e = /x/f] itself gets cached (it's already root path, no conversion needed)
       CAVEAT: some paths are dynamically generated (e.g. results from function callsm such as frequency_count), so you should also also check to see if the root object is the same when checking cache 
* TODO: Python object path, put in invocable members