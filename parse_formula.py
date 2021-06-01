import re

input_rules = [
    [1, 1, 3, 'rule 1', 'Rule 1: Marker DA + Marker IB = Marker RA', 'LHS',
     'mark_da', 700, '+', 'N', 1],
    [2, 2, 3, 'rule 1', 'Rule 1: Marker DA + Marker IB = Marker RA', 'LHS',
     'mark_ib', 800, '=', 'N', 1],
    [3, 3, 3, 'rule 1', 'Rule 1: Marker DA + Marker IB = Marker RA', 'RHS',
     'mark_ra', 1000, '', 'N', 1],
    [4, 1, 2, 'rule 2', 'Rule 2: A >or= 90% of B', 'LHS', 'a', 100, '>=90%',
     'N', 1],
    [5, 2, 2, 'rule 2', 'Rule 2: A >or= 90% of B', 'RHS', 'a', 100, '', 'N',
     1],
    [6, 1, 2, 'rule 3', 'Rule 3: Sum of A and C <= 200 threshold (no RHS)',
     'LHS', 'a', 200000, '+', 'Y', 1000],
    [7, 2, 2, 'rule 3', 'Rule 3: Sum of A and C <= 200 threshold (no RHS)',
     'LHS', 'c', -100, '=<200', 'Y', 1],
    [8, 1, 5, 'rule 4',
     'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'LHS', 'A1',
     1000, '(+', 'N', 1],
    [9, 2, 5, 'rule 4',
     'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'LHS', 'A2', 350,
     '+', 'N', 1],
    [10, 3, 5, 'rule 4',
     'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'LHS', 'A3', 250,
     ')/', 'N', 1],
    [11, 4, 5, 'rule 4',
     'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'LHS',
     'days_mth_end', 16, '==', 'N', 1],
    [12, 5, 5, 'rule 4',
     'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'RHS', 'B1', 100,
     '', 'N', 1],
]

FIRST_RULE_ROW = 1
START_BRACKET_EXPRESSION = ['(+', '(-', '(*', '(/']
SPLIT_FORMULA_SIGNS = re.compile('<=|=|<>|!=|>=|=<|=>|>|<|==')
EQUAL_SIGN = re.compile('==|<=|>=|!=|=<|=>')


def modify_value(value, divider):
    return f"{value}/{divider}" if divider != 1 else value


def modify_amount(amount, use_if_negative, divider):
    if amount < 0 and use_if_negative == 'Y':
        return '0'
    return modify_value(amount, divider)


def add_brackets(expression, value):
    bracket = ''
    if expression in START_BRACKET_EXPRESSION:
        bracket = '('
        expression = expression[1:]
    return f"{bracket}{value}{expression}"


def split_formula(result_amount):
    return SPLIT_FORMULA_SIGNS.split(result_amount)


def evaluate_amount(result_amount):
    result_amount = result_amount.replace("%", "*1/100*")
    return eval(result_amount.replace("=", "==")) if not EQUAL_SIGN.search(
        result_amount) \
        else eval(
        result_amount.replace("<>", "!=").replace("=<", "<=").replace("=>",
                                                                      ">="))


def calc_output(rules):
    output = []

    for rule in rules:
        _, order_number, last_row_rule, rule_id, description, _, cell_id, \
        amount, expression, zero_if_negative, divider = rule

        if order_number == FIRST_RULE_ROW:
            result_formula = ''
            result_amount = ''

        cell_id = modify_value(cell_id, divider)
        amount = modify_amount(amount, zero_if_negative, divider)

        result_formula += add_brackets(expression, cell_id)
        result_amount += add_brackets(expression, amount)

        if order_number == last_row_rule:
            valid_status = evaluate_amount(result_amount)
            lhs, *_, rhs = split_formula(result_amount)
            value_lhs = evaluate_amount(lhs)
            value_rhs = evaluate_amount(rhs)
            output.append((rule_id, description, result_formula, result_amount,
                           valid_status, value_lhs, value_rhs))
    return output


calc_output(input_rules)