from model.tree import LabelNode
from model.tree import DecisionNode

# Given a record (dict) and a decision tree root node, returns the corresponding
# LabelNode.
def classify(record, decision_tree):
    while not isinstance(decision_tree, LabelNode):
        if decision_tree.split_expression == None:
            decision_tree = decision_tree.subtrees[record[decision_tree.attribute]]
        else:
            decision_tree = decision_tree.subtrees[decision_tree.split_expression(record[decision_tree.attribute])]
    return decision_tree.label
