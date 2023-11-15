import argparse
import os.path
from objects import Stack
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

while (True):
    if (len(data.html_tags) == 0 and data.check_Konso == False):
        print("ACCEPTED")
        break
    elif (len(data.html_tags) == 0 and data.check_Konso == True):
        print("REJECTED")
        break
    else:
        if (not read.contain_slash(data.html_tags[iterator])):
            S_State.push(data.html_tags[iterator])