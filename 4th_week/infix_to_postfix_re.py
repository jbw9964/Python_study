
from collections import deque

def infix_to_postfix_fun() -> list : 
    
    infix_string = deque(map(str, input().split()))

    Postfix_string = []

    Stack = []

    while infix_string : 
        text = infix_string.popleft()
        
        if text in '+-*/' :                     # text = +,-,*,/
            
            if text in '+-' :                   # text = +,-
                
                while Stack :                   # every operator in Stack has to be poped into Postfix string
                    in_stack = Stack.pop()

                    if in_stack in '()' :       # there was () in Stack
                        Stack.append(in_stack)
                        break
                    
                    else : 
                        Postfix_string.append(in_stack)

                Stack.append(text)
            
            else :                              # text = *,/

                while Stack :                   # every operator in Stack has to be poped into Postfix string except + or -
                    in_stack = Stack.pop()

                    if in_stack in '()' :       # there was () in Stack
                        Stack.append(in_stack)
                        break
                    
                    if in_stack in '+-' :       # in_stack = +,-
                        Stack.append(in_stack)
                        break
                    else :                      # in_stack = *,/
                        Postfix_string.append(in_stack)
                    
                Stack.append(text)
        
        elif text == '(' :                      # text = (
            Stack.append(text)
        elif text == ')' :                      # text = )
            
            while True :                        # every operator in Stack has to be poped into Postfix string untill ()
                in_stack = Stack.pop()
                
                if in_stack in '()' :           # in_stack = ()
                    break
                else : 
                    Postfix_string.append(in_stack)

        else :                                  # text = number
            Postfix_string.append(int(text))

    while Stack : 
        in_stack = Stack.pop()
        Postfix_string.append(in_stack)

    return Postfix_string

if __name__ == '__main__' : 
    Postfix = infix_to_postfix_fun()

    for i in Postfix : 
        print(i, end=' ')
    print()