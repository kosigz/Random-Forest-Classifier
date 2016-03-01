from math import log
import operator

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
        best, entropy, split_expression = choose_best_attribute(training_data, \
        [a for a in attributes if a != target], target)

        # make a new node
        tree = DecisionNode(best, entropy)

        # split for discrete variables
        if not split_expression: # <--  split expression is none for discretes
            for val in get_values(training_data, best):
                subtree = create_decision_tree(
                    get_examples(training_data, best, val),
                    [attr for attr in attributes if attr != best],
                    target)
                tree.set_subtree(val, subtree)
        else:
        # split for continous value
            for result in [True, False]:
                subtree = create_decision_tree(
                [record for record in training_data if split_expression(record[best]) == result],
                [attr for attr in attributes if attr != best],
                target)

                # set the subtree and split expression!
                tree.set_subtree(result, subtree)
                tree.split_expression = split_expression

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
    split_expressions = {}
    for attr in attributes:
        if attr != target and is_discrete(data, attr):
            entropies[attr] = entropy(data, attr, target)
            split_expressions[attr] = None
        else:
            entropies[attr], split_expression = entropy_for_continuous(data, attr, target)
            split_expressions[attr] = split_expression
    # get the lowest entropy
    k = list(entropies.keys())
    v = list(entropies.values())
    s = list(split_expressions.values())
    return k[v.index(min(v))], v[v.index(min(v))], s[v.index(min(v))]

# should determine if the attribute is discrete or continous, and return the
# entropy of the best split and the value to split on if applicable
def entropy(data, attribute, target):
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

# Continous Split Helpers -----------------------------------------------------
# To be called with continous attribute. Find the split.
def entropy_for_continuous(data, attribute, target):
    entropies = {}
    data = sorted(data, key=lambda item: float(item[attribute]))
    # find the split that minimizes entropy
    for i in range(len(data) + 1):
        first_entropy = entropy(data[:i], attribute, target)
        second_entropy = entropy(data[i:], attribute, target)
        entropies[i] = first_entropy * len(data[:i]) / len(data) \
        + second_entropy * len(data[i:]) / len(data)
    # get the best
    k = list(entropies.keys())
    v = list(entropies.values())
    optimal_split_index, entr = k[v.index(min(v))], v[v.index(min(v))]
    def optimal_split_expression(x):
        return float(x) > float(data[min(optimal_split_index, len(data) - 1)][attribute])
    return entr, optimal_split_expression

# let's say that all numerial data is continuous for now
def is_discrete(training_data, attribute):
    return not unicode(training_data[0][attribute], 'utf-8').isnumeric()
