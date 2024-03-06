import nltk
import re

f = open("input.txt", "r")
input_program = ""
for line in f:
    if line.startswith('//'):
        continue
    input_program += line
f.close()

input_program_tokens = nltk.word_tokenize(input_program)

token_to_class = {
    'int': 'DT',
    'bool': 'DT',
    'if_stmnt': 'if_stmnt',
    'else_stmnt': 'else_stmnt',
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
    '"': '"',
    '(': '(',
    ')': ')',
    "'": "'",
    '[': '[',
    ']': ']',
    ',': ',',
    ':': ':',
    '\\': '\\',
    '\n': '\n',
    '\t': '\t',
    '\r': '\r',
    '\b': '\b',
    '\\\\': '\\\\',
    "\'": "\'",
    '\"': '\"',
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
    '/=': '/='
}


print(input_program_tokens)

RE_Identifier = r"[a-zA-Z_][a-zA-Z0-9_]*"
RE_Integer_Literal = r"^-?\d+$"



# #To categorize the tokens

for token in input_program_tokens:
    if token in token_to_class:
        print(token + " is a " + token_to_class[token] + " token")
    elif re.match(RE_Identifier, token) and (token not in token_to_class):
        print(token + " is an identifier")
    elif re.match(RE_Integer_Literal, token):
        print(token + " is an integer literal")
    else:
        print(token + " is an invalid token")
