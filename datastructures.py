mobile=['nokia','samsung']
mobile.insert(1,'reliance')
top=mobile[0];
print(mobile)
dict={'a':"apple",'b':"ball",'c':"cat"}
print(dict['b'])
for i in dict:
	print(i)
class Queue:
	    def __init__(self):
	        self.items = []
	
	    def isEmpty(self):
	        return self.items == []
	
	    def enqueue(self, item):
	        self.items.insert(0,item)
	
	    def dequeue(self):
	        return self.items.pop()
	
	    def size(self):
	        return len(self.items)

q=Queue()
q.isEmpty()
q.enqueue('dog')
q.enqueue(4)
q.dequeue()
q=Queue()
q.isEmpty()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
