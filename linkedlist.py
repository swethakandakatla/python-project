class Node: 
  
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
# Linked List class 
class LinkedList: 
     # Function to initialize the Linked List object 
    def __init__(self):  
        self.head = None
    def insert(self,prev_node,new_data):    
        #inserting after one node
        if prev_node is None:
            return 
        new_Node=Node(new_data)
        new_Node.next=prev_node.next
        prev_node.next=new_Node
        # inserting at the begining
    def push(self,new_data):
        new_Node=Node(new_data)
        new_Node.next=self.head
        self.head=new_Node
        # deletion at the begining
    def del_data(self,key):
        temp=self.head
        while(temp is not None):
            if(temp.data==key):    
                prev_node=temp
                temp=temp.next
       
        prev_node.next=temp.next
        temp=None
    #searching the data in the list
    def search(self,key):
        temp=self.head   
           
        while(temp is not None):
            if(temp.data==key):
               return True
            temp=temp.next               
            
        return False
    def getnthNode(self,index):
        if(self.head==None):
            return
        temp=self.head
        count=0
        while(temp):
            if(count==index):
                return temp.data
            count=count+1
            temp=temp.next
        #reverse indexing
    # def reverseIndex():
    def numberoccurence(self,key):
        count=0
        temp=self.head
        while(temp):
            if(temp.data==key):
                count=count+1
            temp=temp.next
        return count
    def print_linkedlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def removeDuplicates(self):
       
        temp=self.head
        while(temp.next is not None):
            if(temp.data==temp.next.data):
                new=temp.next.next
                temp.next=None
                temp.next=new
            else:
                temp=temp.next
        return self.head

    
       
    def middleNode(self):
        length=0
        middle=0
        if(self.head==None):
            print("empty linkedlist")
        temp=self.head
        while(temp):
            length=length+1
            temp=temp.next
        temp=self.head
        middle=int(length/2)
        for i in range(middle):
            temp=temp.next
        # print(temp.data)
        # print(mid.data)
        return temp.data
      
    # deletion as per the position
    def del_position(self,position):
        if(self.head==None):
             return
        temp=self.head 
        if(position==0):
            self.head=temp.next
            temp=None
            return
        if(temp.next is None):
            return
        for i in range(position-1):
            temp=temp.next
            if(temp is None):
                break

        next=temp.next.next
        temp.next=None
        temp.next=next
    #remove duplicates from set
    def removeDupUsingSet(self):
        s=set()
        if(self.head is None):
            return
        temp=self.head
        while(temp):
            s.add(temp.data)
            temp=temp.next
        print(s)
        return s

    #last node will be first
    def lastNodefirst(self):
        a=0
        b=0
        c=0
        if(self.head==None):
            return
        temp=self.head  
        b=temp.data 
        if(temp is not None):
            temp=temp.next 
            temp=temp.next.next         
            a=temp.next.data  
            c=b
            b=a
            a=c
            temp.next.data=a
            temp=self.head
            temp.data=b
        
                        
        return self.head     
    # Using recurrsion finding the length of the list
    def getCountRec(self, node): 
        if (not node): # Base case 
            return 0
        else: 
            return 1 + self.getCountRec(node.next) 
  
    # A wrapper over getCountRec() 
    def getCount(self): 
       return self.getCountRec(self.head) 

    # def recurLength(self,current):
    #     if self.head is None:
    #         return 0
        
    #     return 1 + recurLength(current.next)       
               
    # def ListLength(self):
    #     return self.recurLength(self.head)
   
        # length=0
        # if(self.head==None):
        #     return
        # else:temp!=None
        # temp=self.head
        # length=length+1
        # temp=temp.next 
        # print("lenght:",length)
        # return self.recurLength()

    def length(self):
        length=0
        if(self.head==None):
            print("empty linkedlist")
        temp=self.head

        while(temp):  
            length=length+1
            temp=temp.next
        return length  
        
    
        # end of the linkedlist
    def end_Linkedlist(self,new_data):
        new_Node=Node(new_data)
        if self.head is None:
          self.head=new_Node
          return  
       
        # new_data.next=None
        a=self.head
        while (a.next):
            a=a.next
        a.next=new_Node
        
            
if __name__ == "__main__":
    llist=LinkedList()
    llist.push(20)
    llist.push(13)
    llist.push(11)
    llist.push(11)
    llist.push(5)
    print(llist.getCount())
    # llist.lastNodefirst()
    # llist.print_linkedlist()
    # print("remove duplicates from set:",llist.removeDupUsingSet())
    # print("length:",llist.recur())
    # llist.insert(llist.head.next,5)
    # print("with duplicates")
    # llist.print_linkedlist()
    # llist.removeDuplicates()
    # print("number occurence:", llist.numberoccurence(5))
    # llist.end_Linkedlist(30)
    # print("search result:",llist.search(3))
    # print("length of the list:",llist.length())
    # print("value of nth node:",llist.getnthNode(3))
    # llist.del_position(2)
    # print("middle data:",llist.middleNode())
    # print("del the data:",llist.del_data(4))
    # print("without duplicates")
    # llist.print_linkedlist()
# llist=LinkedList()
# llist.head=Node(1)
# n2=Node(2)
# n3=Node(3)
# llist.head.next=n2
# n2.next=n3
# llist.end_Linkedlist(4)
# llist.print_linkedlist()