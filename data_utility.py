from constructor import create_decision_tree
from model.tree import LabelNode
from model.tree import DecisionNode

file = open('training/WeatherTraining.csv')

# read in all attributes = {}
attributes = {}
i = 0
for attr in file.readline().strip().split(','):
    attributes[i] = attr
    i += 1

# read in the remaining lines
data = []
record = {}
i = 0
for line in file:
    l = line.strip().lower().split(',')
    for j in range(len(attributes.keys())):
        record[attributes[j]] = l[j]
    data.append(record)
    record = {}

# use data, attrs, target to call create_decision_tree
attrs = attributes.values()
target = 'play'

decision_tree = create_decision_tree(data, attrs, target)

# Let's test out this tree on an existing record.
test_record = {'windy': 'false', 'outlook': 'sunny', 'temperature': 'mild', 'humidity': 'high'}

while not isinstance(decision_tree, LabelNode):
    decision_tree = decision_tree.subtrees[test_record[decision_tree.attribute]]

print "Label for TEST_RECORD is " + "'" + decision_tree.label + "'"
