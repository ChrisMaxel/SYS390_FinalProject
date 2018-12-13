from os import listdir
from os.path import isfile, join

def getNames():
    mypath = "X:\Linux\SYS390\SYS390_FinalProject\imagesForSRS\Wireframes\Wireframes\ContactUs"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # print(onlyfiles)
    
    for i in range(0,len(onlyfiles),1):
        md = "![Figure ["
        md += onlyfiles[i][:-4]
        md += "]: "
        md += onlyfiles[i][:-4]
        md += "](https://raw.githubusercontent.com/ChrisMaxel/SYS390_FinalProject/master/imagesForSRS/"
        md += "AccountManagment/"
        md += onlyfiles[i]
        print (md,"\n")
        
def main():
    getNames()
    



main()
