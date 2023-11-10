from stack import Stack

S = Stack()
State = ["a","a","a","a","a"]
State[0] = "blank"
State[1] = "<html>"
State[2] = "<head>"
State[3] = "<body>"
State[4] = "done"
for i in range(5):
    print(State[i],end=" ")