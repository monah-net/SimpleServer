import re

inputRules = [
[1, 1, 3, 'rule 1', 'Rule 1: Marker DA + Marker IB = Marker RA', 'LHS', 'mark_da', 700, '+', 'N', 1],
[2, 2, 3, 'rule 1', 'Rule 1: Marker DA + Marker IB = Marker RA', 'LHS', 'mark_ib', 800, '=', 'N', 1],
[3, 3, 3, 'rule 1', 'Rule 1: Marker DA + Marker IB = Marker RA', 'RHS', 'mark_ra', 1000, '', 'N', 1],
[4, 1, 2, 'rule 2', 'Rule 2: A > 90% of B', 'LHS', 'a', 100, '>90%', 'N', 1],
[5, 2, 2, 'rule 2', 'Rule 2: A > 90% of B', 'RHS', 'a', 100, '', 'N', 1],
[6, 1, 2, 'rule 3', 'Rule 3: Sum of A and C = 200 threshold (no RHS)', 'LHS', 'a', 200000, '+', 'Y', 1000],
[7, 2, 2, 'rule 3', 'Rule 3: Sum of A and C = 200 threshold (no RHS)', 'LHS', 'c', -100, '=200', 'Y', 1],
[8, 1, 5, 'rule 4', 'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'LHS', 'A1', 1000, '(+', 'N', 1],
[9, 2, 5, 'rule 4', 'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'LHS', 'A2', 350, '+', 'N', 1],
[10, 3, 5, 'rule 4', 'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'LHS', 'A3', 250, ')/', 'N', 1],
[11, 4, 5, 'rule 4', 'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'LHS', 'days_mth_end', 16, '=', 'N', 1],
[12, 5, 5, 'rule 4', 'Rule 4: (A1+A2+A3)/days number in 2nd half month = B1', 'RHS', 'B1', 100, '', 'N', 1],
]

ORDER_NUMB_RULE = 1
LAST_ROW_RULE = 2
RULE_ID = 3
RULE_DESCRIPTION = 4
CELL_ID = 6
AMOUNT = 7
EXPRESSION = 8
ZERO_IF_NEGATIVE = 9
DIVIDER = 10
FIRST_RULE_ROW = 1
START_BRACKET_EXPRESSION = ['(+', '(-', '(*', '(/']
SPLIT_FORMULA_SIGNS = '(<=)|(=)|(<>)|(!=)|(>=)|(=<)|(=>)|(>)|(<)|(==)'
PY_EQUELTY_SIGNS = '(=>)|(>=)|(=<)|(<=)|(!=)'

def fModifyCellID(cellID, divider):
    if divider != 1:
        return cellID + '/' + str(divider)
    else:
        return cellID
        
def fModifyAmount(amount, useIfNegative, divider):
    if amount < 0 and useIfNegative == 'Y':
        return '0'
    if divider != 1:
       return str(amount) + '/' + str(divider)
    else:
       return str(amount)

def fPercentageReplacement(resultAmt):
    return re.sub("%", "*1/100*", resultAmt)
    
def fSplitFormula(resultAmtEval):
    return re.split(SPLIT_FORMULA_SIGNS, resultAmtEval)
    
def fAmountEvaluation(resultAmtEval):
    if not bool(re.search(PY_EQUELTY_SIGNS, resultAmtEval)):
        resultAmtEvalFixed = re.sub("<>", "!=", re.sub("=", "==", resultAmtEval))
        return eval(resultAmtEvalFixed)
    else: 
        return eval(resultAmtEval)

def fOutputCalc(inputData):
    nRowInputData=len(inputData)
    outputData = []
    for nRow in range(nRowInputData):
        modifiedCellID = fModifyCellID(inputData[nRow][CELL_ID], inputData[nRow][DIVIDER])
        modifiedAmount = fModifyAmount(inputData[nRow][AMOUNT], inputData[nRow][ZERO_IF_NEGATIVE], 
                                        inputData[nRow][DIVIDER])

        if inputData[nRow][ORDER_NUMB_RULE] == FIRST_RULE_ROW:
            resultFormula = ''
            resultAmount = ''
     
        if inputData[nRow][EXPRESSION] in START_BRACKET_EXPRESSION:
            resultFormula = resultFormula + '(' + modifiedCellID + re.sub("\(", "", inputData[nRow][EXPRESSION])
            resultAmount = resultAmount + '(' + modifiedAmount + re.sub("\(", "", inputData[nRow][EXPRESSION])
        else:
            resultFormula = resultFormula + modifiedCellID + inputData[nRow][EXPRESSION]
            resultAmount = resultAmount + modifiedAmount + inputData[nRow][EXPRESSION]     

        if inputData[nRow][ORDER_NUMB_RULE] == inputData[nRow][LAST_ROW_RULE]:
            resultAmtForEval = fPercentageReplacement(resultAmount)
            validStatus = fAmountEvaluation(resultAmtForEval)
            valueLHS = fAmountEvaluation(fSplitFormula(resultAmtForEval)[0])
            valueRHS = fAmountEvaluation(fSplitFormula(resultAmtForEval)[-1])
            outputData.append([inputData[nRow][RULE_ID], inputData[nRow][RULE_DESCRIPTION], 
                                resultFormula, resultAmount, resultAmtForEval, validStatus, valueLHS, valueRHS])
    return outputData    

fOutputCalc(inputRules)
