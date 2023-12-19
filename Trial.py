# dit={"year":[2021,2022,2023,2024]}
# d={"data":[]}
# # for i in dit['year']:
# #     d['data'].append(i)
# # print(d)
# d = {"data": [va for va in dit['year']]}
# print(d)

# # ([d["data"].append(va)] for va in dit['year'])
# # print(d)
from datetime import datetime
import numpy as np

x=datetime.now()
d={"data":[]}
l=[]
for i in range(10000000):
    l.append(i)
    d['data'].append(len(l))


print(sum(l),len(l))

y=datetime.now()
print("list",y-x)

x1=datetime.now()
s,c=0,0
for i in range(10000000):
    s+=i
    c+=1
print(s,c)

y1=datetime.now()
print("iteration",y1-x1)


x2 = datetime.now()

# Using NumPy vectorized operations to create the array
x = np.arange(1,10000000)
d = {"data": []}
d["data"].append(len(x))
print(np.sum(x), len(x))
y2 = datetime.now()
print("array", y2 - x2)

# x2=datetime.now()
# d={"data":[]}
# x=np.array([])
# for i in range(10000000):
#     x=np.append(x,i)
#     d['data'].append(len(x))
# print(np.sum(x),len(x))
# y2=datetime.now()
# print("array",y2-x2)


 