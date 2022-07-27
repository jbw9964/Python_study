
from infix_to_postfix import infix_to_postfix_fun

N = int(input())

Postfix = []
for _ in range(N) : 
    Postfix.append(infix_to_postfix_fun())

Result = []

def postfix_calc_fun(Postfix : list) -> int :
    Stack = []

    for text in Postfix : 

        if type(text) == str :          # num_1 num_2 (text) --> num_1 (text) num_2
            num_2 = Stack.pop()
            num_1 = Stack.pop()
            
            if text == '+' : Stack.append(num_1 + num_2)
            elif text == '-' : Stack.append(num_1 - num_2)
            elif text == '*' : Stack.append(num_1 * num_2)
            else : Stack.append(num_1 / num_2)              # a b / --> a / b
        
        else : 
            Stack.append(int(text))
        
    return Stack[0]

for i in range(N) : 
    Result.append(postfix_calc_fun(Postfix[i]))

print()
# for i in range(N) : 
#     current = Postfix[i]

#     for string in current : 
#         print(string, end=' ')
#     print()
for value in Result : 
    if type(value) == int : print(value)
    else : print(f"{value:.3f}")
