# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

print("BFS")
print(search.breadth_first_graph_search(ab).path())
print("-------------------")
print("DFS")
print(search.depth_first_graph_search(ab).path())
print("-------------------")
print("B&B")
print(search.branch_and_bound(ab).path())
print("-------------------")
print("B&B with underestimation")
print(search.branch_and_bound_underestimation(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
