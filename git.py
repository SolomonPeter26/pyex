import os

     
def git(op):
    #os.getcwd()
    #print s
#    print os.listdir(os.getcwd())

            #change directory
    s = os.chdir((raw_input("Enter Folder:")))
#    os.getcwd()
    print "\n\n"
    print os.listdir(os.getcwd())



    
#    c = str("cd " + str(s))
#    os.system(c)
#    os.system("ls -a")

            # only INITIALISE GIT IN FOLDER
    os.system("git init")

    
            #add files for commit
    os.system("git add .")
    stri="git commit -m \" " + (raw_input("Enter message for commit:")) + "\""
    
            #view log of commits
    print "\t\tLocal ->"
    os.system("git log")
    os.system(stri)   
    
            #view status of repository
    print "\t\tStatus ->"
    os.system("git status")
    
            #view files which have been commited
    print "\t\tCommited Files ->"
#    os.system("git ls-files")
    
    
#    print "\t\tRemote ->"
    os.system("git remote")
    
        
    os.system("git remote add orig git@github.com:SolomonPeter26/pyex.git")
    os.system("git push orig master")


if __name__ == "__main__" :
    git(1)
