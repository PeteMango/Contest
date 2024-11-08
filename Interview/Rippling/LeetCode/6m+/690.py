"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d, imp = defaultdict(list), defaultdict(int)
        for e in employees:
            d[e.id] = e.subordinates
            imp[e.id] = e.importance
        
        def query(eid: int):
            importance = 0
            q = deque([eid])

            while q:
                f = q.popleft()
                importance += imp[f]
                for sub in d[f]:
                    q.append(sub)
            
            return importance
        
        return query(id)
        