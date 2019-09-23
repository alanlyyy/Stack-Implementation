import stack

def postFixResult(expression):

    #expression = "((5+2)*(8-3))/4"
    
    #preprocessing of string
    exp = expression
    exp.replace(" ", "") #strip all white space
    
    #store delimeters "( )"
    postFixStack = stack.Stack()
    
    #store numbers and operations
    numStack = stack.Stack() #ex) 5 - 2 / 4 , or non processed output
    
    #store the running the postfix expression 
    tempStack    = stack.Stack() #ex) 5 2 - 4 / processed output
    
    #flip the stack to reverse order of list for numerical values
    outStack = stack.Stack()
    
    lefty = "({[" # opening delimiters 
    righty = ")}]" # respective closing delims
    operations = "*+-/"
    
    #store operations temporarily
    temp_operation = []
    
    for c in exp:
        if c in lefty:
            postFixStack.push(c) # push left delimiter on stack
            
        #if a right delimeter is detected evaluate the expression
        elif c in righty:
            postFixStack.push(c)
            
            #go through num stack and evaluate expression
            while numStack.isEmpty() == False:
                
                #check if we have an operation in the expression
                if numStack.peek() in operations:
                    temp_operation.append(numStack.pop())
                    
                #not an operation, just an number
                else:
                    tempStack.push(numStack.pop())
            
            #reverse order of numerical values in list
            while tempStack.isEmpty() == False:
                outStack.push(tempStack.pop())
                
            #append operations at the end of the output Stack
            for operation in temp_operation:
                outStack.push(operation)
                
            #reset the list of operations
            temp_operation = []
                
        else:
            #push numbers and operations into numstack
            numStack.push(c)
        
    #reset the list
    temp_operation = []
            
    #go through num stack and evaluate final expressions not bounded by delimeters " ( ) "
    while numStack.isEmpty() == False:
        
        #check if we have an operation in the expression
        if numStack.peek() in operations:
            temp_operation.append(numStack.pop())
        else:
            tempStack.push(numStack.pop())
            
    #reverse order of numerical values in list
    while tempStack.isEmpty() == False:
        outStack.push(tempStack.pop())
    
    #append operations at the end after the numbers
    for operation in temp_operation:
        outStack.push(operation)
        
    
    return outStack
    

expr1 = "((5*2)/4)+(5-2))"
expr2 = "(4+2)"
expr3 = "((6*9)-5)"
expr4 = "(((3/4)*2)+(3*7)/4)"

print(postFixResult(expr1).stack)
print(postFixResult(expr2).stack)
print(postFixResult(expr3).stack)
print(postFixResult(expr4).stack)