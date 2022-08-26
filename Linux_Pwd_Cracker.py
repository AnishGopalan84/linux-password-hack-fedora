import sys
import os 
import crypt
from termcolor import * 
def delfile():
    cmd1 = "rm -r shadw.txt"
    os.system(cmd1)

# PASSWORD CRACKING FROM LINUX SHADOW FILE 
# WORD LIST IS REQUIRED IN SAME FOLDER
def compHash(sha512,salt):
    print (sha512)
    f1 = open("PwdList.txt","r")
    for passtxt in f1.readlines():
        passtxt = passtxt.strip(" ")
        passtxt = passtxt.strip("\n")
        cryptPwd = crypt.crypt(passtxt,salt)            
        if (cryptPwd == sha512):
            return(passtxt)
            break
    return()


def extracthash(filename):
    word=[]
    f2 = open(filename,'r')
    for line in f2.readlines():        
        word.append(line.split(':'))
    #print (word)
    #EXTRACT THE PASSWORD HASH AND CHECK IN THE WORD LIST 
    #SALT VALUE OF FEDORA 32 IS 19 CHARCATER IN PWD HASH
    for i in word:
        if (len(i[1]) > 3):
            salt = i[1][:19]
            encPwd = compHash(i[1],salt)
            if (encPwd):
                print(colored("[+] Password Found For " + i[0] + "  and Password is  " + encPwd,'blue'))
            else:
                print(colored("[+] Password Not Found For " + i[0] ,'red'))
            
def main():
    #COPY THE CONTENTS OF SHADOW FILE
    cmd = "cat /etc/shadow > shadw.txt"
    os.system(cmd)
    if (True):
        filename = "shadw.txt"
       # print(filename)
        if not  os.path.isfile(filename):
            print(colored("[+] File Name Not Found in the Path",'red'))
            exit(0)
        print(colored("[+] File Found",'green'))
        extracthash(filename)
    #STEPS FOR TESTING PUPOSE NOT NECESSARY
    elif (len(sys.argv)==1):
        print(colored("[+] File Name  Required ",'red'))
        #delfile()        
    else:
        print(colored("[+] Too Many Parameters ",'red'))     
        #delfile()

if __name__ == main():
    main()
delfile()
