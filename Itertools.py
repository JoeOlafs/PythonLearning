# Itertools: product, permutations, combinations, accumulate,groupby, and infinite iterators
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b, repeat = 2)
print(list(prod))

from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a)
acc2 = accumulate(a, func = operator.mul)
print(a)
a = [1,2,6,3,4,5]
acc3 = accumulate(a, func = max)
print(list(acc))
print(list(acc2))
print(list(acc3))

from itertools import groupby
def smaller_than_3(x):
     return x<3

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
          {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

a = [1,2,3,4]
group_obj = groupby(a,key=lambda x: x<3) #can also be the function defined above
for key, value in group_obj:
     print(key,list(value))

group_obj2 = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj2:
     print(key,list(value))

from itertools import count, cycle, repeat
a = [1,2,3]
for i in count(10):
     print(i)
     if i==15:
          break

#for i in cycle(a):
#     print(i)
#funciton cycles through the list 'a'

for i in repeat(a, 4):
     print(i)

