from math import log

from model.tree import LabelNode
from model.tree import DecisionNode

# Construction ----------------------------------------------------------------
# Builds a decision tree from the file given with the specified target attribute.
def construct_decision_tree_from_file(filename, target):
    data, attrs = data_from_file(filename)
    return create_decision_tree(data, attrs, target)

# returns reference to the root of a new decision tree
def create_decision_tree(training_data, attributes, target):
    training_data   = training_data[:]
    target_labels   = [record[target] for record in training_data]
    default         = most_frequent(target_labels)

    if not training_data \
    or target_labels.count(default) == len(target_labels) \
    or len(attributes) == 0:
        # either out of attributes to split on or the set has the same
        # label, in which case splitting is not possible
        return LabelNode(default, 0)

    elif len(attributes) == 1:
        return LabelNode(default, entropy(data, attr, target))

    else:
        # select the best attribute to split on
        best, entropy = choose_best_attribute(training_data, \
        [a for a in attributes if a != target], target)

        # make a new node
        tree = DecisionNode(best, entropy)

        # split for discrete variables
        for val in get_values(training_data, best):
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
    entropies = {}
    for attr in attributes:
        if attr != target:
            entropies[attr] = entropy(data, attr, target)
    # get the lowest entropy
    k = list(entropies.keys())
    v = list(entropies.values())
    return k[v.index(min(v))], v[v.index(min(v))]

def entropy(data, attr, target):
    labels = [d[target] for d in data]
    entropy = 0
    for label in get_values(data, target):
        proportion = float(labels.count(label)) / len(labels)
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
