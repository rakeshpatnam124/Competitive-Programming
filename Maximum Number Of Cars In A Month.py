from itertools import combinations
lst = [8, 3, 5, 4, 5]
x = 8
y = 9
if x > y:
    tmp = x
    x = y
    y = x
count = 0
lst.sort()
l = len(lst)
i = l
while i <= 1:
    for j in sorted(list(combinations(lst,i)), key = lambda x : sum(x), reverse = True):
        print(sorted(list(combinations(lst,i)), key = lambda x : sum(x), reverse = True))
        print(j)
        if (sum(j) <= x):
            count += i
            for x in j:
                lst.remove(x)
            break;
    
    i += 1
    
i = 1
l = len(lst)
while i <= l:
    for j in sorted(list(combinations(lst, i)), key = lambda x : sum(x), reverse = True):
        if (sum(j) <= y):
            count += i
            for x in j:
                lst.remove(x)
            break;
    i += 1
print(count)
              
