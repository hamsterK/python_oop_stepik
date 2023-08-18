from collections import namedtuple


class Todo:
    def __init__(self):
        self.things = list()
        self.Task = namedtuple('Task', ['task', 'priority'])

    def add(self, task: str, priority: int):
        self.things.append(self.Task(task, priority))

    def get_by_priority(self, selected_priority: int):
        if len(self.things) == 0:
            return []
        return [task.task for task in self.things if task.priority == selected_priority]

    def get_low_priority(self):
        if len(self.things) == 0:
            return []
        min_priority = min(task.priority for task in self.things)
        return [task.task for task in self.things if task.priority == min_priority]

    def get_high_priority(self):
        if len(self.things) == 0:
            return []
        max_priority = max(task.priority for task in self.things)
        return [task.task for task in self.things if task.priority == max_priority]


todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))
