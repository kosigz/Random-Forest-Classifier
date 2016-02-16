from math import log

from model.tree import LabelNode
from model.tree import DecisionNode

# Construction ----------------------------------------------------------------
# returns reference to the root of a new decision tree
def create_decision_tree(training_data, attributes, target):
    training_data   = training_data[:]
    target_labels   = [record[target] for record in training_data]
    default         = most_frequent(target_labels)

    if not training_data or len(attributes) <= 1 or \
    target_labels.count(default) == len(target_labels):
        # either out of attributes to split on or the set has the same
        # label, in which case splitting is not possible
        return LabelNode(default)

    else:
        # select the best attribute to split on
        best = choose_best_attribute(data, \
        [a for a in attributes if a != target], target)

        # make a new node
        tree = DecisionNode(best)

        # split for discrete variables
        for val in get_values(data, best):
            subtree = create_decision_tree(
                get_examples(training_data, best, val),
                [attr for attr in attributes if attr != best],
                target)
            tree.set_subtree(val, subtree)

        return tree

# Construction, Helper Functions ----------------------------------------------
def most_frequent(values):
    counts = {}
    for v in values:
        if not v in counts:
            counts[v] = 1
        else:
            counts[v] += 1
    k = list(counts.keys())
    v = list(counts.values())
    return k[v.index(max(v))]

def choose_best_attribute(data, attributes, target):
    info_gain = {}
    for attr in attributes:
        if attr != target:
            info_gain[attr] = entropy(data, attr, target)
    # get the lowest entropy
    k = list(info_gain.keys())
    v = list(info_gain.values())
    return k[v.index(min(v))]

def entropy(data, attr, target):
    vals = [d[attr] for d in data]
    entropy = 0
    for val in set(vals):
        proportion = float(vals.count(val)) / len(vals)
        # print proportion + log(proportion, 2)
        entropy -= proportion * log(proportion, 2)
    return entropy

def get_values(data, attribute):
    values = set([])
    for d in data:
        values.add(d[attribute])
    return values

def get_examples(data, attribute, val):
    result = []
    for d in data:
        if d[attribute] == val:
            result.append(d)
    return result

# TEST ------------------------------------------------------------------------
data = [{'weather': 'cloudy', 'temp': 'hi', 'result': 'yes'},
{'weather': 'cloudy', 'temp': 'lo', 'result': 'no'},
{'weather': 'sunny', 'temp': 'hi', 'result': 'yes'},
{'weather': 'sunny', 'temp': 'lo', 'result': 'no'},
{'weather': 'sunny', 'temp': 'hi', 'result': 'no'},
{'weather': 'cloudy', 'temp': 'hi', 'result': 'yes'}]
attributes = ['weather', 'temp', 'result']
target = 'result'
decision_tree = create_decision_tree(data, attributes, target)
