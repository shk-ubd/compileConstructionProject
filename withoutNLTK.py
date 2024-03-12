import re

# Define regular expressions for token recognition
RE_Identifier = r"[a-zA-Z_][a-zA-Z0-9_]*"
RE_Integer_Literal = r"^-?\d+$"
RE_String_Literal = r'\'[^\']*\'|\"[^\"]*\"'

# Define token classes
token_to_class = {
    'int': 'DT',
    'bool': 'DT',
    'if': 'if_stmnt',
    'else': 'else_stmnt',
    'for': 'for',
    'True': 'TRUE',
    'False': 'FALSE',
    'restore': 'res',
    'not': 'NOT',
    'otherwise': 'otherwise',
    'print': 'prt',
    'break': 'brk',
    'continue': 'cnt',
    'pass': 'pass',
    'dec': 'dec',
    'or': 'OR',
    'in': 'in',
    'None': 'none',
    'range': 're',
    'input': 'ip',
    'output': 'op',
    'and': 'AND',
    '$': '$',
    '#': '#',
    ';': ';',
    '(': '(',
    ')': ')',
    '[': '[',
    ']': ']',
    ',': ',',
    ':': ':',
    '\\': '\\',
    '\n': 'NEWLINE',
    '\t': 'TAB',
    '\r': 'CR',
    '\b': 'BS',
    '\\\\': 'BACKSLASH',
    '+': '+',
    '-': '-',
    '*': '*',
    '/': '/',
    '%': '%',
    '//': '//',
    '**': '**',
    '=': '=',
    '==': '==',
    '!=': '!=',
    '<': '<',
    '>': '>',
    '<=': '<=',
    '>=': '>=',
    '&&': '&&',
    '||': '||',
    '!': '!',
    '+=': '+=',
    '-=': '-=',
    '*=': '*=',
    '/=': '/=',
}

# Open and read input file
with open("input.txt", "r") as f:
    lines = f.readlines()

# Tokenize input program, ignoring commented lines
input_program_tokens = []
for line in lines:
    if not line.strip().startswith('//'):
        input_program_tokens += re.findall(RE_String_Literal + r'|[\w]+|[^\w\s]', line)

# Categorize tokens
for token in input_program_tokens:
    if token in token_to_class:
        print(token + " is a " + token_to_class[token] + " token")
    elif re.match(RE_Identifier, token):
        print(token + " is an identifier")
    elif re.match(RE_Integer_Literal, token):
        print(token + " is an integer literal")
    elif re.match(RE_String_Literal, token):
        print(token + " is a string literal")
    else:
        print(token + " is an invalid token")
