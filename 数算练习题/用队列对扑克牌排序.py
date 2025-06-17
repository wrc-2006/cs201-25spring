from collections import defaultdict
n=int(input())
cards=[x for x in input().split()]
letters=['A','B','C','D']
queue_num=defaultdict(list)
queue_letter=defaultdict(list)
for i in cards:
    queue_num[i[1]].append(i)
    queue_letter[i[0]].append(i)
dic_letter={'A':1,'B':2,'C':3,'D':4}
cards.sort(key=lambda x:(dic_letter[x[0]],x[1]))
for i in range(1,10):
    print(f'Queue{i}:',end='')
    #queue_num[str(i)].sort()
    print(*queue_num[str(i)])    ###str()
for i in letters:
    print(f'Queue{i}:',end='')
    queue_letter[i].sort()
    print(*queue_letter[i])
print(*cards)