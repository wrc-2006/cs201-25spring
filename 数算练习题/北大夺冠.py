m=int(input())
dic={}
for _ in range(m):
    team,q,res=[i for i in input().split(',')]
    if team not in dic:
        if res=='yes':
            dic[team]=[1,1,q]  ##做对题目数，提交次数，正确题目
        else:
            dic[team]=[0,1,'']
    else:
        if res=='yes':
            if q in dic[team][2]:
                dic[team][1]+=1
            else:
                dic[team][0]+=1
                dic[team][1]+=1
                dic[team][2]+=q
        else:
            dic[team][1]+=1
key,value=list(dic.keys()),list(dic.values())
lst=[]
for i in range(len(key)):
    lst.append([value[i][0],value[i][1],key[i]])
lst.sort(key=lambda x:(-x[0],x[1],x[2]))
for i in range(min(12,len(key))):
    print(i+1,lst[i][2],lst[i][0],lst[i][1])