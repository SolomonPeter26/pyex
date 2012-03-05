import os

def git(op):
    s = os.walk('/home/solomon/pythonex')
    os.system("ls -a")
    os.system("git add .")
    
    stri="git commit -m "+ (raw_input("Enter message for commit:"))
    os.system(stri)
    print "\t\tLocal ->"
    os.system("git log")
    
    print "\t\tRemote ->"
    os.system("git remote")
#    os.system("git remote add origin git@github.com:SolomonPeter26/pythontask.git")
    os.system("git push origin master")


if __name__ == "__main__" :
    git(1)
