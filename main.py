import argparse
import os.path
from objects import Stack
from objects import Rules
import data
import read

# PARSING FILES
parser = argparse.ArgumentParser()
parser.add_argument("txt_file",type=str)
parser.add_argument("html_file",type=str)
args = parser.parse_args()
txt_file = args.txt_file
html_file = args.html_file

if (os.path.exists(txt_file) and os.path.exists(html_file)):
    print("PDA and html exists. Please wait until the compilation finish!")
elif (not os.path.exists(txt_file) and not os.path.exists(html_file)):
    print("error: html_file and txt_file does not exist")
    quit()
elif (os.path.exists(txt_file) and not os.path.exists(html_file)):
    print("error: html_file does not exist")
    quit()
elif (not os.path.exists(txt_file) and os.path.exists(html_file)):
    print("error: txt_file does not exist")
    quit()

read.txt_read(txt_file)
read.html_read(html_file)

S_State = Stack()
S_State.push('Z')
iterator = 0

# print(data.states)
# print(data.stacks)
# print(data.inputs)
# print(data.start_state)
# print(data.start_stack)
# print(data.final_state)
# print(data.epsilon)

current_state = data.start_state
current_top = data.start_stack

# print(current_state)
# print(current_top)
print(data.html_tags)

while (True):
    if (len(data.html_tags) == 0 and data.check_Konso == False):
        print("ACCEPTED")
        break
    elif (len(data.html_tags) == 0 and data.check_Konso == True):
        print("REJECTED")
        break
    else:
        print(current_state)
        print(data.html_tags[iterator])
        print(current_top)
        print()
        S_State.displayStack()
        rules = read.getContained_Rules(data.pda_rules,current_state,data.html_tags[iterator],current_top)
        rules_eps = read.getContained_Rules(data.pda_rules,current_state,data.epsilon,data.html_tags[iterator])
        stringe = ""
        if (rules != -1):
            rules.displayRules()
            print()
            if (rules.stack_take) in (rules.stack_store):
                rules.stack_store = rules.stack_store[:-len(rules.stack_take)]
            if (len(rules.stack_store) > 0):
                S_State.push(rules.stack_store)
                current_top = S_State.infoTop()
                current_state = rules.next_state
            else:
                current_state = rules.next_state
            iterator += 1
        elif (rules_eps != -1):
            rules_eps.displayRules()
            print()
            if (data.html_tags[iterator] == current_top):
                S_State.pop()
                if (rules_eps.stack_store != data.epsilon):
                    S_State.push(rules_eps.stack_store)
                    current_top = S_State.infoTop()
                else:
                    current_top = S_State.infoTop()
                current_state = rules_eps.next_state
                iterator += 1
            else:
                print("REJECTED")
                break
        else:
            print("REJECTED")
            break
        if (current_state == data.final_state):
            print("ACCEPTED")
            break