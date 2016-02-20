from construction.constructor import *
from construction.data_utility import *
import model.tree
import classifier

data, attrs = data_from_file('training/WeatherTraining.csv', ',')
decision_tree = create_decision_tree(data, attrs, 'play')
sample_record = {'play': 'yes', 'windy': 'false', 'outlook': 'overcast', 'temperature': '30', 'humidity': 'high'}
print classify(sample_record, decision_tree).label
