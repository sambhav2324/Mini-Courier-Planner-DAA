"""Algorithms used by the Mini-Courier Planner."""

def parcel_key(p):
    return (-int(p.get('priority', 0)), int(p.get('deadline', 999999)), str(p['id']))

def merge_sort(items, key=parcel_key):
    if len(items) <= 1: return list(items)
    mid=len(items)//2; left=merge_sort(items[:mid],key); right=merge_sort(items[mid:],key)
    out=[]; i=j=0
    while i<len(left) and j<len(right):
        if key(left[i]) <= key(right[j]): out.append(left[i]); i+=1
        else: out.append(right[j]); j+=1
    return out+left[i:]+right[j:]

def quick_sort(items, key=parcel_key):
    a=list(items)
    def sort(lo,hi):
        if lo>=hi:return
        mid=(lo+hi)//2; pivot_idx=sorted([(key(a[lo]),lo),(key(a[mid]),mid),(key(a[hi]),hi)])[1][1]
        a[pivot_idx],a[hi]=a[hi],a[pivot_idx]; pivot=key(a[hi]); i=lo
        for j in range(lo,hi):
            if key(a[j])<=pivot: a[i],a[j]=a[j],a[i]; i+=1
        a[i],a[hi]=a[hi],a[i]; sort(lo,i-1); sort(i+1,hi)
    sort(0,len(a)-1); return a

def knapsack(parcels, capacity):
    n=len(parcels); dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i,p in enumerate(parcels,1):
        w=int(p['weight']);v=int(p['value'])
        for c in range(capacity+1):
            dp[i][c]=dp[i-1][c]
            if w<=c: dp[i][c]=max(dp[i][c],dp[i-1][c-w]+v)
    selected=[]; c=capacity
    for i in range(n,0,-1):
        if dp[i][c]!=dp[i-1][c]: selected.append(parcels[i-1]);c-=int(parcels[i-1]['weight'])
    selected.reverse()
    return selected,sum(int(p['weight']) for p in selected),dp[n][capacity],dp

def dijkstra(graph, source):
    import heapq
    dist={v:float('inf') for v in graph}; prev={v:None for v in graph}
    if source not in graph: raise ValueError(f'Unknown source: {source}')
    dist[source]=0; heap=[(0,source)]
    while heap:
        d,u=heapq.heappop(heap)
        if d!=dist[u]:continue
        for v,w in graph[u].items():
            if w<0:raise ValueError('Dijkstra requires nonnegative weights')
            nd=d+w
            if nd<dist[v]:dist[v]=nd;prev[v]=u;heapq.heappush(heap,(nd,v))
    return dist,prev

def reconstruct_path(prev,target):
    path=[];node=target
    while node is not None:path.append(node);node=prev.get(node)
    return path[::-1]

def nearest_neighbor_tsp(start,destinations,distances):
    remaining=set(destinations);route=[start];current=start;total=0
    while remaining:
        nxt=min(remaining,key=lambda n:(distances[current][n],n));d=distances[current][nxt]
        if d==float('inf'):raise ValueError(f'No path to {nxt}')
        total+=d;route.append(nxt);remaining.remove(nxt);current=nxt
    back=distances[current][start]
    if back!=float('inf'):total+=back;route.append(start)
    return route,total
