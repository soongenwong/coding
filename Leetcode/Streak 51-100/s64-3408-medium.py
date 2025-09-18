class TaskMeta:
    def __init__(self, uId, p):
        self.priority = p
        self.uId = uId

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        # for every task store userID & priority
        self.taskMeta = {}
        for task in tasks:
            uId, taskId, priority = task
            heapq.heappush(self.heap, (-priority, -taskId))
            self.taskMeta[taskId] = TaskMeta(uId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId))
        self.taskMeta[taskId] = TaskMeta(userId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        curr = self.taskMeta[taskId]
        self.taskMeta[taskId] = TaskMeta(curr.uId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.taskMeta[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, taskId = heapq.heappop(self.heap)
            if -taskId in self.taskMeta:
                curr = self.taskMeta[-taskId]
                if curr.priority == -priority:
                    del self.taskMeta[-taskId]
                    return curr.uId
        return -1
                    
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()