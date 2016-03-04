from construction.constructor import *
from construction.data_utility import *
from utilities.visualizer import *

import model.tree
from classifier.classifier import *

def weather_classifier():
    data, attrs = data_from_file('training/WeatherTraining.csv', ',')
    decision_tree = create_decision_tree(data, attrs, 'play')
    sample_record = {'play': 'yes', 'windy': 'false', 'outlook': 'overcast', 'temperature': '30', 'humidity': 'high'}
    print_tree(decision_tree)
    print classify(sample_record, decision_tree)

def housing_classifier():
    data, attrs = data_from_file('training/HousingTraining.csv', None)
    # data, attrs = data_from_file('training/HousingTraining.csv', None)
    # decision_tree = create_decision_tree(data, attrs, 'play')

weather_classifier()
# data, attrs = data_from_file('training/WeatherTraining.csv', ',')
#print entropy([{'play': 'no', 'windy': 'true', 'outlook': 'rainy', 'temperature': '0', 'humidity': 'normal'}, {'play': 'yes', 'windy': 'false', 'outlook': 'rainy', 'temperature': '1', 'humidity': 'normal'}, {'play': 'yes', 'windy': 'false', 'outlook': 'sunny', 'temperature': '2', 'humidity': 'normal'}, {'play': 'yes', 'windy': 'true', 'outlook': 'overcast', 'temperature': '5', 'humidity': 'normal'}, {'play': 'yes', 'windy': 'true', 'outlook': 'overcast', 'temperature': '10', 'humidity': 'high'}, {'play': 'yes', 'windy': 'false', 'outlook': 'rainy', 'temperature': '15', 'humidity': 'high'}, {'play': 'yes', 'windy': 'false', 'outlook': 'rainy', 'temperature': '19', 'humidity': 'normal'}, {'play': 'no', 'windy': 'true', 'outlook': 'rainy', 'temperature': '19', 'humidity': 'high'}, {'play': 'yes', 'windy': 'true', 'outlook': 'sunny', 'temperature': '19', 'humidity': 'normal'}, {'play': 'no', 'windy': 'false', 'outlook': 'sunny', 'temperature': '22', 'humidity': 'high'}, {'play': 'yes', 'windy': 'false', 'outlook': 'overcast', 'temperature': '25', 'humidity': 'normal'}, {'play': 'no', 'windy': 'true', 'outlook': 'sunny', 'temperature': '28', 'humidity': 'high'}, {'play': 'yes', 'windy': 'false', 'outlook': 'overcast', 'temperature': '30', 'humidity': 'high'}, {'play': 'no', 'windy': 'false', 'outlook': 'sunny', 'temperature': '31', 'humidity': 'high'}], attrs, 'play')
