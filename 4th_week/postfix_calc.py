
def postfix_calc_fun(Postfix : list) -> int :
    Stack = []

    for text in Postfix : 

        if type(text) == str :   # num_1 num_2 (oper) --> num_1 (oper) num_2
            num_2 = Stack.pop()
            num_1 = Stack.pop()
            
            if text == '+' : Stack.append(num_1 + num_2)
            elif text == '-' : Stack.append(num_1 - num_2)
            elif text == '*' : Stack.append(num_1 * num_2)
            else : Stack.append(num_1 / num_2)              # a b / --> a / b
        
        else : 
            Stack.append(int(text))
        
    return Stack[0]
