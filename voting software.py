from cryptography.fernet import Fernet
import tkinter as tk

#init main window
tk=tk.Tk()
tk.geometry("800x600")
tk.title('VOTING SOFTWARE')

candidate_list=[]

# write encryption key
def write_key():
    file=open('/home/user/Documents/python/voting software/voting software assets/password.key','ab')
    key = Fernet.generate_key()
    file.write(key)
    file.close()

#read encryption key
def read_key():
    file=open('/home/user/Documents/python/voting software/voting software assets/password.key','rb')
    key=file.read()
    return key
    file.close()

write_key()

key=read_key()
fer=Fernet(key)


#adding candidate
def addcandidate(name):
    
    with open('/home/user/Documents/python/voting software/voting software assets/candidates list.txt','a') as i:
        i.write(name + '\n')


#viewing candidate
def viewcandidate():
    
    with open('/home/user/Documents/python/voting software/voting software assets/candidates list.txt','r')as i:
        for lines in i.readlines():
            data=lines.rstrip()
            print(data)

#check for unique rollno.
def checkduplicate():
    
    voter_rollnumber=str(input("enter  voter's roll number:"))
    with open('/home/user/Documents/python/voting software/voting software assets/voter roll no.txt','a')as i:
        i.write(voter_rollnumber + '\n')
    with open('/home/niranjan/Documents/python/voting software/voting software assets/voter roll no.txt','r')as j:    
        for lines in j.readlines():
            data=lines.rstrip()
            
           
            if voter_rollnumber==data:
                print('you have already voted')
                return False
           
            else:
                return True


#get voter rollno and add vote and encrypt the vote
def vote(voter_rollnumber):
    while (checkduplicate()==True):
        candidate=input('enter the name of the candidate you want to vote for:')
        with open('/home/user/Documents/python/voting software/voting software assets/casted vote.txt','a')as i:
            encrypted_candidate=fer.encrypt(candidate.encode()).decode()
            i.write(voter_rollnumber + '|' + encrypted_candidate + '\n')


# decrypt no. of votes and count the votes
def countvotes():
    with open('/home/user/Documents/python/voting software/voting software assets/casted vote.txt','r')as i:
        for lines in i.readlines():
            data=lines.rstrip()
            voter_rollno,candidate=data.split('|')
            decrypted_candidate=fer.decrypt(candidate.encode()).decode()
            candidate_list.append(decrypted_candidate)
            
    
    for candidate in candidate_list :
        print("election results are as follows:")
        print(candidate + ':' + str(candidate_list.count(candidate)))


#main program
while (True):
    
    print('1.add candidate')
    print('2.view candidate')
    print('3.vote')
    print('4.count votes')
    print('5.exit')
    
    choice=int(input('enter your choice:'))
    
    if (choice==1):
        name=input('enter the name of the candidate:')
        addcandidate(name)
    
    elif (choice==2):
        viewcandidate()
    
    elif (choice==3):
        if (checkduplicate()==True):
            vote(voter_rollnumber) 
    elif (choice==4):
        countvotes()
    
    elif choice==5:
        break
    
    else:
        print('invalid choice')
        continue

tk.loop()
    
    
    


