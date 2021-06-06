class NonExponentialError(Exception):
    def __init__(self):
        super().__init__("The given expression is Non Exponential")

class NonPower1Error(Exception):
    def __init__(self):
        super().__init__("The passed expression node is not of instance Power1")

class NodeError(Exception):
    def __init__(self):
        super().__init__("The node is matched incorrectly")