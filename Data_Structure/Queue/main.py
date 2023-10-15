queue = []
def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(queue)

def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        remove_element = queue.pop(0)
        print(f"Remove {remove_element} from queue")
        print(queue)

while True:
    print("Enter your operation: 1. Push 2. Pop 3. Quit")
    choice = int(input())

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("Enter correct operation.")
