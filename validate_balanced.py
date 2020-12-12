
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
    list_indexes = []
    parentesis_balance = ""

    is_par = False
    is_open = False
    is_close = False

    stack = []
    open_par = "({["
    close_par = "]})"

    list_char_status = []

    index = 0

    print("Input string: ", s)

    for character in s:
        # parentesis_balance += character
        if character in open_par:
            stack.append(character)
            # balanced_par.append(character)
            print("index char open: ", index)
            is_open = True
            is_close = False
            # print("is_open: ", is_open)
            # list_char_status.append((is_open, is_close))
        elif character in close_par:
            print("index char closed: ", index)
            is_close = True
            is_open = False
            # print("is_closed: ", is_close)
            if len(stack) == 0:
                matchet_pairs = False
                is_par = False
            else:
                stack_top = stack.pop()
                balancing_bracket = open_par[close_par.index(character)]
                # print("index no ha evaluado stack_top != balancing_bracket: ", index)
                if stack_top != balancing_bracket:
                    matchet_pairs = False
                    # print("index stack_top != balancing_bracket: ", index)
                    list_indexes.append(index)
                    is_par = False
                else:
                    # print("index stack_top == balancing_bracket: ", index)
                    matchet_pairs = True
                    is_par = True

        print("character in list original: ", character)

        list_char_status.append((is_open, is_close))

        # print("is_par: {}, (is_open: {}, is_closed: {})".format(is_par, is_open, is_close))
        print("List_Char_States: ", list_char_status)

        balanced_par.append(character)

        balancear_paarentesis(balanced_par, list_indexes, list_char_status)

        index += 1

        # if matchet_pairs:
        #     parentesis_balance += character
        #     balanced_par.append(parentesis_balance)

    return not len(stack)
    # return parentesis_balance


def balancear_paarentesis(list_input, list_index, list_char_states):
    i = 0

    char_key_close = "}"
    char_bracket_close = "]"
    char_parent_close = ")"

    char_key_open = "{"
    char_bracket_open = "["
    char_parent_open = "("

    states_char_to_change = ()

    # print("item by list_index: ", list_index)

    parenthesis_balanced = ""

    for item in reversed(list_input):
        print("item_list reversed: ", item)
        parenthesis_balanced += item
        for state_char in reversed(list_char_states):
            # ESTE CODIGO PUEDE SERVIR, GUARDARLO
            # for i in range(0, len(list_input) - 1):
            #     print("item_original_list[{}]: {}".format(i, list_input[i]))
            # i += 1
            print("char_state: ", state_char)
            # if state_char[0] and not state_char[1]:
            #     parenthesis_balanced += item
            # else:
            #     if item == char_key_open:
            #         parenthesis_balanced += char_key_close
            #     elif item == char_bracket_open:
            #         parenthesis_balanced += char_bracket_close
            #     elif item == char_parent_open:
            #         parenthesis_balanced += char_parent_close

            for index in list_index:
                states_char_to_change = list_char_states[index]
                print("char_state of item to change: ", states_char_to_change)
                if states_char_to_change[0] and states_char_to_change[1] is False:
                    if item == char_key_open:
                        parenthesis_balanced += char_key_open
                    elif item == char_bracket_open:
                        parenthesis_balanced += char_bracket_open
                    elif item == char_parent_open:
                        parenthesis_balanced += char_parent_open
                    elif item == char_key_close:
                        parenthesis_balanced += char_key_close
                    elif item == char_bracket_close:
                        parenthesis_balanced += char_bracket_close
                    elif item == char_parent_close:
                        parenthesis_balanced += char_parent_close

        print("string_parenthesis_balanced: ", parenthesis_balanced)
    # print("list_char_states normal: ", list_char_states)


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

    # def test_case_3(self):
    #     input_data = "([{"
    #     output_data = "([{}])"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))

    def test_case_4(self):
        input_data = "([]("
        output_data = "([]())"
        self.assertEquals(output_data, parenthesis_balancer(input_data))

        '''
        Input string:  ([](

        index char open:  0
        is_open:  True
        character in list:  (
        is_par: False, (is_open: True, is_closed: False)
        List_Char_States:  [(True, False)]
        
        item_list reversed:  (
        item by list_index:  []
        list_char_states normal:  [(True, False)]
        
        
        index char open:  1
        is_open:  True
        character in list:  [
        is_par: False, (is_open: True, is_closed: False)
        List_Char_States:  [(True, False), (True, False)]
        
        item_list reversed:  [
        item_list reversed:  (
        item by list_index:  []
        list_char_states normal:  [(True, False), (True, False)]
        
        
        index char closed:  2
        is_closed:  True
        index no ha evaluado stack_top != balancing_bracket:  2
        index stack_top != balancing_bracket:  2
        character in list:  ]
        is_par: False, (is_open: False, is_closed: True)
        List_Char_States:  [(True, False), (True, False), (False, True)]
        
        item_list reversed:  ]
        item_list reversed:  [
        item_list reversed:  (
        item by list_index:  [2]
        list_char_states normal:  [(True, False), (True, False), (False, True)]
        
        
        index char open:  3
        is_open:  True
        character in list:  (
        is_par: False, (is_open: True, is_closed: False)
        List_Char_States:  [(True, False), (True, False), (False, True), (True, False)]
        
        item_list reversed:  (
        item_list reversed:  ]
        item_list reversed:  [
        item_list reversed:  (
        item by list_index:  [2]
        list_char_states normal:  [(True, False), (True, False), (False, True), (True, False)]
        '''

    # def test_case_5(self):
    #     input_data = ")))"
    #     output_data = "((()))"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))

    # def test_case_6(self):
    #     input_data = "]("
    #     output_data = "[]()"
    #     self.assertEquals(output_data, parenthesis_balancer(input_data))

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
