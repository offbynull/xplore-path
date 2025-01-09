import itertools
import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath

_TEST_OBJ = {
    'Colors': {"Apple": "Red", "Cherry": "Red", "Blueberry": "Blue", "Grape": "Purple", "Orange": "Orange",
               "Watermelon": "Green", "Strawberry": "Red", "Lemon": "Yellow", "Kiwi": "Brown", "Mango": "Orange",
               "Pineapple": "Yellow", "Coconut": "Brown", "Raspberry": "Red", "Pomegranate": "Red", "Fig": "Purple",
               "Papaya": "Orange", "Blackberry": "Black"},
    'Regions': {"Banana": ["Southeast Asia", "Malaysia", "Indonesia"], "Cherry": ["Turkey", "Europe"],
                "Grape": ["Near East", "Mediterranean"], "Orange": ["China", "Southeast Asia"],
                "Watermelon": ["Africa", "Sudan"], "Strawberry": ["France", "North America"],
                "Lemon": ["India", "China"], "Kiwi": ["China"], "Peach": ["China"], "Plum": ["China", "Europe"],
                "Mango": ["India", "Southeast Asia"], "Pineapple": ["South America", "Brazil"],
                "Coconut": ["Southeast Asia", "India"], "Raspberry": ["Europe", "Asia"],
                "Pomegranate": ["Iran", "Afghanistan"], "Fig": ["Western Asia", "Mediterranean"],
                "Papaya": ["Southern Mexico", "Central America"], "Blackberry": ["North America", "Europe"]},
    'Capitals': {"Kazakhstan": "Astana", "Malaysia": "Kuala Lumpur", "Indonesia": "Jakarta", "Turkey": "Ankara",
                 "China": "Beijing", "Sudan": "Khartoum", "France": "Paris", "India": "New Delhi", "Brazil": "Brasília",
                 "Iran": "Tehran", "Afghanistan": "Kabul", }
}

class EvaluatorTest(unittest.TestCase):
    def _pop_first_and_assert_path(self, p_list, p_expected_label, p_expected_value):
        p = p_list.pop(0)
        self.assertEqual(p_expected_label, p.full_label())
        self.assertEqual(p_expected_value, p.value())
        
    def test_must_inner_join_path_vs_path(self):
        root = PythonObjectPath.create_root_path(_TEST_OBJ)
        r = evaluate(root, '/Colors/* inner join /Regions/* on [label ./l/*[0] = label ./r/*[0]]')
        r_actual = list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [None], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Cherry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 0], 'Turkey')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 1], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Grape'], 'Purple')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape', 0], 'Near East')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape', 1], 'Mediterranean')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Orange'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange', 1], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Watermelon'], 'Green')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 0], 'Africa')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 1], 'Sudan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Strawberry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry', 0], 'France')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry', 1], 'North America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Lemon'], 'Yellow')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon', 1], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Kiwi'], 'Brown')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Kiwi'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Kiwi', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Mango'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango', 1], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Pineapple'], 'Yellow')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple', 0], 'South America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple', 1], 'Brazil')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Coconut'], 'Brown')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut', 0], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut', 1], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Raspberry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry', 0], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry', 1], 'Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Pomegranate'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate', 0], 'Iran')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate', 1], 'Afghanistan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Fig'], 'Purple')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig', 0], 'Western Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig', 1], 'Mediterranean')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Papaya'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya', 0], 'Southern Mexico')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya', 1], 'Central America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Blackberry'], 'Black')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry', 0], 'North America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry', 1], 'Europe')

    def test_must_inner_join_single_vs_path(self):
        root = PythonObjectPath.create_root_path(_TEST_OBJ)
        r = evaluate(root, '(Cherry, Watermelon, Blueberry) inner join /Regions/* on [./l = label ./r/*[0]]')
        r_actual = list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [None], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], 'Cherry')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 0], 'Turkey')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 1], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], 'Watermelon')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 0], 'Africa')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 1], 'Sudan')

    def test_must_inner_join_path_vs_single(self):
        root = PythonObjectPath.create_root_path(_TEST_OBJ)
        r = evaluate(root, '/Colors/* inner join (Cherry, Watermelon, Blueberry) on [label ./l/*[0] = ./r]')
        r_actual = list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [None], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Cherry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], 'Cherry')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Blueberry'], 'Blue')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], 'Blueberry')

    def test_must_inner_join_single_vs_single(self):
        root = PythonObjectPath.create_root_path(_TEST_OBJ)
        r = evaluate(root, '(Cherry, Blueberry, Orange) inner join (Cherry, Watermelon, Blueberry) on [./l = ./r]')
        r_actual = list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [None], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], 'Cherry')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], 'Cherry')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], 'Blueberry')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], 'Blueberry')


if __name__ == '__main__':
    unittest.main()
