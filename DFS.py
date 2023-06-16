def DFS(a,b,tar):
    m={}
    isSolvable = False
    path = []
    s = []
    s.append([0,0])
    while(len(s)>0):
        u = s.pop()
        if((u[0],u[1]) in m):
            continue
        if(u[0]>a or u[1]>b or u[0]<0 or u[1]<0):
            continue
        path.append([u[0],u[1]])
        m[(u[0],u[1])] = 1
        if(u[0] == tar or u[1] == tar):
            isSolvable = True
            if(u[0] == tar):
                if(u[1]!=0):
                    path.append([u[0],0])
            else:
                if(u[0]!=0):
                    path.append([0,u[1]])
            for i in range(len(path)):
                print("(",path[i][0],",",path[i][1],")")
            break
        s.append([u[0],b])
        s.append([a,u[1]])
        for i in range(max(a,b)+1):
            c=u[0]+i
            d=u[1]-i
            if(c==a or d==0):
                s.append([c,d])
            c=u[0]-i
            d=u[1]+i
            if(c==0 or d==b):
                s.append([c,d])
        s.append([a,0])
        s.append([0,b])
    if(not isSolvable):
        print("No solution")
j1,j2,tar=4,3,2
DFS(j1,j2,tar)
