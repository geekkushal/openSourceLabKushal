# Q1
print(" By Kushal Ajwani , 22104038 , B - 15 , IT ")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

r = False

if(len(s1) > len(s2)):
    k = s1
    s1 = s2
    s2 = k
    r = True

i = 0
j = 0

n = len(s1)
m = len(s2)
common = ""

print(" s1 = ",s1,"   s2 = ",s2)
uncommonj = ""

while(i<n and j<m):
    if(s1[i]==s2[j]):
        common += s1[i]
       # print(" i = ",i," j = ",j," matched ! ")
        i+=1
        jlast = i
      #  print(" i = ",i)
    else:
        uncommonj += s2[j]
  #  print(" j = ",j)
    j+=1


if(len(common) == 0):
    print("No")
elif(r):
    print("Yes")
    print(" Common characters : ",common)
    print(" s2 remaining part => ",s1[i:])
    print(" s1 remaining part => ",uncommonj)
    
else:
    print("Yes")
    print(" Common characters : ",common)
    print(" s1 remaining part => ",s1[i:])
    print(" s2 remaining part => ",uncommonj)
