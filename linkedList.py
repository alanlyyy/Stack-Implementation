class Node(object):
    
    def __init__(self,data):
    
        #stores the data
        self.data = data;
        
        #stores the pointer to the next node
        self.nextNode = None;
        

class Linkedlist(object):
    
    def __init__(self):
        #self.head is the pointer for keeping track of current node
        self.head = None
        self.size = 0;
    
    #O(1) because no list traversing required
    def insertStart(self,data):
        
        #increase size when inserting
        self.size = self.size + 1
        
        #create a new node 
        newNode = Node(data)
        
        #if the self.head is empty, self.head will be pointing to first node
        if not self.head:
            self.head = newNode
        #otherwise it will point to the next node
        else:
            #point to the previous node
            newNode.nextNode = self.head;
            #update the current node pointer with the new node
            self.head = newNode
    
    def remove(self,data):
        
        #if list is empty do nothing
        if self.head is None:
            return;
        
        #update the size of the linkedlist
        self.size -= 1
        
        #store the current pointer
        currentNode = self.head
        previousNode = None
        
        #setting the previous node and current node pointers
        while currentNode.data != data:
            
            #store the pointer for current node into previous node
            previousNode = currentNode
            
            #update the pointer to the next node
            currentNode = currentNode.nextNode
            
        #if the current node is null (head of linkedlist) is the node we want to remove
        #Basically for this case, we skip the while loop
        if previousNode is None:
        
            #update the pointer of the next node as the current node
            self.head = currentNode.nextNode
        
        #removing current node by having previous node point to the next node of the current node.
        else:
            
            previousNode.nextNode = currentNode.nextNode
        
    # O(1) time complexity, because does not require iterating through the linked list
    def size1(self):
        return self.size
        
    #O(N) linear time complexity because of looping through entire linkedlist
    def size2(self):
        
        #get the pointer for current node
        actualNode = self.head;
        
        size = 0;
        
        #while the pointer is not pointing to an null object
        while actualNode is not None:
            
            #update the size
            size += 1
            
            #update the pointer to the next node
            actualNode = actualNode.nextNode
            
        return size
    
    #O(N) time complexity because we have to traverse the list to reach the end    
    def insertEnd(self,data):
        
        #update the size
        self.size = self.size + 1
        
        #create a new node
        newNode = Node(data)
        
        #store the pointer of current node
        actualNode = self.head
        
        #while the next node is not pointing to a null
        while actualNode.nextNode is not None:
            
            #update the current pointer to be the next node
            actualNode = actualNode.nextNode
        
        #when next node is pointing to a null, update the pointer to 
        #point to the new node
        actualNode.nextNode = newNode
        
    def traverseList(self):
        
        #store the current pointer to the current node
        actualNode = self.head
        
        #while the current node is not null
        while actualNode is not None:
        
            print("%d" % actualNode.data);
            
            #update the current pointer with the next node
            actualNode = actualNode.nextNode
            

if __name__ == "__main__":
    linkedlist = Linkedlist()
    linkedlist.insertStart(12)
    linkedlist.insertStart(122)
    linkedlist.insertStart(3)
    linkedlist.insertEnd(31)
    
    linkedlist.traverseList() #yieleds 3,122,12,31
    
    print(linkedlist.size1())
    
    linkedlist.remove(31)
    linkedlist.remove(12)
    linkedlist.remove(122)
    linkedlist.remove(3)
    
    print(linkedlist.size1())
