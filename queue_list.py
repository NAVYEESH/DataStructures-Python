queue=[]
def enqueue():
    element=input()
    queue.append(element)
    print(element,"is added to queue")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop()
        print("removed element")
def display():
    print(queue)
while True:
    print("slelect the operation 1.add 2.remove 3. show 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("select the correct choice")