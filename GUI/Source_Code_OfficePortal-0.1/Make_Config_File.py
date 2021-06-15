def clearConfigfile():
    f = open('office_portal.txt', "w+")
    f.truncate(0)
    f.close()
def makeConfig(newLine):
    f = open('office_portal.txt', "a")
    f.writelines([str(newLine) + '\n'])
    f.close()
