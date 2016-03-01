# Model -----------------------------------------------------------------------
class LabelNode(object):
    def __init__(self, label, entropy):
        self.label = label
        self.entropy = entropy

class DecisionNode(object):
    def __init__(self, attribute, entropy, split_expression=None):
        self.attribute = attribute
        self.subtrees = {}
        self.entropy = entropy
        self.split_expression = split_expression

    def set_subtree(self, val, subtree):
        self.subtrees[val] = subtree
