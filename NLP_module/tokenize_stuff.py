def tokenize(program):
    """
    Helper method to receive a program as string and return it as a list of
    tokens
    """
    # We add spaces in order to create tokens using whitespace as criteria
    program_with_spaces = program.replace('(', ' ( ').replace(')', ' ) ')
    return program_with_spaces.split()

def identify_element(element):
    """
    Helper method to cast each element of the program to his atomic
    representation
    """
    try:
        return int(element)
    except ValueError:
        try:
            return float(element)
        except ValueError:
            return str(element)

def build_abstract_syntax_tree(tokens):
    """
    Recursive function to build an abstract syntax tree (AST), an AST is a list
    of nested lists representing the code structure for the program.
    """
    if len(tokens) == 0:
        raise SyntaxError("Unexpected End of File while reading")

    token = tokens.pop(0)

    if token == '(':
        sublist = []
        first_item = next(iter(tokens or []), None)
        while first_item != ')':
            sublist.append(build_abstract_syntax_tree(tokens))
        tokens.pop(0)
        return sublist
    elif token == ')':
        raise SyntaxError("Unexpected ), please check your program :)")
    else:
        return identify_element(token)

def parse(program):
    """
    Method that takes a string that represents a program and return his
    equivalent AST
    """
    tokens = tokenize(program)
    return build_abstract_syntax_tree(tokens)

def execute_program():
    """
    Main method of the program, it prompts to the user to get the program input
    """
    program = input("Please write here your program: ")
    return parse(program)


if __name__ == "__main__":
    print(execute_program())