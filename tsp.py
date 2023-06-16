answer=[]
def tsp(graph,v,curpos,n,count,cost):
    if(count==n and graph[curpos][0]):
        answer.append(cost+graph[curpos][0])
        return
    for i in range(n):
        if(v[i]==False and graph[curpos][i]):
            v[i]=True
            tsp(graph,v,i,n,count+1,cost+graph[curpos][i])
            v[i]=False
n=4
graph=[[0,10,15,20],
       [10,0,35,25],
       [15,35,0,30],
       [20,25,30,0]]
v=[False for i in range(n)]
v[0]=True
tsp(graph,v,0,n,1,0)
print(min(answer))