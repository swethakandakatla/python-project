class Queue:
    def __init__(self,capacity):
        self.front= self.size=0
        #capacity is the length of the queue
        self.rear=capacity-1
        self.Q = [None]*capacity 
        self.capacity = capacity
    def Qisfull(self):
        return self.capacity==self.size
    def Qisempty(self)
        return self.size=0
    def enQueue(self):
        if(self.Qisfull()):
            print("queue is full")
            return
        self.rear = (self.rear + 1) % (self.capacity) 
        self.Q[self.rear] = item 
        self.size = self.size + 1
        print("% s enqueued to queue"  % str(item)) 
  
    # Function to remove an item from queue.  
    # It changes front and size 
    def DeQueue(self): 
        if self.Qisempty(): 
            print("Empty") 
            return
          
        print("% s dequeued from queue" % str(self.Q[self.front])) 
        self.front = (self.front + 1) % (self.capacity) 
        self.size = self.size -1

    def que_front(self): 
        if self.isEmpty(): 
            print("Queue is empty") 
  
        print("Front item is", self.Q[self.front]) 
          
    # Function to get rear of queue 
    def que_rear(self): 
        if self.isEmpty(): 
            print("Queue is empty") 
        print("Rear item is",  self.Q[self.rear]) 
        
# class Queue:
#     def __init__(self):
#        self.items=[]
#     def enqueue(self,item):
#        self.items.append(item)
#     def dequeue(self):
#        return self.items.pop(0)
#     def isEmpty(self):
#        return self.items==[]
#     def __len__(self):
#        return len(self.items)
# q=Queue()     
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(50)
# print("enqueue the elements:",q.enqueue(60))

# print("delete the element from Queue",q.dequeue())





       

