# Model -----------------------------------------------------------------------
class LabelNode(object):
    def __init__(self, label):
        self.label = label

class DecisionNode(object):
    def __init__(self, attribute):
        self.attribute = attribute
        self.subtrees = {}

    def set_subtree(self, val, subtree):
        self.discrete = True    # TODO make the tree handle continuous valued nodes
        self.subtrees[val] = subtree
