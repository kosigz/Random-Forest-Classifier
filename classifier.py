from model.tree import LabelNode
from model.tree import DecisionNode
from constructor import create_decision_tree

print "classify"

# Given a record (dict) and a decision tree root node, returns the corresponding
# LabelNode.
def classify(record, decision_tree):
    print "Called classify"
    while not isinstance(decision_tree, LabelNode):
        decision_tree = decision_tree.subtrees[record[decision_tree.attribute]]
        print decision_tree.entropy
    return decision_tree
