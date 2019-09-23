import stack

#R-6.1
ArrayStack = stack.Stack()
ArrayStack.push(5)
ArrayStack.push(3)
ArrayStack.pop()
ArrayStack.push(2)
ArrayStack.push(8)
ArrayStack.pop()
ArrayStack.pop()
ArrayStack.push(9)
ArrayStack.push(1)
ArrayStack.pop()
ArrayStack.push(7)
ArrayStack.push(6)
ArrayStack.pop()
ArrayStack.pop()
ArrayStack.push(4)
ArrayStack.pop()
ArrayStack.pop()
print("Array stack:",ArrayStack.stack)

#R-62 
#18 operations, 7 successful pops, and 3 non successful pops

#R-63
def transfer(S,T):
    """transfers all data in stack S to stack T,
    where Top of S goes to top of T, while Bot of Stack
    becomes top of T
    """
    
    #copy the data from the stack S
    d = S.stack.copy()
    
    #append data from stack S to stack T
    while d != []:
        T.push(d.pop())
        
    """
    d = S
    while S.isEmpty() == False:
        T.push(d.pop())
    """
    
    return T
        
    
S = stack.Stack()
T = stack.Stack()

S.push(5)
S.push(4)
S.push(3)
S.push(2)
S.push(1)
T = transfer(S,T)
print("S: ", S.stack)
print("T: ", T.stack)

#R6-4
def recursiveRemove(inputStack):
    if inputStack.sizeStack() == 0:
        return inputStack.stack
    else:
        inputStack.pop()
        return recursiveRemove(inputStack)

inputStack = stack.Stack()
inputStack.push(5)
inputStack.push(4)
inputStack.push(3)
inputStack.push(2)
inputStack.push(1)
inputStack.push(0)
print(recursiveRemove(inputStack))

#R6-5
myList = [5,4,3,2,1]

print("Before List: ", myList)
def outStack(inputList):
    
    tempList = inputList
    tempStack = stack.Stack()
    
    while len(tempList) != 0:
        tempStack.push(tempList.pop())
    
    return tempStack.stack
    
print("reversed list:", outStack(myList)) 

#C-6.15
#x = stack.pop()
#x > stack.peek()
#with only having 2 operations we can only compare values
#of the top 2 indexes of the stack, the third item is not touched.

#C6-22
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