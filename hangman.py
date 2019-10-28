import math

import random


def schan(s, i, a):
    l = len(s)
    t = ""
    if i == 0:
        t = t + a
        t = t + s[1:]
    elif i == (l - 1):
        t = t + s[:i]
        t = t + a
    else:
        t = t + s[:i]
        t = t + a
        t = t + s[i + 1:]
    return t



q = ("apple", "banana", "capsule", "destiny","association","enviroment","malayalam","Goodness")
# print("*")
# n=input()
# l=len(n)
# s=""
# print(n)
# for i in range(l):
#     s=s+str((chr(ord(n[i])+1)))
# print(s)



# print("\n" + str(q[x]))

def star():
    print("\n"+" * "*15)
def stars():
    print(""+"*"*45)
# print(schan(n,0,"s"))
# print(schan(n,l-1,"s"))
# print(schan(n,2,"s"))
x = random.randint(0, len(q))
answer = (str(q[x]).strip()).upper()
q=answer
l = len(answer)
que = ("$" * l).strip()
i = 5
f = 0
p=""
o=""
c=0
stars()
stars()
print("\n\t\t\t^^^Hang_Man^^^\n")
stars()
stars()
print("\n")
star()
print("\n\t\tYour Word is  :" + str(que))
star()
while (i != 0):
    print("\n\t\tEnter Your Letter : ",end=" ")
    t = input().strip()

    p=t.upper()
    if(p==""):
        print("\n\t\tEnter Something in it Bro..")
        print("\n\t\tYour Word : " + str(que) + " \n")
        print("\n\t\t!! Chances Remaing: "+str(i)+" !!")
        star()
        continue
    elif(o.find(p)==-1):
        o=o+p
    else:
        print("\n\t\tYou Have Guess "+str(p)+" Before")
        print("\n\t\tYour Word : " + str(que) + " \n")
        print("\n\t!! Chances Remaing: "+str(i)+" !!")
        star()
        continue
    if (answer.find(p) != -1):
        c = answer.count(p)
        print("\n\t\t++ Correct ++\n")
        for j in range(c):
            e = answer.index(p)
            que = schan(que, e, p)
            answer = schan(answer, e, "_")
            c=answer.count("_")
            # print("\t"+str(p)+" at "+str(e)+" and length "+str(l))

    else:
        i -= 1
        print("\n\t\tXX Wrong XX\n")
        if(i==0):
            break;
        print("\n\t\t!! Chances Remaing: "+str(i)+" !!")
    if (c == l):
        f = 1
        break
    star()
    print("\n\t\tYour Word : " + str(que) + " \n")
    print("\t\tRemaining Letters : " + str(l-c))
    star()
    # print("Answer :" + str(answer) + "\n")

if (f == 1):
    star()
    print("\t\tWord Was : " + str(q))
    print("\n\t\tYou Have Won!!")

    star()
else:
    star()
    print("\t\tWord Was : " + str(q))
    print("\n\t\tYou Lose Buddy :[")
    star()
