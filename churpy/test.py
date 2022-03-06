import re

"""
-----MY THOUGHT PROCESS TO THE CHALLENGE----
I will approach using Abstract Syntax Tree (AST)
Individual rule of grammar are called productions
First I will create an empty node.Then I will extract the dictionary of the key: value pairs
Second I will extract the ternary expression from the input and extract a list of all the tokens 
tokens: 1.left parenthesis
        2. right parenthesis
        3. if statements
        4.Operands: - for subtraction and + for addition
Steps: 1.If my operator is if we add the expression as the left subtree
        2.If current token is + or - set root node to operator and new children added as right children.
        3.If current token is a number followed by == the evaluate the to true or false and set root.
        value of the current node to that number and return to the parent.
        4.If token is ) we go to the parent of the current node.
"""


class ParseTernary:
    # Todo: Check on error handiling and exceptions

    def __init__(self, expression):
        self.expression = expression
        self.variable_dict = self.clean_variable_dictionary
        self.cleaned_tenary_expression = self.clean_expression_data


    @property
    def clean_variable_dictionary(self) -> dict:
        final_dict = {}
        reg = r'(\{[^{}]+\})'
        matches = re.findall(reg, self.expression)
        new_match = str(matches[0]).replace("\n", "")
        new_match = re.sub(' +|{|}', '', new_match).split(",")
        for i in new_match:
            new_val = i.split(":")
            # Todo: working with floats to diversify inputs
            # final_dict[new_val[0]] = float(new_val[1])
            final_dict[new_val[0]] = int(new_val[1])
        return final_dict

    @property
    def clean_expression_data(self) -> str:
        """
        :param expression:
        :return list:
        takes in an expression and returns the cleaned str with variables replaced
        """
        variable_dictionary = self.variable_dict
        reg = r'(\`[^{}]+\`)'
        matches = re.findall(reg, self.expression)
        new_match_list = (str(matches[0]).replace("\n", "")).replace("`", "")
        variables = re.findall(r'[var_]\w+', new_match_list)
        for var in variables:
            new_match_list = new_match_list.replace(var, str(variable_dictionary.get(var)))

        return new_match_list

    def parse_ternary(self):
        """
        :type expression: str
        :rtype: str
        """

        stack = []
        for c in self.expression[::-1]:
            # Todo: Create a descend parse tree for the cleaned expression data and identify base case for recusrsion
            print("THe C iss ", c)
            pass


# Input for testing the class functionality
input = """
`
if (var_1 == 2, 0, if (var_2 == 4, 15, 0))
+ if (var_2 == 3, 5, 0)
- if (var_4 == 2, 0, 5)
+ if (var_3 == 3, 5, 0)`, {
    var_1: 1,
    var_2: 4,
    var_3: 3,
    var_4: 5
}
"""

c = ParseTernary(input)
c.parse_ternary()
