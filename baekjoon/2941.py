croatian=["c=","c-","dz=","d-","lj","nj","s=","z="]
data=input()
num=0
for i in croatian:
    num+=data.count(i)
    data=data.replace(i,",")
data=data.replace(",","")
num+=len(data)
print(data)
print(num)