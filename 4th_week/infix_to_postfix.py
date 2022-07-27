
def infix_to_postfix_fun() -> list : 
    
    Infix_string = list(map(str, input().split()))

    Stack = []
    Postfix_string = []

    index_count = 0
    while True : 
        text = Infix_string[index_count]

        if text in ('()+-*/') :         # text = operator
            
            if text == '(' :            # text = ()
                while True : 
                    index_count += 1
                    text = Infix_string[index_count]

                    if text == ')' : break

                    if text in ('+-*/') : 
                        if len(Stack) == 0 : Stack.append(text)                             # Stack is empty
                        elif text == '*' or text == '/' : Stack.append(text)                # operator in Stakc has lower priority
                        elif Stack[len(Stack) - 1] == '*' or Stack[len(Stack) - 1] == '/' : # operator in Stack has higher priority
                            Postfix_string.append(Stack.pop())
                            Stack.append(text)
                        else : Stack.append(text)

                    else : 
                        Postfix_string.append(int(text))
                
                for i in range(len(Stack)) : 
                    Postfix_string.append(Stack.pop())


            else :                      # text = + - * /
                if len(Stack) == 0 : Stack.append(text)                                 # Stack is empty
                elif text == '*' or text == '/' : Stack.append(text)                    # operator in Stakc has lower priority
                elif Stack[len(Stack) - 1] == '*' or Stack[len(Stack) - 1] == '/' :     # operator in Stack has higher priority
                    Postfix_string.append(Stack.pop())
                    Stack.append(text)
                else : Stack.append(text)


        else :                          # text = number
            Postfix_string.append(int(text))
        
        index_count += 1

        if index_count > len(Infix_string) - 1 :    # searched every text in string
            for i in range(len(Stack)) : 
                Postfix_string.append(Stack.pop())
            break
    
    return Postfix_string

if __name__ == '__main__' : 
    infix_to_postfix_fun()