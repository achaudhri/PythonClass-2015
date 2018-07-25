# Ambreen Chaudhri
# HW 5 Singly Linked List

# Need to do: Make a LinkedList class with the following interfaces:
# 1 __init__(self, value): Takes a number and sets it as the value at the head of the List
# 2 length(self): Returns the length of the list
# 3 addNode(self, new_value): Takes a number and adds it to the end of the list
# 4 addNodeAfter(self, new_value, after_node): Takes a number and adds it after the after_node
# 5 addNodeBefore(self, new_value, before_node): Takes a value and adds before the before_node
# 6 removeNode(self, node_to_remove): Removes a node from the list
# 7 removeNodesByValue(self, value): Takes a value, removes all nodes with that value
# 8 reverse(self): Reverses the order of the linked list
# 9 __str(self)__: Displays the list in some reasonable way

# This is the starter definition of a Node class.
class Node(object):
    def __init__(self, _value = None , _next = None):
        self.value = int(_value)
        self.next = _next

    def __str__(self):
        return str(self.value)  

    def addChild(self,new_value):
        if self.next == None:
            self.next = Node(new_value)
        else:
            self.next.addChild(new_value)

    def concatChild(self, head): 
        if self.next == None:
            return str(self.value)
        else:
            return str(self.value) + ", " + self.next.concatChild(head)

    def height(self, head):
        if self.next == None or self.next == head:
            return 1
        else:
            return self.next.height(head) + 1

    def index(self,position):
        if position != 0 and self.next == None:
            return "The index is out of range."
        elif position == 0:
            return self
        else:
            temp = position - 1
            return self.next.index(temp)

    def checkValues(self,check):
        if self.value == check:
            return True
        else:
            return False

# This is the LinkedList class. 
class LinkedList(object):

#1 Takes a number and sets it as the value at the head of the List
    def __init__(self,_node=None):  
        if _node != None:
            self.head = Node(_node)
        else:
            self.head=_node
                            
#2. Returns the length of the list
    def length(self):                
        return self.head.height(self.head)


    def instanceCounter(self, value_to_count):
        instance_count = 0
        temp_length = self.head.height(self.head)-1
        x = self.head.next
        while (temp_length > 0) & (x != None):
            if x.value == value_to_count:
                instance_count += 1            
            temp_length -= 1
            x = x.next
        return instance_count 

#3. Takes a number and adds it to the end of the list
    def addNode(self,new_value):     
        if self.head == None:
            self.head = Node(new_value)
        else:
            self.head.addChild(new_value)

#4. Takes a number and adds it after the after_node.  Note that after_node takes the index
# of the value so after_node = 0, places the new_value in front of the head of the linked list.
    def addNodeAfter(self, new_value, after_node):
        if after_node == 0:
            insertPoint = self.head
        else:
            insertPoint = self.head.index(after_node)
        addedNode = Node(new_value,insertPoint.next)
        insertPoint.next = addedNode

#5. Takes a value and adds before the before_node.  Again it is based on the index of the list. 
    def addNodeBefore(self, new_value, before_node):
        if before_node == 0:
            oldhead = self.head
            self.head = Node(new_value,oldhead)
        else:
            insertPoint = self.head.index(before_node - 1)
            addedNode = Node(new_value,insertPoint.next)
            insertPoint.next = addedNode

#6. Removes a node from the list.  Again it is based on the index of the list. 
    def removeNode(self, node_to_remove):
        if node_to_remove == 0:
            newhead = self.head.next
            self.head = newhead
            return
        preRemNode = self.head.index(node_to_remove - 1)
        if node_to_remove == self.length() -1:
            preRemNode.next = None
        else:
            postRemNode = self.head.index(node_to_remove + 1)
            preRemNode.next = postRemNode

#7. Takes a value, removes all nodes with that actual value.  This I had to look up.  Notice
# the while statement!  
    def removeNodesByValue(self, value_to_remove):
        current = self.head
        if current.value == value_to_remove: 
            self.head = self.head.next
        removed = False
        occurrences_of_value = self.instanceCounter(value_to_remove)
        if occurrences_of_value > 0:
            while removed == False:
                if current.next.value == value_to_remove:
                    current.next, current = current.next.next, None
                    removed = True
                else: current = current.next
            self.removeNodesByValue(value_to_remove)  
                              
#8. This reverses the list.             
    def reverse(self):
        for i in range(1,self.length()):
            newhead = self.head.index(i).value
            self.addNodeBefore(newhead,0)
            self.removeNode(i+1)
        return self

#9. This returns a string for all the list elements in order. 
    def __str__(self):
        try:
            return self.head.concatChild(self.head)
        except:
            if self.head == None:
                return "This is an empty list."        
        
######  These are some tests ##########


# mylist = LinkedList(7)
# print mylist.__str__()
# print mylist.length()
# mylist.addNode(82)  
# mylist.addNode(65)      
# print mylist.__str__()
# mylist.length()
# mylist.addNodeAfter(15,1)
# mylist.addNodeAfter(234,0)  # this places the value in the first position   
# mylist.addNodeBefore(5,3)
# print mylist.__str__() 
# mylist.removeNode(0)
# print mylist.__str__() 
# mylist.removeNodesByValue(234)
# print mylist.__str__() 
# mylist.reverse()
# print mylist.__str__() 



