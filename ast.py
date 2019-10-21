
class AST(object):
    pass


class BinaryOperator(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.token = token.value


class Identifier(AST):
    def __init__(self, token):
        self.token = token
