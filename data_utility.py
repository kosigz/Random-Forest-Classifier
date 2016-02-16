from constructor import create_decision_tree
from runner import classify

def data_from_file(filename, delimiter):
    file = open(filename)
    # read in all attributes = {}
    attributes = {}
    i = 0
    for attr in file.readline().strip().split(delimiter):
        attributes[i] = attr
        i += 1

    # read in the remaining lines
    data = []
    record = {}
    i = 0
    for line in file:
        l = [l.strip() for l in line.lower().strip().split(delimiter)]
        for j in range(len(attributes.keys())):
            record[attributes[j]] = l[j]
        data.append(record)
        record = {}

    return (data, attributes.values())

data, attrs = data_from_file('training/WeatherTraining.csv', ',')
print data
