class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        print(f"{val} pushed into stack")

    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"{removed} removed from stack")
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            print("Top element:", self.stack[-1])
        else:
            print("Stack is empty")

    def display(self):
        print("Stack:", self.stack)

    def is_empty(self):
        return len(self.stack) == 0


# Create stack
s = Stack()

while True:
    print("\n--- Stack Operations ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        val = int(input("Enter value to push: "))
        s.push(val)

    elif choice == "2":
        s.pop()

    elif choice == "3":
        s.peek()

    elif choice == "4":
        s.display()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")