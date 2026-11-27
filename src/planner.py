import json,time,random,csv
from pathlib import Path
from algorithms import merge_sort,quick_sort,knapsack,dijkstra,reconstruct_path,nearest_neighbor_tsp

def load_dataset(path):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    if not all(k in data for k in ('depot','graph','parcels')):raise ValueError('Dataset needs depot, graph, parcels')
    graph={u:{v:float(w) for v,w in edges.items()} for u,edges in data['graph'].items()}
    for u,edges in graph.items():
        for v in edges:
            if v not in graph:raise ValueError(f'Graph references unknown node {v}')
    for p in data['parcels']:
        for f in ('id','destination','priority','deadline','weight','value'):
            if f not in p:raise ValueError(f'Parcel missing {f}')
        if p['destination'] not in graph:raise ValueError(f"Unknown destination {p['destination']}")
    return data,graph

def run_plan(data,graph,capacity):
    timings={};t=time.perf_counter();ordered=merge_sort(data['parcels']);timings['merge_sort']=time.perf_counter()-t
    t=time.perf_counter();quick=quick_sort(data['parcels']);timings['quick_sort']=time.perf_counter()-t
    assert [p['id'] for p in ordered]==[p['id'] for p in quick], 'Sorting algorithms produced different order'
    t=time.perf_counter();selected,weight,value,dp=knapsack(ordered,capacity);timings['knapsack']=time.perf_counter()-t
    depot=data['depot'];dest=sorted({p['destination'] for p in selected if p['destination']!=depot});nodes=[depot]+dest
    t=time.perf_counter();distances={};paths={}
    for s in nodes:
        d,prev=dijkstra(graph,s);distances[s]=d;paths[s]={n:reconstruct_path(prev,n) if d[n]!=float('inf') else [] for n in nodes}
    timings['dijkstra_all_pairs']=time.perf_counter()-t
    t=time.perf_counter();route,total=nearest_neighbor_tsp(depot,dest,distances);timings['nearest_neighbor_route']=time.perf_counter()-t
    expanded=[]
    for a,b in zip(route,route[1:]):
        leg=paths[a][b];expanded.extend(leg if not expanded else leg[1:])
    if not expanded:expanded=[depot]
    return dict(sorted=ordered,selected=selected,capacity=capacity,weight=weight,value=value,route=route,expanded_route=expanded,route_distance=total,dp=dp,timings=timings,paths=paths)

def print_report(r):
    print('\n'+'='*66+'\n MINI-COURIER PLANNER — REPORT\n'+'='*66)
    print('\nPARCEL PRIORITY (Merge Sort):')
    print('ID       To       Priority Deadline Weight Value')
    for p in r['sorted']:print(f"{p['id']:<8} {p['destination']:<8} {p['priority']:<8} {p['deadline']:<8} {p['weight']:<6} {p['value']}")
    print('\nPACKING (0/1 Knapsack):')
    print(f"Bag capacity={r['capacity']} | Used={r['weight']} | Selected value={r['value']}")
    for p in r['selected']:print(f"  {p['id']} -> {p['destination']} (weight {p['weight']}, value {p['value']})")
    print('\nROUTE (Dijkstra + Nearest Neighbor):')
    print('Stops: '+' -> '.join(r['route']));print('Road path: '+' -> '.join(r['expanded_route']))
    print(f"Total distance: {r['route_distance']:.1f} units")
    print('\nRUNTIME:')
    for name,t in r['timings'].items():print(f'  {name:<24} {t:.8f} s')
    print('='*66)

def benchmark(output_dir,sizes=(50,150,300,600)):
    random.seed(42);rows=[]
    for n in sizes:
        parcels=[dict(id=f'P{i:05}',priority=random.randint(1,5),deadline=random.randint(1,100)) for i in range(n)]
        tests=[('Merge Sort',merge_sort),('Quick Sort',quick_sort),('Python sorted',lambda a:sorted(a,key=lambda p:(-p['priority'],p['deadline'],p['id'])))]
        for name,fn in tests:
            t=time.perf_counter();fn(parcels);elapsed=time.perf_counter()-t;rows.append(dict(size=n,algorithm=name,runtime_seconds=elapsed))
    output_dir.mkdir(exist_ok=True,parents=True);csvfile=output_dir/'sorting_benchmark.csv'
    with csvfile.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    try:
        import matplotlib.pyplot as plt
        for name in sorted({x['algorithm'] for x in rows}):
            subset=[x for x in rows if x['algorithm']==name];plt.plot([x['size'] for x in subset],[x['runtime_seconds'] for x in subset],marker='o',label=name)
        plt.xlabel('Number of parcels');plt.ylabel('Runtime (seconds)');plt.title('Sorting Algorithm Runtime');plt.legend();plt.grid(True,alpha=.3);plt.tight_layout();plt.savefig(output_dir/'sorting_runtime.png',dpi=160);plt.close()
    except ImportError:print('Optional matplotlib missing; CSV produced, chart skipped.')
    return csvfile
