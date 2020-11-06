# node class
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    # method to update the data of the Node
    def updateData(self, data):
        self.data = data

    # method to set Link for the Next Node
    def setLink(self, node):
        self.link = node

    # method returns data stored in the Node
    def getData(self):
        return self.data

    # method returns address of the next Node // goes to the Next Node
    def getNextNode(self):
        return self.link

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # method adds elements to the left of the Linked List
    def addToStart(self, data):# 21
        # create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    # method adds elements to the right of the Linked List
    def addToEnd(self, data): # data = 16
        start = self.head
        tempNode = Node(data) # data = 16 : link = None
        # start  = 5
        # reach the last element TAIL
        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return True

    # method displays Linked List
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!")
            return None

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # method returns length of linked list
    def length(self):
        start = self.head
        size = 0
        while start:# start != None
            size += 1
            start = start.getNextNode()
        # print(size)
        return size

    # method returns index of the recieved data
    def index(self, data):
        start = self.head
        position = 1

        while start:
            if start.getData() == data:
                return position
            else:
                position += 1
                start = start.getNextNode()


    # method removes item passed from the Linked List
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        # if previous is None then the data is found at first position
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found

    # method returns max element from the List
    def Max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                 largest = start.getData()
            start = start.getNextNode()
        return largest

    # method returns minimum element of Linked list
    def Min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    # method pushes element to the Linked List
    def push(self, data):
        self.addToEnd(data)
        return True

    # method removes and returns the last element from the Linked List
    def pop(self):
        start = self.head
        previous = None

        while start.getNextNode():
            previous = start
            start = start.getNextNode()

        if previous is None:
            self.head = None
        else:
            previous.setLink(None)
            data = start.getData()
            del start
            return data

    # method to clear LinkedList
    def clear(self):
        self.head = None
        return True


    # method returns count of Element recieved
    def count(self, element):
        start = self.head
        count1 = 0
        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
        return count1
    
    #Print first K elements in the Linked List 
    def get(self, index):
        if index >= self.length():
            print("ERROR: Index out of range!")
            return None
        cur_index = 1
        cur_node = self.head
        while True:
            if cur_index == index:
                return cur_node.getData()
            print(str(cur_node.getData()), end=" ")
            cur_node = cur_node.getNextNode()
            cur_index = cur_index + 1
    
    #Push in O(1)
    def newpush(self, data):
        start = self.tail
        temp_node = Node(data)
        start.setLink(temp_node)
        del temp_node
            
    #Reverse the Linked List 
    def reverse(self):
        previous = None
        start = self.head
        
        if start is None:
            print("Empty List!")
            return None
        
        after = start.getNextNode()
        while after is not None:
            start.link = previous
            previous = start
            start = after
            after = after.getNextNode()
        start.link = previous
        self.head = start
        
    #Copy the Linked List
    def copy(self):
        newLL = LinkedList()
        start = self.head
        
        while start is not None: # <- refer kepada newList punya kepala
            tempNode = Node(start.getData())
            newLL.head = tempNode
            tempNode.setLink(self.head)

            return newLL
    
    #Convert the Linked List to a List :
    def copyToList(self):
        start = self.head
        lists = []
        
        while start is not None:
            lists.append(start.getData())
            start = start.link
            
        return lists
    
    #Check if the Linked List is Sorted in Ascending Order :
    def checkAsc(self):
        start = self.head
        while start.link is not None: 
            n = start
            
            if n.data >= n.link.data: 
                return False
            start = start.getNextNode()
        return True; 
    
    #Check if the Linked List is Sorted in Descending Order :
    def checkDes(self):
        start = self.head
        while start.link is not None: 
            n = start
            
            if n.data <= n.link.data: 
                return False
            start = start.getNextNode()
        return True;
    
        
    #Swap 2 indexes in the Linked List
    def swap(self, x, y):
        if x == y:
            print("Cannot Same")
            return  
  
        # Find x
        previous_x = None
        cur_x = self.head 
        while cur_x != None and cur_x.data != x: 
            previous_x = cur_x 
            cur_x = cur_x.link
  
        # Find y
        previous_y = None
        cur_y = self.head 
        while cur_y != None and cur_y.data != y: 
            previous_y = cur_y 
            cur_y = cur_y.link
  
        if cur_x == None or cur_y == None: 
            print("both x and y are not found")
            return 

        if previous_x != None: 
            previous_x.link = cur_y 
        else: 
            self.head = cur_y 
  
        if previous_y != None: 
            previous_y.link = cur_x 
        else: 
            self.head = cur_x 
  
        temp = cur_x.link
        cur_x.link = cur_y.link
        cur_y.link = temp 
        
   
    
