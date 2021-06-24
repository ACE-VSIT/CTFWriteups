import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def generateLine(content,link):
    content = content[3:]
    data = content.split(' ',1)
    line = "| Day " + data[0] + " | " + data[1][:-3] + " | [Click Here](" + link.replace(" ", "%20") + ")\n"
    return (line)

contents = [name for name in os.listdir(".") if not os.path.isdir(name)]
contents.remove("README.md")
contents.remove("GenerateReadme.py")
contents.sort(key=natural_keys)


contentList = ["## This folder includes all writeups for 25 days of cybersecurity at tryhackme\n", "\n", "| Day | Title | Link |\n", "| ----| ----  | ---- |\n"]

for content in contents:
    contentList.append(generateLine(content,content))

f = open("README.md","w")
f.writelines(contentList)

print("Wish fulfilled\n ~Prezi")