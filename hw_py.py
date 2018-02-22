
# coding: utf-8

# In[1]:


a=input()
b=input()
c=input()

if a=='' or b=='' or c=='' or int(a)<=0 or int(b)<=0 or int(c)<=0:
    print('Треугольник не существует')
else:
    a=int(a)
    b=int(b)
    c=int(c)
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**.5
    print(s)


# In[2]:


begin = int(input())
nums = []
divs = 0
for i in range(2, begin+1):
    for j in range(2, i):
        if i%j == 0:
            divs +=1
    if divs == 0:
        nums.append(i)
    else:
        divs = 0
        
print(nums)


# In[7]:


begin = int(input())
list = [i for i in range(begin+1) if i%5 == 0]
print(list)


# In[6]:


a=int(input())
b=int(input())
c=int(input())

D = b**2 - 4*a*c
if D>0:
    x1 = (-b-D**.5)/2*a
    x2 = (-b+D**.5)/2*a
    print(x1)
    print(x2)
elif D == 0:
    x1 = -b/(2*a)
    print(x1)
else:
    print('Нет корней у квадратного уравнения')


# In[4]:


import random
import numpy as np

names = ['Bob', 'John', 'Dan', 'Bill', 'Andrey', 'Phil', 'Scott', 'Jake', 'Misha', 'Sergey']
debts = [random.randint(50, 1001) for i in range(10)]

dictionary = dict(zip(names,debts))
mean = np.mean(list(dictionary.values()))
debt_sum = sum(list(dictionary.values()))
disp = np.var(list(dictionary.values()))
mini = min(list(dictionary.values()))
maxi = max(list(dictionary.values()))

for key, val in dictionary.items():
    if val == mini:
        min_key = key
    elif val == maxi:
        max_key = key

num = []        
diff = 1001        
for key, val in dictionary.items():
    diff_sub = abs(val - mean)
    if diff_sub<diff:
        diff = diff_sub
        num = []
        num.append(key)
    elif diff_sub == diff:
        num.append(key)
if len(num) == 1:
    num = num[0]
        
print('Средняя сумма долга {}'.format(mean))
print('Абсолютный долг {}'.format(debt_sum))
print('Дисперсия {}'.format(disp))
print('Имя с максимальным/минимальным долгом {}/{}'.format(max_key, min_key))
print('Имя человека с долгом, который ближе всего по значению к среднему: {}'.format(num))

