# Write here the code challenge solution

def validate_Parentheses(sequence):

    '''Given a string s containing the characters '(', ')', '{', '}', '[' and ']', then validate the input string , Open & Close brackets must same type of brackets and correct order. 
    Function to pair if sequence contains valid parenthesis
    :param sequence: Sequence of brackets
    :return: True is sequence is valid else False
    '''
    
    stack = []

    opening = ('([{')
    closing = (')]}')
    pair = {')' : '(' , ']' : '[' , '}' : '{'}

    for i in sequence :

        if i in opening :
            stack.append(i)
            
        if i in closing :
            if not stack :
                return False
            elif stack.pop() != pair[i] :
                return False
            else :
                continue
            
    if not stack :
        return True
    else :
        return False

if __name__ == '__main__':
   sequence = '{[()]}'
   print(f'Is {sequence} valid ? : {validate_Parentheses(sequence)}')
   sequence1 = '{[()]}{]{}}'
   print(f'Is {sequence1} valid ? : {validate_Parentheses (sequence1)}')

    
