from model.tree import LabelNode
from model.tree import DecisionNode

def print_tree(decision_tree):
    if isinstance(decision_tree, LabelNode):
        print "============ LABEL ============"
        print "Label:\t\t" + str(decision_tree.label)
        print "Entropy:\t" + str(decision_tree.entropy)
        print "==============================="
    else:
        print "========== DECISION ==========="
        print "Split On:\t" + str(decision_tree.attribute)
        print "Entropy:\t" + str(decision_tree.entropy)
        print "==============================="
        for subtree_key in decision_tree.subtrees:
            print subtree_key
            print_tree(decision_tree.subtrees[subtree_key])
