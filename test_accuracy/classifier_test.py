import unittest
import sys

from ..construction.constructor import *

class UnitTests(unittest.TestCase):
    def test(self):
        decision_tree = construct_decision_tree_from_file('training/WeatherTraining.csv', ',')
        sample_record = {'play': 'yes', 'windy': 'false', 'outlook': 'overcast', 'temperature': '30', 'humidity': 'high'}
        print classify(sample_record, decision_tree)
        self.assertEquals(classify(sample_record, decision_tree), 'yes')

if __name__ == '__main__':
    unittest.main()
