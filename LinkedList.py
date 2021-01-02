#Here is a code that implements memory compaction process. Go through the below code and observe how linked list is used for #its implementation.
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    #This method is added for this tryout alone
    def set_head(self,new_node):
        self.__head=new_node

    #This method is added for this tryout alone
    def set_tail(self,new_node):
        self.__tail=new_node

    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list") 
                                        
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


def find_total_nodes(mem_block):
    temp=mem_block.get_head()
    total_nodes=0
    while(temp is not None):
        total_nodes+=1
        temp=temp.get_next()

    return total_nodes

def maximum_contiguous_free_blocks(mem_block):
    temp=mem_block.get_head()
    total_nodes=find_total_nodes(mem_block)
    free_list=[]
    free_contiguous_nodes=0
    if(temp.get_data()=="Free"):
        free_contiguous_nodes+=1
    prev_data=temp.get_data()
    temp=temp.get_next()
    while(temp is not None):
        if(temp.get_data()=="Free"):
                if(prev_data=="Free"):
                    free_contiguous_nodes+=1
                else:
                    free_list.append(free_contiguous_nodes)
                    free_contiguous_nodes=1
        else:
            free_list.append(free_contiguous_nodes)
            free_contiguous_nodes=0

        prev_data=temp.get_data()
        temp=temp.get_next()
    free_list.append(free_contiguous_nodes)
    max_free_contiguous_nodes=max(free_list)
    return((max_free_contiguous_nodes/total_nodes)*100)

def total_free_blocks(mem_block):
    temp=mem_block.get_head()
    total_blocks=find_total_nodes(mem_block)
    total_free_blocks=0
    while(temp is not None):
        if(temp.get_data()=="Free"):
            total_free_blocks+=1
        temp=temp.get_next()
    return ((total_free_blocks/total_blocks)*100)

def memory_compaction(mem_block):
    temp=mem_block.get_head()
    prev_occupied=None
    prev_free=None
    occupied=None
    free=None
    if(temp.get_data()=="Occupied"):
            occupied=temp
            prev_occupied=temp
    elif(temp.get_data()=="Free"):
            free=temp
            prev_free=temp
    temp=temp.get_next()
    while(temp is not None):
        if(temp.get_data()=="Occupied"):
            if(occupied==None):
                occupied=temp
            if(prev_occupied==None):
                prev_occupied=temp
            else:
                prev_occupied.set_next(temp)
                prev_occupied=temp
        elif(temp.get_data()=="Free"):
            if(free==None):
                free=temp
            if(prev_free==None):
                prev_free=temp
            else:
                prev_free.set_next(temp)
                prev_free=temp
        temp=temp.get_next()

    prev_occupied.set_next(free)
    prev_free.set_next(None)
    mem_block.set_head(occupied)
    mem_block.set_tail(prev_free)

mem_block=LinkedList()
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Free")
mem_block.add("Free")
mem_block.add("Free")

print("Before compaction")
print("_________________")
print("Max. contiguous free blocks:", maximum_contiguous_free_blocks(mem_block),"%")
print("Total free blocks:",total_free_blocks(mem_block),"%")

memory_compaction(mem_block)

print()
print("After compaction")
print("________________")
print("Max. contiguous free blocks:", maximum_contiguous_free_blocks(mem_block),"%")
print("Total free blocks:",total_free_blocks(mem_block),"%")




# LinkedList 1 only add display and find
'''class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node = Node(data)
        if self.__head == None:
            self.__head = new_node
            return
        last = self.__head
        while(last.get_next()):
            last = last.get_next()
        last.set_next(new_node)
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        temp = self.__head
        while(temp):
            print(temp.get_data())
            temp = temp.get_next()
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        temp = self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp = temp.get_next()
        return None
        #Remove pass and write the logic to find the node and return the node if found or return None.
                                            
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
list1.add('Sugar')
list1.add('Milk')
list1.add('Salt')
list1.display()
#Add all the required element(s)
#Search for the required node
node=list1.find_node("Milk")
if(node!=None):
    print("Node found")
else:
    print("Node not found") 
  '''
    
  
#LinkedList 2 add, display, find, insert before and delete node
'''
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node = Node(data)
        if self.__head == None:
            self.__head = new_node
            return
        last = self.__head
        while(last.get_next()):
            last = last.get_next()
        last.set_next(new_node)
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        temp = self.__head
        while(temp):
            print(temp.get_data())
            temp = temp.get_next()
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        temp = self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp = temp.get_next()
        return None
        #Remove pass and copy the code you had written to find the node containing the element.
    
    def insert(self,data,data_before):
        new_node = Node(data)
        if self.__head == None:
            self.__head = new_node
            return
        before_node = self.find_node(data_before)
        if before_node != None:
            new_node.set_next(before_node.get_next())
            before_node.set_next(new_node)
        #Remove pass and write the logic to insert an element.
    
    def delete(self,data):
        delete_node = self.__head
        if delete_node is not None:
            if delete_node.get_data() == data:
                self.__head = delete_node.get_next()
                delete_node = None
                return
        while delete_node is not None:
            if delete_node.get_data() == data:
                break
            prev = delete_node
            delete_node = delete_node.get_next()
        if delete_node == None:
            return
        prev.set_next(delete_node.get_next()) 
        delete_node = None
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
list1.add('Sugar')
list1.add('Milk')
#Add all the required element(s)
#Insert the element in the required position
list1.insert("NewItem","Sugar")
list1.display()

list1.delete("Milk")
list1.display()
   '''



   