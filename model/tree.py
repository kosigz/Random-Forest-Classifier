# Model -----------------------------------------------------------------------
class LabelNode(object):
    def __init__(self, label, entropy):
        self.label = label
        self.entropy = entropy

class DecisionNode(object):
    def __init__(self, attribute, entropy):
        self.attribute = attribute
        self.subtrees = {}
        self.entropy = entropy

    def set_subtree(self, val, subtree):
        self.discrete = True    # TODO make the tree handle continuous valued nodes
        self.subtrees[val] = subtree
