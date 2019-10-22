import ast


class Parser(object):
    def __init__(self, token_list):
        self.counter = 0
        self.raw, self.tokens = zip(*token_list[0])
        self.tokens = list(self.tokens)
        self.raw = list(self.raw)
        self.current_token = self.tokens[self.counter]
        self.current_raw = self.raw[self.counter]


    def parse(self):
        return self.parse_expression()

    def error(self):
        raise Exception("Invalid syntax")

    def consume_token(self):
        self.counter += 1
        self.current_token = self.tokens[self.counter]
        self.current_raw = self.raw[self.counter]

    def parse_expression(self):
        node = self.parse_term()
        while self.current_raw is '+':
            self.consume_token()
            node = ast.BinaryOperator(self.parse_term(), '+', self.parse_term())
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_raw is '-':
            self.consume_token()
            node = ast.BinaryOperator(self.parse_factor(), '-', self.parse_factor())
        return node

    def parse_factor(self):
        node = self.parse_piece()
        while self.current_raw is '/':
            self.consume_token()
            node = ast.BinaryOperator(self.parse_piece(), '/', self.parse_piece())
        return node

    def parse_piece(self):
        node = self.parse_element()
        while self.current_raw is '*':
            self.consume_token()
            node = ast.BinaryOperator(self.parse_element(), '*', self.parse_element())
        return node

    def parse_element(self):
        if self.current_raw is '(':
            self.consume_token()
            if self.current_raw is ')':
                self.consume_token()
                node = self.parse_expression()
                return node
        if self.current_token is 'IDENTIFIER':
            node = ast.Identifier(self.current_raw)
            return node
        if self.current_token is 'NUMBER':
            node = ast.Num(self.current_raw)
            return node
        self.error()