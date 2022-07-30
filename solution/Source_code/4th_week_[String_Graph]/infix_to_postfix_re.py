
from collections import deque

def infix_to_postfix_fun() -> list : 
    
    # 1. 입력받은 문자열을 Queue 에 넣은 후, 하나씩 pop 시키며 생각한다. pop 시킨 문자를 text 라 하자.
    infix_string = deque(map(str, input().split()))

    Postfix_string = []

    Stack = []

    while infix_string : 
        text = infix_string.popleft()
    
        #---------------------------------------------------------------#
        # 3. text 가 연산자일 경우 Stack 에 넣어야 한다.
        # 4. text 가 연산자 중 +,-,*,/ 이면, Stack 내부의 연산자 중 자신보다 높거나 같은 우선순위를 가진 연산자들은 모두 pop 시켜 Postfix_string 에 넣어야 한다.

        if text in '+-*/' :                     # text = operator except ()
            
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
        
        #---------------------------------------------------------------#
        # 5. text 가 ( 이면 그냥 Stack 에 넣고, ) 이면 pop 된 연산자가 ( 일 때까지 Stack 을 pop 시켜 Postfix_string 에 넣어야 한다.

        elif text == '(' :                      # text = (
            Stack.append(text)
        elif text == ')' :                      # text = )
            
            while True :                        # every operator in Stack has to be poped into Postfix string untill ()
                in_stack = Stack.pop()
                
                if in_stack in '()' :           # in_stack = ()
                    break
                else : 
                    Postfix_string.append(in_stack)

        #---------------------------------------------------------------#
        # 2. text 가 숫자일 경우 Postfix_string 에 넣는다.

        else :                                  # text = number
            Postfix_string.append(int(text))

        #---------------------------------------------------------------#
        # end while

    # 6. 모든 text 를 둘러보았을 때, Stack 내부에 남아있는 연산자들을 모두 Postfix_string 에 넣는다.

    while Stack : 
        in_stack = Stack.pop()
        Postfix_string.append(in_stack)

    return Postfix_string

if __name__ == '__main__' : 
    Postfix = infix_to_postfix_fun()

    for i in Postfix : 
        print(i, end=' ')
    print()