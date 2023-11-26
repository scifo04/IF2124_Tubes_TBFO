from objects import Rules
import data

def shrink_list(liste):
    i = 0
    if (liste[len(liste)-1] == ''):
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

def attribute_check(a,b):
    check = False
    if (not a in b):
        if (a[:-1] in b) and (a[(len(a)-2):] == '""'):
            for i in range(len(b)-len(a[:-1])):
                if (a[:-1] == b[i:i+len(a)-1]):
                    d = i+len(a)-1
                    for j in range(d,len(b)):
                        if (b[j] == '"'):
                            check = True
                            return check
    else:
        check = True
        return check
    return check

def txt_read(file):
    txt = open(file,'r')
    reader = txt.read()
    local = [[('') for j in range(2000)] for i in range(14)]
    rules_mapper = [('') for i in range(5)]
    row_att = 0
    col_att = 0
    part = 0
    loc = 0
    map = 0
    allowappend = True
    allowdefine = True
    allowcount = False

    for i in reader:
        if (part != 14):
            if (i == '~'):
                part = 14
                loc = 0
                allowappend = False
            if (allowappend):
                if (i != ' ' and i != '\n'):
                    if (part != 13):
                        local[part][loc] = local[part][loc] + i
                    else:
                        rules_mapper[map] = rules_mapper[map] + i
                elif (i == ' '):
                    if (part != 13):
                        loc += 1
                    else:
                        map += 1
                elif (i == '\n'):
                    if (part != 13):
                        part += 1
                        loc = 0
                    else:
                        rules = Rules(rules_mapper[0],rules_mapper[1],rules_mapper[2],rules_mapper[3],rules_mapper[4])
                        local[13][loc] = rules
                        rules_mapper = [('') for i in range(5)]
                        map = 0
                        loc += 1
        else:
            if (allowdefine):
                attributes = [[('') for j in range(8)] for i in range(len(shrink_list(local[1])))]
                allowdefine = False
            if (i == '('):
                allowappend = True
            elif (i == ')'):
                col_att += 1
                allowappend = False
            elif (i == '\n'):
                if (not allowcount):
                    allowcount = True
                else:
                    row_att += 1
                    col_att = 0
            elif (allowappend):
                attributes[row_att][col_att] = attributes[row_att][col_att] + i
    # rules = Rules(rules_mapper[0],rules_mapper[1],rules_mapper[2],rules_mapper[3],rules_mapper[4])
    # local[12][loc] = rules
    # rules_mapper = [('') for i in range(5)]
    # map = 0
    # loc += 1
    data.states = local[0]
    data.inputs = local[1]
    data.stacks = local[2]
    data.start_state = local[3][0]
    data.start_stack = local[4][0]
    data.final_state = local[5][0]
    data.epsilon = local[6][0]
    data.any = local[7][0]
    data.comment = local[8][0]
    data.allowtext = local[9]
    data.differentiator = local[10][0]
    data.compulsorier = local[12]
    data.contente = local[11][0]
    data.pda_rules = local[13]

    #print(data.contente)
    data.states = shrink_list(data.states)
    data.inputs = shrink_list(data.inputs)
    data.stacks = shrink_list(data.stacks)
    data.allowtext = shrink_list(data.allowtext)
    data.pda_rules = shrink_list(data.pda_rules)
    data.compulsorier = shrink_list(data.compulsorier)
    data.attribute_row = len(data.inputs)

    # print(data.attribute_col,data.attribute_row)
    # print(data.attribute_rules)
    # print(data.allowtext)

def html_read(file):
    html = open(file,'r')
    reader = html.read()
    text = ''
    local_html = []
    append_content = False
    for i in reader:
        if (i == '<'):
            text = text + i
            data.check_Konso = True
            append_content = False
        elif i != "<" and i != ">" and data.check_Konso and not append_content:
            text = text + i
        elif (i == '>'):
            text = text + i
            data.check_Konso = False
            append_content = True
            local_html.append(text)
            text = ''
        elif (i != " " and i != "<" and i != ">" and append_content and not data.check_Konso):
            if (i != "\n"):
                local_html.append(data.contente)
                append_content = False
    data.html_tags = local_html
    for i in range(len(data.html_tags)):
        data.html_tags[i] = "[" + ((data.html_tags[i][1:][:-1])).upper() + "]"

