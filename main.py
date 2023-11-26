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
# print(data.html_tags)
check = False

# CHECK IF STATE IS VALID WITH THE RULES
for i in range(len(data.pda_rules)):
    if not (read.isExists(data.states,data.pda_rules[i].cur_state)):
        print(data.states[i])
        print(data.pda_rules[i].cur_state)
        print("NON EXISTENT STATE DETECTED: REJECTED")
        quit()

# CHECK IF THE ATTRIBUTES CONTAINS COMPULSORY OBJECT
# for i in range(len(data.html_tags)):
#     if (not read.containsChar(data.html_tags[i],data.differentiator)):
#         counter = read.getElmt(data.inputs,read.shortenInput(data.html_tags[i]))
#         for j in range (len(data.attribute_rules[counter])):
#             if data.compulsorier in data.attribute_rules[counter][j]:
#                 for k in range(len(read.acquire_attribute(data.html_tags[i]))):
#                     # print(read.acquire_attribute(data.html_tags[i])[k],data.attribute_rules[counter][j][:-len(data.compulsorier)])
#                     if read.attribute_check(data.attribute_rules[counter][j][:-len(data.compulsorier)],read.acquire_attribute(data.html_tags[i])[k]):
#                         print("",end='')
#                         break
#                     else:
#                         print("COMPULSORY REJECTED")
#                         quit()

# CHECK IF THE WRITTEN ATTRIBUTES EXISTS
# for i in range(len(data.html_tags)):
#     if (not read.containsChar(data.html_tags[i],data.differentiator)):
#         counter = read.getElmt(data.inputs,read.shortenInput(data.html_tags[i]))
#         # print(read.shortenInput(data.html_tags[i]),counter,read.removeCompulsorier(read.shrink_list(data.attribute_rules[counter])),read.acquire_attribute(data.html_tags[i]))
#         current_checker = read.removeCompulsorier(read.shrink_list(data.attribute_rules[counter]))
#         current_target = read.acquire_attribute(data.html_tags[i])
#         if (len(current_target) != 0):
#             for j in range (len(current_target)):
#                 for k in range (len(current_checker)):
#                     if (read.attribute_check(current_checker[k],current_target[j])):
#                         # print("SUCCESS")
#                         check = True
#                 if (check):
#                     # print("SUCCESSSSSSSSSSS")
#                     check = False
#                 else:
#                     print("REJECTED")
#                     quit()
#         else:
#             print(end='')
            # print("SUCCESS")
        # if (check):
        #     print("SUCCESSSSSS")
        #     check = False
        # else:
        #     print("REJECTED")

# CHANGE COMMENTS TO ITS COMMENT VERSION
comment_counter = 0
for i in range(len(data.html_tags)):
    # print(data.comment,data.html_tags[i][:2]+data.html_tags[i][-1:])
    if data.comment == data.html_tags[i][:2]+data.html_tags[i][-1:]:
        data.html_tags[i] = data.comment
        comment_counter += 1
for i in range(comment_counter):
    data.html_tags.remove(data.comment)

# CHANGE ALL TAGS TO VALIDATED INPUT VERSION
for i in range(len(data.html_tags)):
    data.html_tags[i] = read.shortenInput(data.html_tags[i])

# print(data.html_tags)

# CHECK IF THE TEXT IS IN THE RIGHT PLACE
# html = open(html_file,'r')
# reader = html.read()
# if (len(reader) != 0):
#     current_box = ""
#     appender = ""
#     append_for_box = False
#     append_for_content = True
#     for i in reader:
#         # print(i)
#         if (i != ' ' and i != '<' and i != '>' and append_for_content):
#             if (read.isExists(data.allowtext,read.shortenInput(current_box))):
#                 print(end="")
#             else:
#                 if (i != ' ' and i != '\n'):
#                     print("REJECTED")
#                     quit()
#         elif (i != '<' and i != '>' and append_for_box):
#             appender = appender + i
#         elif (i == '<' and append_for_content):
#             append_for_content = False
#             append_for_box = True
#             appender = appender + i
#         elif (i == '>' and append_for_box):
#             appender = appender + i
#             current_box = '[' + appender[1:][:-1].upper() + ']'
#             appender = ""
#             append_for_content = True
#             append_for_box = False

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
        S_State.displayStack()
        read.txt_read(txt_file)
        rules = read.getContained_Rules(data.pda_rules,current_state,data.html_tags[iterator],current_top)
        rules_eps = read.getContained_Rules(data.pda_rules,current_state,data.epsilon,data.html_tags[iterator])
        if (len(S_State.compon) > 1):
            rules_eps2 = read.getContained_Rules(data.pda_rules,current_state,data.epsilon,data.html_tags[iterator]+S_State.compon[len(S_State.compon)-2])
            
        else:
            rules_eps2 = read.getContained_Rules(data.pda_rules,current_state,data.epsilon,data.html_tags[iterator])
        stringe = ""
        if (rules != -1):
            # rules.displayRules()
            # print("\n")
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
            if (rules_eps2 == -1):
                # rules_eps.displayRules()
                # print("\n")
                if (data.html_tags[iterator] == current_top and current_top == rules_eps.stack_take):
                    S_State.pop()
                    if (rules_eps.stack_store != data.epsilon):
                        S_State.push(rules_eps.stack_store)
                        current_top = S_State.infoTop()
                    else:
                        current_top = S_State.infoTop()
                    current_state = rules_eps.next_state
                    iterator += 1
                elif (data.html_tags[iterator] == current_top and current_top in rules_eps.stack_take):
                    S_State.pop()
                    current_top = S_State.infoTop()
                    current_state = rules_eps.next_state
                    iterator += 1
                else:
                    print("THIS REJECTED")
                    break
            else:
                # rules_eps2.displayRules()
                # print("\n")
                S_State.pop()
                S_State.pop()
                S_State.push(rules_eps2.stack_store)
                current_top = S_State.infoTop()
                current_state = rules_eps2.next_state
                iterator += 1
        else:
            print("REJECTED")
            break
        if (current_state == data.final_state):
            print("ACCEPTED")
            break