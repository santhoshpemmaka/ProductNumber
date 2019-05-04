"""
find product of the special conditions in the individual number
1. number atleast consists of the 1 or 0
2. number didn't start with the 0
3. product will allow once 
"""
"""
Example:-
Input:-
3
110
123
100
Output:
1353000
Input:-
3
111
222
100
Output:-
0
"""

num = int(input())
l1 = []
for i in range(num):
    l1.append(input())
l2 = []

for i in range(len(l1)):
    result = l1[i]
    found=0
    if result[0] != '0':
        for i in range(len(result)):
            if result[i] == '0' or result[i] == '1':
                found=1
    l2.append(found)
sum1=1
res=0
for i in range(len(l2)):
    if l2[i] == 1:
        sum1 = sum1*(int(l1[i]))
    else:
        res=1
        break;
if res == 0:
    print(sum1)
else:
    print(0)

