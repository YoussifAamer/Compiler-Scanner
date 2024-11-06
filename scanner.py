import re

token_patterns = [
    ('KEYWORD', r'\b(if|for|int|while|print|input)\b'),                
    ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),            
    ('NUMERIC_CONSTANT', r'\b\d+(\.\d+)?(e[-+]?\d+)?\b'),  
    ('CHARACTER_CONSTANT', r"\'[a-zA-Z0-9]\'"),      
    ('STRING', r'\".*?\"'),                         
    ('OPERATOR', r'[+\-*=]'),                     
    ('SPECIAL_CHAR', r'[;,(){}"]'),                 
    ('COMMENT', r'//[^\n]*'),                        
    ('NEWLINE', r'\n'),                            
    ('WHITESPACE', r'\s+'),                        
]

combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)

def tokenize(code):
    tokens = []
    for match in re.finditer(combined_pattern, code):
        token_type = match.lastgroup  
        token_value = match.group(token_type)  
        if token_type != 'WHITESPACE':  
            tokens.append((token_type, token_value))
    return tokens

user_input = input("input a sentence to analyze: ")

tokens = tokenize(user_input)

print("Tokens")
for token_type, token_value in tokens:
    print(f'{token_type}: {token_value}')