from datetime import datetime

class Task():
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = datetime.strptime(deadline, '%d.%m.%y')
        self.is_done = False

    def set_is_done(self):
        self.is_done = True

    def view_task_info(self):
        return(f"Задача: {self.description}; Срок: {self.deadline.strftime('%d.%m.%y')}")


tasks = []


def add_task(description, deadline):
    tasks.append(Task(description, deadline))


def view_current_tasks():
    print("Список текущих задач:")
    for index, task in enumerate(tasks):
        if not(task.is_done):
            print(f"№: {index}; {task.view_task_info()}")

def view_completed_tasks():
    print("Список выполненных задач:")
    for index, task  in enumerate(tasks):
        if task .is_done:
            print(f"№: {index}; {task.view_task_info()}")


add_task('Сделать ДЗ: OB01. Задание 1', '12.06.24')
add_task('Сделать ДЗ: OB01. Задание 2', '12.06.24')
add_task('Сделать ДЗ: OB02', '13.06.24')

tasks[0].set_is_done()

view_current_tasks()
view_completed_tasks()