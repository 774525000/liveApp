class NoSuchTaskName(Exception):
    def __init__(self, task_name: str = ''):
        self.task_name = task_name

    def __str__(self):
        return f'no such task name: {self.task_name}'

    def __repr__(self):
        return self.__str__()
