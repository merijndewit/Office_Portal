import sys,os

if getattr(sys, 'frozen', False):
    cd = os.path.dirname(sys.executable)
else:
    cd = os.path.dirname(os.path.abspath(__file__))

def clearConfigfile():
    f = open(cd + '/office_portal.txt', "w+")
    f.truncate(0)
    f.close()
def makeConfig(newLine):
    f = open(cd + '/office_portal.txt', "a")
    f.writelines([str(newLine) + '\n'])
    f.close()
