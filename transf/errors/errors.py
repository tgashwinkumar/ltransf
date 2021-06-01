class InvalidRoot(Exception):
    def __init__(self):
        super().__init__("RootNode is not an operator")
        