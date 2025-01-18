import hashlib
import json
import pathlib
import tempfile
import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.filesystem.context import FileSystemContext
from xplore_path.nodes.filesystem.filesystem_node import FileSystemNode
from xplore_path.collections_.sequence_collection import SequenceCollection


class EvaluatorTest(unittest.TestCase):
    def _eval(self, expr):
        dir_ = pathlib.Path(__file__).parent.parent.parent / 'playground'
        with tempfile.TemporaryDirectory() as workspace:
            fs_path = FileSystemNode.create_root_path(dir_, FileSystemContext(workspace=pathlib.Path(workspace)))
            outputs = Evaluator().evaluate(fs_path, expr)
            actual = [expr]
            if isinstance(outputs, SequenceCollection):
                for v in outputs:
                    actual.append(f'{v}')
            else:
                actual.append(f'{outputs}')
            actual = sorted(actual)
            expected_path = dir_ / '.expected' / hashlib.sha256(expr.encode()).hexdigest()
            expected_path.parent.mkdir(parents=True, exist_ok=True)
            # expected_path.write_text(json.dumps(actual))
            expected = json.loads(expected_path.read_text())
            self.assertEqual(expected, actual)
        
    def test_must_match_known_results(self):
        # Inspect root
        self._eval("/*")          # List all files
        self._eval("$count(/*)")  # Count number of files

        # Inspect mouse assays
        self._eval("/mouse_assays.zip/*")                                           # List individual mouse assays
        self._eval("/mouse_assays.zip/Mouse_Assay_001.csv//*")                      # List first mouse assay's data
        self._eval("/mouse_assays.zip/r'.*001.csv'//*")                             # List first mouse assay's data, using regex
        self._eval("/mouse_assays.zip/g'*001.csv'//*")                              # List first mouse assay's data, using glob
        self._eval("label /mouse_assays.zip/Mouse_Assay_001.csv/0/*")               # List first mouse assay's headers (labels in first row)
        self._eval("/mouse_assays.zip//*/GO_Term")                                  # For each assay, list all values under the GO terms column
        self._eval("/mouse_assays.zip//*/GO_Term[. = g'GO:*']")                     # For each assay, list all values under the GO terms column starting with "GO:" (these are the actual GO terms)
        self._eval("/mouse_assays.zip//0/GO_Term")                                  # For each assay, list first value under the GO terms column (these are the actual GO terms)
        self._eval("$distinct(/mouse_assays.zip//0/GO_Term)")                       # Across all assays, list distinct GO terms
        self._eval("$frequency_count(/mouse_assays.zip//0/GO_Term)//*")             # Across all assays, count how often each GO term appears

        # Well data
        self._eval("position /mouse_assays.zip/Mouse_Assay_001.csv/*[.//*=Well]")   # Get row where Well data starts
        self._eval("label /mouse_assays.zip/Mouse_Assay_001.csv/*[.//*=Well]")      # Get row where Well data starts (using label instead of position)
        self._eval("/mouse_assays.zip/Mouse_Assay_001.csv/*[position . > position /mouse_assays.zip/Mouse_Assay_001.csv/*[.//*=Well]]//*") # Truncate rows to those after Well

        # Inspect mouse GO terms
        self._eval("/goslim_mouse.json//*")                                                         # List all
        self._eval("/goslim_mouse.json//*[./meta//val = g'*neuro*']//*")                            # List only related to neuro
        self._eval("/goslim_mouse.json//*[./meta//val = g'*neuro*']//id")                           # List only related to neuro, ids only
        self._eval("/goslim_mouse.json//*[./meta//val = g'*neuro*']//lbl")                          # List only related to neuro, labels only
        self._eval("/goslim_mouse.json//*[./meta//val = g'*neuro*']//(id, lbl)")                    # List only related to neuro, ids and labels
        self._eval("/goslim_mouse.json//*[./meta//val = g'*neuro*']//r'id|lbl'")                    # List only related to neuro, ids and labels using regex
        self._eval("$regex_extract(/goslim_mouse.json//*[./meta//val = g'*neuro*']//id, '\\d{7}')")   # List only related to neuro, cleaned ids only

        # Get GO terms in assays related to neuro
        self._eval("$distinct(/mouse_assays.zip/*/0/GO_Term)")                 # List GO terms in assays
        self._eval("/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']")  # List GO terms related to neuro
        self._eval("($distinct(/mouse_assays.zip/*/0/GO_Term) inner join /goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*'] on [$regex_extract(.//l, '\\d{7}') = $regex_extract(.//r//id, '\\d{7}')])") # List GO terms in assays related to neuro


if __name__ == '__main__':
    unittest.main()
