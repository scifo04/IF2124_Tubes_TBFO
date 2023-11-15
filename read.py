from objects import Rules
import data

def shrink_list(liste):
    i = 0
    while (liste[i] != ''):
        i += 1
    blanks = i
    liste = liste[:blanks]
    return liste

def display_list_rules(liste):
    print("[",end="")
    for i in range(len(liste)):
        liste[i].displayRules()
        if (i != len(liste)-1):
            print(", ",end="")
    print("]")

def convert_to_slash(string):
    newstring = ''
    for i in range (len(string)):
        if (i == 1):
            newstring = newstring + '/'
            newstring = newstring + string[i]
        else:
            newstring = newstring + string[i]
    return newstring

def contain_slash(string):
    check = False
    for i in range (len(string)):
        if (string[i] == '/'):
            check = True
            return check
    return check

def txt_read(file):
    txt = open(file,'r')
    reader = txt.read()
    local = [[('') for j in range(100)] for i in range(7)]
    rules_mapper = [('') for i in range(5)]
    part = 0
    loc = 0
    map = 0

    for i in reader:
        if (i != ' ' and i != '\n'):
            if (part != 6):
                local[part][loc] = local[part][loc] + i
            else:
                rules_mapper[map] = rules_mapper[map] + i
        elif (i == ' '):
            if (part != 6):
                loc += 1
            else:
                map += 1
        elif (i == '\n'):
            if (part != 6):
                part += 1
                loc = 0
            else:
                rules = Rules(rules_mapper[0],rules_mapper[1],rules_mapper[2],rules_mapper[3],rules_mapper[4])
                local[6][loc] = rules
                rules_mapper = [('') for i in range(5)]
                map = 0
                loc += 1
    rules = Rules(rules_mapper[0],rules_mapper[1],rules_mapper[2],rules_mapper[3],rules_mapper[4])
    local[6][loc] = rules
    rules_mapper = [('') for i in range(5)]
    map = 0
    loc += 1

    data.states = local[0]
    data.inputs = local[1]
    data.stacks = local[2]
    data.start_state = local[3][0]
    data.start_stack = local[4][0]
    data.final_state = local[5][0]
    data.pda_rules = local[6]

    data.states = shrink_list(data.states)
    data.inputs = shrink_list(data.inputs)
    data.stacks = shrink_list(data.stacks)
    data.pda_rules = shrink_list(data.pda_rules)

def html_read(file):
    html = open(file,'r')
    reader = html.read()
    text = ''
    local_html = []
    for i in reader:
        if (i == '<'):
            text = text + i
            data.check_Konso = True
        elif (i == '>'):
            text = text + i
            data.check_Konso = False
            local_html.append(text)
            text = ''
        elif (data.check_Konso):
            text = text+i
    data.html_tags = local_html