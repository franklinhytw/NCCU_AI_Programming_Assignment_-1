from queue import PriorityQueue

q = PriorityQueue()
text = "asd"
q.put("s",1)
q.put("q",3)
q.put("a",2)
q.put("z",1)

while not q.empty(): 
    print(q.get())

print(q)