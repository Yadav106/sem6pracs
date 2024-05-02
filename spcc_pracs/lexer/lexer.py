class Token:
    def __init__(self, line, lexeme, token_type):
        self.token_type = token_type
        self.lexeme = lexeme
        self.line = line

    def __str__(self):
        return f"{self.line} | {self.lexeme} : {self.token_type}"

class Lexer:
    def __init__(self, source):
        self.source = source
        self.length = len(source)
        self.index = 0
        self.tokens = []
        self.line = 1

    def is_at_end(self):
        return self.index >= self.length

    def peek(self):
        return self.source[self.index]

    def check(self, char):
        return self.peek() == char

    def consume(self):
        current = self.peek()
        self.index += 1
        return current

    def preprocessor(self):
        preprocessor_string = ""
        while not self.check('<'):
            preprocessor_string += self.consume()

        preprocessor_token = Token(self.line, preprocessor_string, "PREPROCESSOR")
        self.tokens.append(preprocessor_token)

        current = self.consume()
        open_angle_bracket_token = Token(self.line, current, "LEFT_ANGLE_BRACKET")
        self.tokens.append(open_angle_bracket_token)

        header_string = ""
        while not self.check('>'):
            header_string += self.consume()

        header_token = Token(self.line, header_string, "HEADER")
        self.tokens.append(header_token)

        current = self.consume()
        close_angle_bracket_token = Token(self.line, current, "RIGHT_ANGLE_BRACKET")
        self.tokens.append(close_angle_bracket_token)

    def string(self):
        lexeme = ""
        while not self.check('"'):
            lexeme += self.consume()

        string_token = Token(self.line, lexeme, "STRING")
        self.tokens.append(string_token)
        self.consume()

    def scan(self):
        while (not self.is_at_end()):
            char = self.consume()
            if char == '\n': self.line += 1
            elif char == '"': self.string()
            elif char == '#': self.preprocessor()


def read_file(name):
    with open(name, 'r') as f:
        file = f.read()
        return file

file = read_file("code.c")
lexer = Lexer(file)
lexer.scan()

for i in lexer.tokens:
    print(i)