def getContained_Rules(liste,current_state,inpute,top_stack):
    IDX_UNDEF = -1
    for i in range(len(liste)):
        if (liste[i].cur_state == current_state and liste[i].input_word == inpute and (liste[i].stack_take == top_stack or liste[i].stack_take == data.any)):
            return liste[i]
        elif (liste[i].cur_state == current_state and liste[i].input_word == inpute and (top_stack in liste[i].stack_take)):
            return liste[i]
    return IDX_UNDEF

def isContained_Slash(stringe):
    check = False
    for i in range(len(stringe)):
        if (stringe[i] == '/'):
            check = True
            return check
    return check

def isExists(liste,stringe):
    check = False
    for i in range(len(liste)):
        if (liste[i] == stringe):
            check = True
            return check
    return check

def isSubStringList(liste,stringe):
    check = False
    for i in range(len(liste)):
        if attribute_check(liste[i],stringe):
            check = True
            return check
    return check

def getElmt(liste,stringe):
    IDX_UNDEF = -1
    for i in range(len(liste)):
        if (liste[i] == stringe):
            return i
    return IDX_UNDEF

def shortenInput(stringe):
    attribute_list = acquire_attribute(stringe)
    checkpoint = stringe[0]
    newstring = ''
    for i in range(1,len(stringe)):
        if (stringe[i] == ' ' and checkpoint == stringe[0]):
            return -1
        elif (stringe[i] == ' ' and checkpoint != stringe[0]):
            a = i
            for j in range (a):
                newstring = newstring + stringe[j]
            break
        else:
            checkpoint = stringe[i]
    if len(attribute_list) > 0:
        for i in range(len(attribute_list)):
            if (attribute_list[i] != ''):
                newstring = newstring + "_" + attribute_list[i]
        newstring = newstring + "]"
        return newstring
    else:
        return stringe

def acquire_attribute(stringe):
    attribute_list = []
    important_point = stringe[0]
    start_append = False
    tag_count = 0
    currentWord = ''
    for i in range(len(stringe)):
        if stringe[i] == ' ':
            important_point = stringe[i]
        elif stringe[i] != ' ' and start_append == False and important_point != stringe[0]:
            currentWord = currentWord + stringe[i]
            start_append = True
        elif stringe[i] != '"' and start_append:
            currentWord = currentWord + stringe[i]
        elif stringe[i] == '"' and start_append:
            currentWord = currentWord + stringe[i]
            tag_count += 1
            if (tag_count == 2):
                if (stringe[i+1] == ' ' or stringe[i+1] == stringe[len(stringe)-1]):
                    start_append = False
                    attribute_list.append(currentWord)
                    currentWord = ''
                    tag_count = 0
                else:
                    return "REJECTED"
    for i in range(len(attribute_list)):
        for j in range(len(attribute_list[i])):
            if attribute_list[i][j] == '=' and not isSubStringList(data.compulsorier,attribute_list[i]):
                attribute_list[i] = attribute_list[i][:j]
                break
            elif isSubStringList(data.compulsorier,attribute_list[i]):
                attribute_list[i] = attribute_list[i]
                break
    for i in range(len(attribute_list)):
        for j in range(i):
            if attribute_list[i] < attribute_list[j]:
                temp = attribute_list[i]
                attribute_list[i] = attribute_list[j]
                attribute_list[j] = temp
    for i in range(len(attribute_list)):
        for j in range(i):
            if attribute_list[i] == attribute_list[j]:
                attribute_list[j] = ''
    return attribute_list

def containsChar(stringe,chare):
    return chare in stringe

def removeCompulsorier(liste):
    for i in range(len(liste)):
        if data.compulsorier in liste[i]:
            liste[i] = liste[i][:-len(data.compulsorier)]
    return liste