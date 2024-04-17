"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

Explanation: 

Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 

return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

"""

from collections import defaultdict
import json


def answer(equations, values, queries):
    graph = defaultdict(dict)

    for (num, denom), val in zip(equations, values):
        graph[num][denom] = val
        graph[denom][num] = 1 / val

    print(f"Graph: {json.dumps(graph)}")

    # DFS to find the result for each query

    def dfs(start, end, visited: set):
        if start not in graph or end not in graph:
            return -1.0

        if start == end:
            return 1.0

        visited.add(start)

        for padosi, value in graph[start].items():
            if padosi not in visited:
                res = dfs(padosi, end, visited)
                if res != -1:
                    return value * res

        return -1.0

    # Calculate the result for each query
    results = []
    for numerator, denominator in queries:
        results.append(dfs(numerator, denominator, set()))
    print(f"Query  Output: {results}")


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

answer(equations, values, queries)
