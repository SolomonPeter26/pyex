import os, glob
import fileinput
import re
num=0;
def scandirs(path):
        global num;
        for currentFile in glob.glob( os.path.join(path, '*') ):
            if os.path.isdir(currentFile):
                print '\tgot a directory: ' + currentFile  + "\n"
                scandirs(currentFile)
            print "processing file: " + currentFile
            n=0;
            if re.search("c\Z",currentFile) or  re.search("cpp\Z",currentFile) or re.search("rb\Z",currentFile) or re.search("py\Z",currentFile) or re.search("txt\Z",currentFile):
                for line in fileinput.input(currentFile):
                    n+=1;
                    num+=1;
                print "\t No.of lines: " + currentFile +" has " + str(n) + "\n"


if __name__ == '__main__':
    global num;
    scandirs(raw_input("Enter the path: "))
    print "\n\nTotal Lines of code in folder is:" + str(num) + "\n"
