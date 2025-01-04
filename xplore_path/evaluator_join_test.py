import itertools
import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath

_TEST_OBJ = {
    'Colors': {"Apple": "Red", "Cherry": "Red", "Blueberry": "Blue", "Grape": "Purple", "Orange": "Orange", "Watermelon": "Green", "Strawberry": "Red", "Lemon": "Yellow", "Kiwi": "Brown", "Mango": "Orange", "Pineapple": "Yellow", "Coconut": "Brown", "Raspberry": "Red", "Pomegranate": "Red", "Fig": "Purple", "Papaya": "Orange", "Blackberry": "Black"},
    'Regions': {"Banana": ["Southeast Asia", "Malaysia", "Indonesia"], "Cherry": ["Turkey", "Europe"], "Grape": ["Near East", "Mediterranean"], "Orange": ["China", "Southeast Asia"], "Watermelon": ["Africa", "Sudan"], "Strawberry": ["France", "North America"], "Lemon": ["India", "China"], "Kiwi": ["China"], "Peach": ["China"], "Plum": ["China", "Europe"], "Mango": ["India", "Southeast Asia"], "Pineapple": ["South America", "Brazil"], "Coconut": ["Southeast Asia", "India"], "Raspberry": ["Europe", "Asia"], "Pomegranate": ["Iran", "Afghanistan"], "Fig": ["Western Asia", "Mediterranean"], "Papaya": ["Southern Mexico", "Central America"], "Blackberry": ["North America", "Europe"]},
    'Capitals': {"Kazakhstan": "Astana", "Malaysia": "Kuala Lumpur", "Indonesia": "Jakarta", "Turkey": "Ankara", "China": "Beijing", "Sudan": "Khartoum", "France": "Paris", "India": "New Delhi", "Brazil": "Brasília", "Iran": "Tehran", "Afghanistan": "Kabul",}
}

