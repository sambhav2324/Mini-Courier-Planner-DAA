import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from algorithms import merge_sort,quick_sort,knapsack,dijkstra,nearest_neighbor_tsp
class Tests(unittest.TestCase):
 def setUp(self):self.p=[{'id':'x','priority':1,'deadline':3},{'id':'b','priority':4,'deadline':4},{'id':'a','priority':4,'deadline':2}]
 def test_sorting_same(self):self.assertEqual([x['id'] for x in merge_sort(self.p)],[x['id'] for x in quick_sort(self.p)])
 def test_sort_order(self):self.assertEqual([x['id'] for x in merge_sort(self.p)],['a','b','x'])
 def test_knapsack_optimum(self):
  s,w,v,_=knapsack([{'id':'1','weight':3,'value':4},{'id':'2','weight':4,'value':5},{'id':'3','weight':2,'value':3}],5);self.assertEqual((w,v),(5,7))
 def test_dijkstra_shortest(self):
  g={'s':{'a':2,'b':8},'a':{'s':2,'b':1},'b':{'s':8,'a':1}};d,_=dijkstra(g,'s');self.assertEqual(d['b'],3)
 def test_tsp_approx(self):
  d={'s':{'a':2,'b':5},'a':{'s':2,'b':1},'b':{'s':5,'a':1}};r,t=nearest_neighbor_tsp('s',['a','b'],d);self.assertEqual(r,['s','a','b','s']);self.assertEqual(t,8)
if __name__=='__main__':unittest.main()
