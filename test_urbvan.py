import unittest

"""
A bracket is considered to be any one of the following characters: 
    (, ), {, }, [, or ].
Two brackets are considered to be a matched pair if the an opening bracket 
(i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) 
of the exact same type. There are three types of matched pairs 
of brackets: [], {}, and ().
A matching pair of brackets is not balanced if the set of brackets it encloses 
are not matched. For example, {[(])} is not balanced because the contents in 
between { and } are not balanced
Your job is to fix the brackets so that all opening and closing parentheses 
(brackets) have matching counterparts. You will do this by appending 
parenthesis to the beginning or end of the string.

"""


def parenthesis_balancer(s):
    pass

    matchet_pairs = True
    balanced_par = []
    parentesis_balance = ""

    stack = []
    open_par = "({["
    close_par = ")}]"

    for character in s:
        # parentesis_balance += character
        if character in open_par:
            stack.append(character)
        elif character in close_par:
            if len(stack) == 0:
                matchet_pairs = False
            else:
                stack_top = stack.pop()
                balancing_bracket = open_par[close_par.index(character)]

                if stack_top != balancing_bracket:
                    matchet_pairs = False
                else:
                    matchet_pairs = True

        if matchet_pairs:
            parentesis_balance += character
            balanced_par.append(parentesis_balance)

    for char in parentesis_balance:
        if char in open_par:
            stack.append(char)
        elif char in close_par:
            if len(stack) == 0:
                matchet_pairs = False
            else:
                stack_top = stack.pop()
                balancing_bracket = open_par[close_par.index(char)]

                if stack_top != balancing_bracket:
                    matchet_pairs = False
                else:
                    matchet_pairs = True

        if matchet_pairs:
            parentesis_balance += close_par[open_par.index(char)]

    # return not len(stack)
    return parentesis_balance


class ParenthesisBalancerTest(unittest.TestCase):

    # def test_case_0(self):
    #     input_data = ""
    #     output_data = ""
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_1(self):
    #     input_data = "()"
    #     output_data = "()"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_2(self):
    #     input_data = "()[]{}"
    #     output_data = "()[]{}"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))

    def test_case_3(self):
        input_data = "([{"
        output_data = "([{}])"
        self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_4(self):
    #     input_data = "([]("
    #     output_data = "([]())"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_5(self):
    #     input_data = ")))"
    #     output_data = "((()))"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_6(self):
    #     input_data = "]("
    #     output_data = "[]()"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_7(self):
    #     input_data = "{[]}]"
    #     output_data = "[{[]}]"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_8(self):
    #     input_data = "{[]}]"
    #     output_data = "[{[]}]"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_9(self):
    #     input_data = "((()"
    #     output_data = "((()))"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))
    #
    # def test_case_10(self):
    #     input_data = "{{(({[[](({})"
    #     output_data = "{{(({[[](({}))]}))}}"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))


unittest.main(exit=True)