class EvaluatorTest(unittest.TestCase):
    def _pop_first_and_assert_path(self, p_list, p_expected_label, p_expected_value):
        p = p_list.pop(0)
        self.assertEqual(p_expected_label, p.full_label())
        self.assertEqual(p_expected_value, p.value())
        
    def test_must_inner_join(self):
        root = PythonObjectPath.create_root_path(_TEST_OBJ)
        r = evaluate(root, '/Colors/* inner join /Regions/* on [label ./l/*[0] = label ./r/*[0]]')
        r_actual = list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [None], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Cherry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry'], ['Turkey', 'Europe'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 0], 'Turkey')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 1], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Grape'], 'Purple')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape'], ['Near East', 'Mediterranean'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape', 0], 'Near East')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape', 1], 'Mediterranean')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Orange'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange'], ['China', 'Southeast Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange', 1], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Watermelon'], 'Green')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon'], ['Africa', 'Sudan'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 0], 'Africa')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 1], 'Sudan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Strawberry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry'], ['France', 'North America'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry', 0], 'France')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry', 1], 'North America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Lemon'], 'Yellow')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon'], ['India', 'China'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon', 1], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Kiwi'], 'Brown')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Kiwi'], ['China'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Kiwi', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Mango'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango'], ['India', 'Southeast Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango', 1], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Pineapple'], 'Yellow')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple'], ['South America', 'Brazil'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple', 0], 'South America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple', 1], 'Brazil')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Coconut'], 'Brown')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut'], ['Southeast Asia', 'India'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut', 0], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut', 1], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Raspberry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry'], ['Europe', 'Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry', 0], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry', 1], 'Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Pomegranate'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate'], ['Iran', 'Afghanistan'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate', 0], 'Iran')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate', 1], 'Afghanistan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Fig'], 'Purple')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig'], ['Western Asia', 'Mediterranean'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig', 0], 'Western Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig', 1], 'Mediterranean')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Papaya'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya'], ['Southern Mexico', 'Central America'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya', 0], 'Southern Mexico')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya', 1], 'Central America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Blackberry'], 'Black')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry'], ['North America', 'Europe'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry', 0], 'North America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry', 1], 'Europe')

    def test_must_left_join(self):
        root = PythonObjectPath.create_root_path(_TEST_OBJ)
        r = evaluate(root, '/Colors/* left join /Regions/* on [label ./l/*[0] = label ./r/*[0]]')
        r_actual = list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [None], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Apple'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Cherry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry'], ['Turkey', 'Europe'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 0], 'Turkey')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 1], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Blueberry'], 'Blue')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Grape'], 'Purple')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape'], ['Near East', 'Mediterranean'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape', 0], 'Near East')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape', 1], 'Mediterranean')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Orange'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange'], ['China', 'Southeast Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange', 1], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Watermelon'], 'Green')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon'], ['Africa', 'Sudan'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 0], 'Africa')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 1], 'Sudan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Strawberry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry'], ['France', 'North America'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry', 0], 'France')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry', 1], 'North America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Lemon'], 'Yellow')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon'], ['India', 'China'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon', 1], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Kiwi'], 'Brown')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Kiwi'], ['China'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Kiwi', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Mango'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango'], ['India', 'Southeast Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango', 1], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Pineapple'], 'Yellow')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple'], ['South America', 'Brazil'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple', 0], 'South America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple', 1], 'Brazil')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Coconut'], 'Brown')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut'], ['Southeast Asia', 'India'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut', 0], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut', 1], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Raspberry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry'], ['Europe', 'Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry', 0], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry', 1], 'Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Pomegranate'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate'], ['Iran', 'Afghanistan'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate', 0], 'Iran')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate', 1], 'Afghanistan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Fig'], 'Purple')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig'], ['Western Asia', 'Mediterranean'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig', 0], 'Western Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig', 1], 'Mediterranean')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Papaya'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya'], ['Southern Mexico', 'Central America'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya', 0], 'Southern Mexico')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya', 1], 'Central America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Blackberry'], 'Black')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry'], ['North America', 'Europe'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry', 0], 'North America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry', 1], 'Europe')

    def test_must_right_join(self):
        root = PythonObjectPath.create_root_path(_TEST_OBJ)
        r = evaluate(root, '/Colors/* right join /Regions/* on [label ./l/*[0] = label ./r/*[0]]')
        r_actual = list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [None], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Banana'], ['Southeast Asia', 'Malaysia', 'Indonesia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Banana', 0], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Banana', 1], 'Malaysia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Banana', 2], 'Indonesia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Cherry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry'], ['Turkey', 'Europe'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 0], 'Turkey')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Cherry', 1], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Grape'], 'Purple')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape'], ['Near East', 'Mediterranean'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape', 0], 'Near East')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Grape', 1], 'Mediterranean')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Orange'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange'], ['China', 'Southeast Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Orange', 1], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Watermelon'], 'Green')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon'], ['Africa', 'Sudan'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 0], 'Africa')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Watermelon', 1], 'Sudan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Strawberry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry'], ['France', 'North America'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry', 0], 'France')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Strawberry', 1], 'North America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Lemon'], 'Yellow')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon'], ['India', 'China'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Lemon', 1], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Kiwi'], 'Brown')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Kiwi'], ['China'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Kiwi', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Peach'], ['China'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Peach', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Plum'], ['China', 'Europe'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Plum', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Plum', 1], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Mango'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango'], ['India', 'Southeast Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Mango', 1], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Pineapple'], 'Yellow')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple'], ['South America', 'Brazil'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple', 0], 'South America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pineapple', 1], 'Brazil')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Coconut'], 'Brown')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut'], ['Southeast Asia', 'India'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut', 0], 'Southeast Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Coconut', 1], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Raspberry'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry'], ['Europe', 'Asia'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry', 0], 'Europe')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Raspberry', 1], 'Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Pomegranate'], 'Red')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate'], ['Iran', 'Afghanistan'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate', 0], 'Iran')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Pomegranate', 1], 'Afghanistan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Fig'], 'Purple')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig'], ['Western Asia', 'Mediterranean'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig', 0], 'Western Asia')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Fig', 1], 'Mediterranean')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Papaya'], 'Orange')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya'], ['Southern Mexico', 'Central America'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya', 0], 'Southern Mexico')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Papaya', 1], 'Central America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Blackberry'], 'Black')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry'], ['North America', 'Europe'])
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry', 0], 'North America')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 'Blackberry', 1], 'Europe')

    def test_must_allow_nesting_of_joins(self):
        root = PythonObjectPath.create_root_path(_TEST_OBJ)
        # r = evaluate(root, '/Capitals/*')
        # r = evaluate(root, '(/Colors/* inner join /Regions/* on [label ./l/*[0] = label ./r/*[0]])/r/*')
        # r = evaluate(root, '(/Colors/* inner join /Regions/* on [label ./l/*[0] = label ./r/*[0]])/r')
        r = evaluate(root, '/Capitals/* inner join (/Colors/* inner join /Regions/* on [label ./l/*[0] = label ./r/*[0]])/r/*/* on [label ./l/*[0] = ./r//*]')
        r_actual = list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [None], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Turkey'], 'Ankara')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 0], 'Turkey')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'China'], 'Beijing')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'China'], 'Beijing')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 1], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'China'], 'Beijing')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 0], 'China')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Sudan'], 'Khartoum')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 1], 'Sudan')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'France'], 'Paris')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 0], 'France')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'India'], 'New Delhi')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'India'], 'New Delhi')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 0], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'India'], 'New Delhi')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 1], 'India')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Brazil'], 'Brasília')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 1], 'Brazil')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Iran'], 'Tehran')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 0], 'Iran')
        self._pop_first_and_assert_path(r_actual, [None, 'joined'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'l', 'Afghanistan'], 'Kabul')
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, [None, 'joined', 'r', 1], 'Afghanistan')
        # for r_ in list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r))):
        #     print(f'self._pop_first_and_assert_path(r_actual, {r_.full_label()}, {f"'{r_.value()}'" if type(r_.value()) == str else r_.value()})')


if __name__ == '__main__':
    unittest.main()
