import os
from datetime import datetime

Current_Date = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
if os.path.isfile(r'./src/main/bkit/astgen/ASTGeneration.py'):
    os.rename(r'./src/main/bkit/astgen/ASTGeneration.py',r'./src/main/bkit/astgen/ASTGeneration_' + str(Current_Date) + '.py')

filename = "./src/main/bkit/astgen/ASTGeneration.py"
fo = open(filename, "w")
fo.write("""# Generate automatically
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
""")

with open("./target/BKITParser.py") as fp: 
    Lines = fp.readlines()
    classBkit = False
    for line in Lines:
        index = line.find("class")
        if index != -1 and classBkit == True:
            comment = ""
            with open("./src/main/bkit/parser/BKIT.g4") as bkit:
                bkitlines = bkit.readlines()
                for cmt in bkitlines:
                    init = line[index + 6:-28][0].lower()+line[index + 6:-28][1:]
                    i = cmt.find(init + ":",0,len(init)+1)
                    if i != -1 and cmt[0] != '/':
                        comment = cmt

            fo.write("""    # """ + (comment if len(comment) > 0 else "\n") + """    def visit""" + line[index + 6:-28] + """(self, ctx:BKITParser.""" + line[index + 6:-21] + """):
        return None

""")
        elif index != -1 and classBkit == False:
            classBkit = True

fo.close()