#Here is a code that simulates undo- redo operation. Go through the code and observe how the stack is used in this implementation. And also puxh and pop operations

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size
                                       
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg    
'''First the element is removed from the list and it is pushed in the undo_stack '''
def remove():
    global clipboard,undo_stack
    data=clipboard[len(clipboard)-1]
    clipboard.remove(data)
    undo_stack.push(data)
    print("Remove:",clipboard)

'''if no element is removed from clipboard list then the undo stack will be empty else the removed data stored in undo_stack is again appended in the clipboard list and also it is stored in redo_stack as well 
1. list is first stored in undo_stack
2. store element from the undo_stack that is to be removed
3. append the stored data to clipboard 
'''
def undo():
    global clipboard,undo_stack,redo_stack
    if(undo_stack.is_empty()):
        print("There is no data to undo")
    else:
        data=undo_stack.pop()
        clipboard.append(data)
        redo_stack.push(data)
    print("Undo:",clipboard)

'''if no element is removed from clipboard  or if no undo operation is performed then the redo_stack will be empty else the  
1. list is first stored in redo_stack
2. store element from the redo_stack that is removed
3. push the stored data to undo_stack and remove it from clipboard list
'''

def redo():
    global clipboard, undo_stack,redo_stack
    if(redo_stack.is_empty()):
        print("There is no data to redo")
    else:
        data=redo_stack.pop()
        if(data not in clipboard):
                print("There is no data to redo")
                redo_stack.push(data)
        else:
            clipboard.remove(data)
            undo_stack.push(data)
    print("Redo:",clipboard)



clipboard=["A","B","C","D","E","F"]
undo_stack=Stack(len(clipboard))
redo_stack=Stack(len(clipboard))
remove()
undo()
redo()


#bad code
'''
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top < self.__max_size-1:
            return True
        else:
            return False
                
        #Remove pass and write the logic to check whether stack is full. If the stack is full, return true else return false.

    def push(self,data):
        flag = self.is_full()
        if self.__top == -1:
          self.__top+=1
          self.__elements[self.__top]=data
          print(self.__top)
          print(self.__elements)
        elif(flag):
          self.__top+=1
          self.__elements[self.__top]=data
          print(self.__top)
          print(self.__elements)
        else:
          print("Max size reached")
          #Remove pass and write the logic to push element into the stack. Element should be pushed only if the stack is not full. Otherwise, display appropriate message
    
    def is_empty(self):
        if self.__top == -1:
            return 0
        else:
            return 1
        #Remove pass and write the logic to check whether stack is empty. If the stack is empty, return true else return false.
    
    def pop(self):
        if(self.is_empty()):
            self.__elements.pop()
            self.__top-=1
        #Remove pass and write the logic to pop an element. Pop the element only if stack is not empty. Otherwise, display appropriate message

    def display(self):
        print(self.__elements)
        #Remove pass and write the logic to display the element(s).
                                          
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(5)
#Push all the required element(s).
stack1.push("Shirt1")
stack1.push("Shirt2")
stack1.push("Shirt3")
stack1.push("Shirt4")
stack1.push("Shirt5")
stack1.push("Shirt6")
#Pop an element
print(stack1.pop())
stack1.display()
'''