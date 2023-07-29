import queue
stack = queue.LifoQueue()
def push_element():
    element = input("Enter the element: ")
    stack.put(element)
    print(stack.queue)

def pop_element():
    if stack.empty():
        print("Stack is empty!")
    else:
        remove_element = stack.get()
        print(f"Remove {remove_element} from stack")
        print(stack.queue)

while True:
    print("Enter your operation: 1. put 2. get 3. Quit")
    choice = int(input())

    if choice == 1:
        push_element()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter correct operation.")
