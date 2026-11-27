from pathlib import Path
import argparse,sys
ROOT=Path(__file__).resolve().parent;sys.path.insert(0,str(ROOT/'src'))
from planner import load_dataset,run_plan,print_report,benchmark

def main():
 p=argparse.ArgumentParser(description='Mini-Courier Planner capstone application')
 p.add_argument('--data',default=str(ROOT/'data'/'sample_city.json'),help='Dataset JSON file')
 p.add_argument('--capacity',type=int,default=30,help='Courier bag capacity')
 p.add_argument('--benchmark',action='store_true',help='Benchmark sorting and export CSV/chart')
 a=p.parse_args()
 if a.capacity<0:p.error('capacity must be non-negative')
 data,graph=load_dataset(a.data);result=run_plan(data,graph,a.capacity);print_report(result)
 if a.benchmark:
  csvfile=benchmark(ROOT/'results');print(f'Benchmark CSV: {csvfile}')
  chart=ROOT/'results'/'sorting_runtime.png'
  if chart.exists():print(f'Chart: {chart}')
if __name__=='__main__':main()
