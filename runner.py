from model.tree import LabelNode
from model.tree import DecisionNode
from constructor import create_decision_tree

"""
Given a record (dict) and a decision tree root node, returns the corresponding
LabelNode.
"""
def classify(record, decision_tree):
    while not isinstance(decision_tree, LabelNode):
        decision_tree = decision_tree.subtrees[record[decision_tree.attribute]]
    return decision_tree
