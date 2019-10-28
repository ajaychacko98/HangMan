from file import *
#
# x = random.randint(0, 3)
# q = ("apple", "banana", "capsule", "destiny")
# print("*")
# n=input()
# l=len(n)
# s=""
# print(n)
# for i in range(l):
#     s=s+str((chr(ord(n[i])+1)))
# print(s)



# print("\n" + str(q[x]))


# print(schan(n,0,"s"))
# print(schan(n,l-1,"s"))
# print(schan(n,2,"s"))
# answer = str(q[x]).strip()
answer=word().upper()
q=answer.upper()
l = len(answer)
que = ("@" * l).strip()
i = 5
f = 0
c=0
logo()
star()
print("\tYour Word is  :" + str(que))
star()
while (i != 0):
    print("\n\tEnter Your Letter : ",end=" ")
    p = input().strip().upper()
    if (answer.find(p) != -1):
        c = answer.count(p)
        print("\n\t++ Correct ++\n")
        p,que,answer,c=remain(p, que, answer,c)
    else:
        i -= 1
        print("\n\tXX Wrong XX\n")
        print("\n\tChances Remaing: "+str(i))
    if (c == l):
        f = 1
        break
    star()
    print("\tYour Word : " + str(que) + "\n")
    print("\tRemaining Letters : " + str(l-c))
    star()
    # print("Answer :" + str(answer) + "\n")

if (f == 1):
    won(q)
else:
    lose(q)
