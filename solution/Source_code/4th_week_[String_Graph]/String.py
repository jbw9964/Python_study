
from infix_to_postfix_re import infix_to_postfix_fun

N = int(input())

Postfix = []
for _ in range(N) : 
    Postfix.append(infix_to_postfix_fun())

Result = []

def postfix_calc_fun(Postfix : list) -> int :
    Stack = []

    for text in Postfix : 

        #------------------------------------------------------------#
        # 3. text 가 연산자일 경우, Stack 에서 2 개를 pop 해 서로 연산을 진행하고 결과를 다시 Stack 에 넣는다.

        if type(text) == str :                              # num_1 num_2 (text) --> num_1 (text) num_2
            num_2 = Stack.pop()
            num_1 = Stack.pop()
            
            if text == '+' : Stack.append(num_1 + num_2)
            elif text == '-' : Stack.append(num_1 - num_2)
            elif text == '*' : Stack.append(num_1 * num_2)
            else : Stack.append(num_1 / num_2)              # a b / --> a / b
        
        #------------------------------------------------------------#
        # 2. text 가 숫자일 경우 Stack 에 넣는다.

        else : 
            Stack.append(int(text))
        
        #------------------------------------------------------------#
        # end for
        
    return Stack[0]

for i in range(N) : 
    Result.append(postfix_calc_fun(Postfix[i]))

print()
for i in range(N) : 
    current = Postfix[i]

    for string in current : 
        print(string, end=' ')
    print()
for value in Result : 
    if type(value) == int : print(value)
    else : print(f"{value:.3f}")
