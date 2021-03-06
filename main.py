from typing import Final
import data as d
import art
import os
import random
from time import sleep
# The screen clear function


data=d.data #need to be shuffled every time game begin
random.shuffle(data)

class user:
    name=''
    questionCount=0
    score=0
    ch='Play'

def introDisplay(user):
    os.system('cls')
    print(art.logo)
    user.name=input('\nEnter Name: ')
    os.system('cls')
    
    # return name

def checkIfRight(user, ch):
    # c1=data[user.questionCount]['follower_count']
    # a="A"
    os.system('cls')
    
    a='A' if data[user.questionCount]['follower_count']>data[user.questionCount+1]['follower_count'] else 'B'
    if(ch.upper()==a.upper()):
        user.score+=1
        # inp=input("PressAnyKeyToContinue")
        return 1
    elif(ch.upper()=='exit'.upper()):
        return -1
    else:
        # inp=input("PressAnyKeyToContinue")
        return 0
    


def printNewQuestion(user):
    print(art.logo)
    print(user.name,' your score: ',user.score)
    print('\n\nWhich of the following has higer instagram followers?\n')
    print('"',data[user.questionCount]['name'],'"') 
    print(art.vs)
    print('"',data[user.questionCount+1]['name'],'"')
    user.questionCount+=2
    user.ch=input("\nChose : ")
    ans=checkIfRight(user,user.ch)
    if(ans==1):
        print('TRUE\n')
        inp=input("Press Any Key To Continue: ")
    elif(ans==-1):
        pass
    elif(ans==0):
        print("FALSE\n")
        inp=input("Press Any Key To Continue: ")

def displatFinalScore(user):
    os.system('cls')
    print("GAME OVER")
    print(user.name,", Your Final Score is: ", user.score)

user1=user
# user1.name=introDisplay()

def finalFuncCall(user):
    introDisplay(user)
    while(user.ch.upper()!='EXIT' and user.questionCount<48):
        printNewQuestion(user1)
    else:
        displatFinalScore(user)
        en=input("Start a New Game??(Y/N): ")
        if(en.upper()=='Y'):
            user.name=''
            user.score=0
            user.ch=''
            user.questionCount=0
            random.shuffle(data)
            introDisplay(user)
            finalFuncCall(user)
    



finalFuncCall(user)


