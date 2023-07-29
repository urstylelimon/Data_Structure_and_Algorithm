import collections
stack = collections.deque()
def push_element():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is empty!")
    else:
        remove_element = stack.pop()
        print(f"Remove {remove_element} from stack")
        print(stack)

while True:
    print("Enter your operation: 1. Push 2. Pop 3. Quit")
    choice = int(input())

    if choice == 1:
        push_element()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter correct operation.")
