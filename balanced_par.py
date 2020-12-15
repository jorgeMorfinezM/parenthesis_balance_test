# -*- coding: utf-8 -*-

def balancer(string_eval):

    item_char_list = list(string_eval)
    stack_list = []
    num_par_open = item_char_list.count('(')
    num_par_close = item_char_list.count(')')

    list_of_indexes_open = []
    list_of_indexes_close = []

    if num_par_open != num_par_close:
        print("Los paréntesis no están bien balanceados")
    else:
        index_pair = 0
        # for valor in item_char_list:

        for index_pair in range(0, len(item_char_list) - 1):
            if item_char_list[index_pair] == '(':
                stack_list.append(item_char_list[index_pair])
                # index_open += 1
                # list_of_indexes_open.append(index_open)
                # index_pair += 1
            elif item_char_list[index_pair] == ')' and len(stack_list) > 0:
                stack_list.pop()
                # index_close += 1
                # list_of_indexes_close.append(index_close)

            index_pair += 1

    index_open = 0
    index_close = 0

    index_pair = 0

    stack_balanced = [None] * len(string_eval*2)

    for index_pair in range(len(item_char_list)):
        if item_char_list[index_pair] == '(':
            list_of_indexes_open.append(index_open)
            index_open += 1
        elif item_char_list[index_pair] == ')':
            list_of_indexes_close.append(index_close)
            index_close += 1

        index_pair += 1

    if num_par_open != num_par_close:
        if num_par_open != len(list_of_indexes_close):
            for i in list_of_indexes_open:
                stack_balanced.append('(')
                stack_balanced.remove(None)
        elif num_par_open > 0:
            for i in list_of_indexes_open:
                stack_balanced[i] = '('
                stack_balanced.remove(None)
        else:
            for item in item_char_list:
                stack_balanced.append(item)
                stack_balanced.remove(None)

        if num_par_close != len(list_of_indexes_open):
            for i in reversed(list_of_indexes_open):
                stack_balanced.append(')')
                stack_balanced.remove(None)
        elif num_par_close > 0:
            for i in list_of_indexes_close:
                stack_balanced[i] = ')'
                stack_balanced.remove(None)
        else:
            for item in item_char_list:
                stack_balanced.append(item)
                stack_balanced.remove(None)

    parenthesis_balanced_string = ""

    for item in stack_balanced:
        if item is not None:
            parenthesis_balanced_string += item

    if len(stack_list) == 0:
        print("Los paréntesis están bien balanceados")

    print("num_char_open: ", num_par_open)
    print("num_char_close: ", num_par_close)
    print("stack_list: ", stack_list)
    print("list_of_indexes: \n open: {}, \n closed: {}".format(list_of_indexes_open, list_of_indexes_close))
    # print("Stack_Balanced: ", stack_balanced)
    print("String_Balanced: ", parenthesis_balanced_string)


if __name__ == "__main__":

    # cadena = "(((()))((((((()))))((()))(()())))((()))))))))))))))))"
    # cadena = "(((((((((((((((((((())))))))))))))))))))"
    cadena = "(()"

    balancer(cadena)
