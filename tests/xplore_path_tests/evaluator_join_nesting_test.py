import itertools
import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


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


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def _pop_first_and_assert_path(self, p_list, p_expected_label, p_expected_value):
        p = p_list.pop(0)
        self.assertEqual(tuple(p_expected_label), p.full_label())
        self.assertEqual(p_expected_value, p.value())

    def test_must_allow_nesting_of_joins(self):
        root = PythonObjectNode.create_root_path(_TEST_OBJ)
        # r = evaluate(root, '/Capitals/*').unpack
        # r = evaluate(root, '(/Colors/* inner join /Regions/* on [label ./l/*[0] = label ./r/*[0]])/r/*').unpack
        # r = evaluate(root, '(/Colors/* inner join /Regions/* on [label ./l/*[0] = label ./r/*[0]])/r').unpack
        r = evaluate(root, '/Capitals/* inner join (/Colors/* inner join /Regions/* on [label ./l/*[0] = label ./r/*[0]])/r/*/* on [label ./l/*[0] = ./r//*]').unpack
        r_actual = list(itertools.chain(*([r_] + r_.descendants() for r_ in r)))
        self._pop_first_and_assert_path(r_actual, [], None)
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'Turkey'], 'Ankara')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 0], 'Turkey')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'China'], 'Beijing')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 0], 'China')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'China'], 'Beijing')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 1], 'China')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'China'], 'Beijing')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 0], 'China')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'Sudan'], 'Khartoum')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 1], 'Sudan')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'France'], 'Paris')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 0], 'France')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'India'], 'New Delhi')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 0], 'India')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'India'], 'New Delhi')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 0], 'India')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'India'], 'New Delhi')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 1], 'India')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'Brazil'], 'Brasília')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 1], 'Brazil')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'Iran'], 'Tehran')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 0], 'Iran')
        self._pop_first_and_assert_path(r_actual, ['joined'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'l', 'Afghanistan'], 'Kabul')
        self._pop_first_and_assert_path(r_actual, ['joined', 'r'], None)
        self._pop_first_and_assert_path(r_actual, ['joined', 'r', 1], 'Afghanistan')
        # for r_ in list(itertools.chain(*([r_] + r_.all_descendants() for r_ in r))):
        #     print(f'self._pop_first_and_assert_path(r_actual, {r_.full_label()}, {f"'{r_.value()}'" if type(r_.value()) == str else r_.value()})')


if __name__ == '__main__':
    unittest.main()
