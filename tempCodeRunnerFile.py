def acquire_attribute(stringe):
    attribute_list = []
    important_point = stringe[0]
    start_append = False
    tag_count = 0
    currentWord = ''
    for i in range(len(stringe)):
        print(currentWord)
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
    return attribute_list