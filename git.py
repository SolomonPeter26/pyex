import os

def createrepo():
            #change directory
    folpath=""
    fold=raw_input("Enter repository name ");
    os.chdir("/home/solomon/SolomonPeter26/Private")
    folpath=" mkdir " + str(fold)
    os.system(folpath)
    chp="/home/solomon/SolomonPeter26/Private/" + fold
    os.chdir(chp)
    os.system(" touch README.md");
    print "\n\n"
    print os.listdir(os.getcwd())
    
def pushgithub():    #commits on local repo and pushes to remote repo
    fold=raw_input("Enter repository name ");
    uname=raw_input("Enter User name ");
    chp="/home/solomon/" + uname + "/Private/" + fold
    os.chdir(chp)
    print "\n\n"
    print os.listdir(os.getcwd())   #shifted to local repo
    os.system("git remote")
    bran=raw_input("Enter remote branch ");     #select which remote branch you want to go to
    commitlocal()                   #commits on local repo
    remotepush(bran,uname,fold)     #pushes to remote repo
    

     
def git(op):

            # only INITIALISE GIT IN FOLDER
    os.system(" git config --global user.name \"Solomon Peter\"")
    os.system(" git config --global user.email \"peterkingsley26@gmail.com\"")
    os.system(" git init")

    
def commitlocal():
            #add files for commit
    os.system(" git add .")
    stri=" git commit -m \" " + (raw_input("Enter message for commit:")) + "\""
    
            #view log of commits
    print "\t\tLocal ->"
    os.system(stri)
    os.system(" git log")
    
            #view status of repository
    print "\t\tStatus ->"
    os.system(" git status")
    
            #view files which have been commited
    print "\t\tCommited Files ->"
    os.system(" git ls-files")
    
def remotel():    
    print "\t\tRemote ->"
    os.system(" git remote")



    crn="curl -F 'login=SolomonPeter26' -F 'token=a4d1fb125214f2a1ded31145ae77b068' https://github.com/api/v2/json/repos/create -F 'name=" + fold + "' -F 'description=" + raw_input("Enter description for project: ") + "\'"
    print crn
    os.system(crn)

#function to push on github  
def remotepush(bran,uname,fold):
#    strr=" git remote add " + brname + " git@github.com:" + uname + "/" + fold + ".git"
#    print strr
#    os.system(strr)
    strr2="git push " + bran + " master"
    print strr2
    os.system(strr2)
    

if __name__ == "__main__" :
    pushgithub()
