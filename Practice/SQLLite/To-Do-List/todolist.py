# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta


# creating the sqlite database engine with sqlalchemy
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

#  It allows us to create classes that include directives
#  to describe the actual database table they will be mapped to.
Base = declarative_base()

# defining the class for the database table 'task'


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return f'<Task todo: "{self.task}">'


# creates the table in the database by running sql commands(internally)
Base.metadata.create_all(engine)

# Manages persistence operations for ORM-mapped objects
Session = sessionmaker(bind=engine)
my_session = Session()

task_1 = Task(task='to complete the to do list project')


def add_task():
    task = input("Enter task\n")
    deadline = input("Enter deadline\n")
    deadline = datetime.strptime(deadline, '%Y-%m-%d')
    task_obj = Task(task=task, deadline=deadline)
    my_session.add(task_obj)
    my_session.commit()
    print("The task has been added!")

    return task_obj


# prints out all the tasks of the present day
def tasks_today():
    today = datetime.today().strftime("%Y-%m-%d")
    tasks = my_session.query(Task).filter(Task.deadline == today).all()
    date = datetime.today().strftime("%d %b")
    if len(tasks):
        print(f"Today {date}")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task.task}")
    else:
        print(f"Today {date}")
        print("Nothing to do!")


# prints out all the tasks of a week from today
def week_tasks():
    today = datetime.today()
    for i in range(7):
        day = today + timedelta(days=i)
        day_str = day.strftime("%Y-%m-%d")
        tasks = my_session.query(Task).filter(Task.deadline == day_str).all()
        date = day.strftime("%A %b %d")
        if tasks:
            print(date)
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task.task}")
            print()
        else:
            print(date)
            print("Nothing to do! \n")


# prints all the tasks sorting by date
def all_tasks():
    tasks = my_session.query(Task).all()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.task}. {task.deadline.strftime('%d %b')}")
    else:
        print("Nothing to do!")


def delete_task():
    print('Chose the number of the task you want to delete:')
    tasks = my_session.query(Task).all()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.task}. {task.deadline.strftime('%d %b')}")
    else:
        print("Nothing to do!")
    n = int(input()) - 1
    del_task = my_session.query(Task).all()[n]
    my_session.delete(del_task)
    my_session.commit()
    print('The task has been deleted!')


def missed_task():
    today = datetime.today().strftime("%Y-%m-%d")
    tasks = my_session.query(Task).filter(Task.deadline < today).all()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.task}. {task.deadline.strftime('%d %b')}")


def ask():
    print("""
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
""")
    user_choice = input()
    return user_choice


while True:
    choice = ask()
    if choice == '1':
        tasks_today()
    elif choice == '2':
        week_tasks()
    elif choice == '3':
        all_tasks()
    elif choice == '4':
        missed_task()
    elif choice == '5':
        add_task()
    elif choice == '6':
        delete_task()
    elif choice == '0':
        break
