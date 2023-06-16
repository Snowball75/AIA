import random
def randomSol(tsp):
    cit=list(range(len(tsp)))
    sol = []
    for i in range(len(tsp)):
        randomcity = cit[random.randint(0,len(cit)-1)]
        sol.append(randomcity)
        cit.remove(randomcity)
    return sol
def routelength(tsp,sol):
    route_len = 0
    for i in range(len(sol)):
        route_len+=tsp[sol[i-1]][sol[i]]
    return route_len
def getneighbour(sol):
    neis = []
    for i in range(len(sol)):
        for j in range(i+1,len(sol)):
            nei=sol.copy()
            nei[i]=sol[j]
            nei[j]=sol[i]
            neis.append(nei)
    return neis
def getBestNeighbour(tsp,neis):
    bRouteLen = routelength(tsp,neis[0])
    bNei = neis[0]
    for nei in neis:
        curRoutelen = routelength(tsp,nei)
        if(curRoutelen<bRouteLen):
            bRouteLen = curRoutelen
            bNei = nei
    return bNei,bRouteLen
def hillClimbing(tsp):
    curSol=randomSol(tsp)
    curRouteLen = routelength(tsp,curSol)
    neis = getneighbour(curSol)
    bNei,bNeiRouteLen = getBestNeighbour(tsp,neis)
    while bNeiRouteLen < curRouteLen:
        corSol = bNei
        curRouteLen = bNeiRouteLen
        neis = getneighbour(curSol)
        bNei,bNeiRouteLen = getBestNeighbour(tsp,neis)
    return curSol,curRouteLen
tsp=[
    [0,400,500,300],
    [400,0,300,500],
    [500,300,0,400],
    [300,500,400,0]]
print(hillClimbing(tsp))
