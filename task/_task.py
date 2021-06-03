import asyncio
from spider import Spider
from inspect import isfunction
from ._exception import NoSuchTaskName


class Task:
    def __init__(self):
        self._tasks = {}

    def add_task(self, task_name):
        def callback(fn):
            if isfunction(fn):
                self._handle_task(task_name, fn)

        return callback

    def _handle_task(self, task_name, fn):
        tasks = self._tasks.get(task_name)
        if tasks is None:
            self._tasks[task_name] = []
        self._tasks[task_name].append(fn)

    def execute_task(self, task_name, *args, **kwargs):
        tasks = self._tasks.get(task_name)
        if tasks is None:
            raise NoSuchTaskName(task_name)
        asyncio.run(self._run(tasks, *args, **kwargs))

    @staticmethod
    async def _run(tasks, *args, **kwargs):
        async with Spider.async_client() as _:
            task_list = []
            for task in tasks:
                task_list.append(task(*args, **kwargs))
            await asyncio.gather(*task_list)
