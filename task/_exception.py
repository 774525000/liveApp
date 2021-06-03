class TaskException(Exception):
    basic_str = ''

    def __init__(self, msg: str = ''):
        self.msg = msg

    def __str__(self):
        return f'{self.basic_str}: {self.msg}'

    def __repr__(self):
        return self.__str__()


class NoSuchTaskNameException(TaskException):
    basic_str = 'no such task name'


class NotAsyncTaskException(TaskException):
    basic_str = 'not a async task function'
