
import random
def word():
    f=open("list.txt","r")
    a=[]
    p=f.readline().strip("\n")
    while(p!=""):
        a.append(p)
        p=f.readline().strip("\n")
    print(a)
    l=len(a)
    print(l)
    x=random.randint(0,l-1)
    print(a[x])
    return(a[x])
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
def star():
    print("\n"+" * "*15)
def stars():
    print("\n"+"*"*30)
def won(d):
    print("\t\tWord Was : " + str(d))
    print("\n\tYou Have Won!!")
    star()
def lose(d):
    star()
    print("\t\tWord Was : " + str(d))
    print("\n\tYou Lose Buddy :[")
    star()
def logo():
    stars()
    stars()
    print("\n\t...HangMan...")
    stars()
    stars()
    print("\n")
def remain(p,que,answer,c):
    for j in range(c):
        e = answer.index(p)
        que = schan(que, e, p)
        answer = schan(answer, e, "_")
        c = answer.count("_")
    return (p,que,answer,c)
