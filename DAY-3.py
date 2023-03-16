#list comperehension
'''print([i for i in range(11)])
print([i for i in range(11) if i%2 != 0])
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[j**2 if j%2!=0 else j**3  for j in i] for i in mat])'''

'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2 !=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)'''

#qn1
'''mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,2,2]
x=[]
for i in list_b:
    for j in range(0,len(mylist)):
        if(mylist[j]==i):
            x.append((i,j))
print(x)
print([(i,mylist.index(i))  for i in list_b])
print(dict((i,mylist.index(i))  for i in list_b))
result={ }
for i in list_b:
    result[i]=mylist.index(i)
print(result)
result={i:mylist.index(i) for i in list_b}
print(result)'''

#qn2
'''sentences=["a new world record was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on tuesday",
           "with over three lakh diya or earthen lamps",
           "lit up simultaneously on the banks of the sarayu river"]
stpwords=['for','a','of','the','was','and','to','in','on','with']
result=[]
for i in sentences:
    row_data=[]
    for word in i.split():
        if word not in stpwords:
            row_data.append(word)
    result.append(row_data)
print(result)'''

#qn3
'''l=[i for i in input().split(',')]
i5=l.index('5')
i8=l.index('8')
ans=sum([int(i) for i in l[:i5]+l[i8+1:]])+int("".join(l[i5:i8+1]))
print(ans)'''


'''num=3,2,6,5,1,4,8,9
x=[]
m=[]
sum=0
for i in range(len(num)):
       if num[i]==5 or num[i]==8:
           x.append(i) #x=[3,6]
for j in range(len(num)):
    if j<x[0]:
        sum+=num[j]
    elif j> x[1]:
        sum+=num[j]
print(sum)
#print(int("".join(num[x[0]:x[1]+1]))+sum)'''

#qn4
'''s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))'''

#qn5

'''def max_visited_speciality(patient_medical_speciality_list,medical_specialist):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality=medical_speciality['P']
    elif E>O:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'P',303,'P',302,'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"Ent"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)'''
