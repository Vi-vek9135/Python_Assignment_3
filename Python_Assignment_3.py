## Content
## 1. Documentation
## 2. Implementation 







##-------------------------------------------------1. Documentation-----------------------------------##
##
##
##  1. Classes and Objects:
##     Classes: Two main classes, `Task` and `TaskList`, are defined. Additionally, a subclass `PriorityTask` is created.
##     Objects: Instances of these classes are created throughout the code, such as `task_list`, `task1`, `task2`, and `priority_task`.
##
##  2. Methods:
##     Methods: Both the `Task` and `TaskList` classes contain methods.
##     Task Methods: The `Task` class has a `mark_as_complete` method to change the task status to "complete."
##     TaskList Methods: `TaskList` class has methods like `add_task`, `add_priority_task`, `remove_task`, `list_tasks`, `find_task`, and
##                       `find_priority_task` to manage the task list.
##
##  3. Method Overloading:
##     Method Overloading in `TaskList`: Overloading is simulated in Python by providing default values for parameters. `add_task` and
##                                       `add_priority_task` methods allow adding tasks with or without a description and priority.
##
##  4. Method Overriding:
##     Method Overriding in `PriorityTask`: The `__str__` method is overridden in the `PriorityTask` class to provide a specialized string representation.
##                                          This is an example of method overriding.
##
##  5. Inheritance:
##     Inheritance: The `PriorityTask` class inherits from the `Task` class. It reuses the properties and methods of the base class while
##                  introducing additional attributes specific to priority tasks.
##
##  6. Encapsulation:
##     Encapsulation: Attributes of the classes (`title`, `description`, `status`, `priority`) are encapsulated within the classes, and
##                    access to them is controlled through methods.
##
##  7. Polymorphism:
##     Polymorphism in `__str__` methods: The `__str__` method is polymorphic, providing different string representations for `Task` and `PriorityTask` objects.
##
##
##
##      Classes and Objects are used to structure the application.
##      Methods are employed for behavior and functionality.
##      Method Overloading and Overriding enhance flexibility and allow specialization.
##      Inheritance promotes code reuse.
##      Encapsulation ensures data integrity and control over attribute access.
##      Polymorphism simplifies interactions with objects.
##
##
##
##--------------------------------------------------------------------END_OF_DOCUMENTATION--------------------------------------------------------------------##








##---------------------------------------------------2. Implementation-----------------------------------------------------------------------------------------##




# Class representing a basic Task
class Task:
    
    def __init__(self, title, description="", status="incomplete"):
        # Attributes encapsulated within the class
        self.title = title
        self.description = description
        self.status = status

    def mark_as_complete(self):
        # Method to mark a task as complete
        self.status = "complete"

    def __str__(self):
        # Method overriding to customize the string representation of a Task
        return f"Task: {self.title} - Status: {self.status}"



# Class representing a collection of tasks
class TaskList:
    
    def __init__(self):
        # Encapsulation: tasks attribute encapsulated within the class
        self.tasks = []

    def add_task(self, title, description=""):
        # Method overloading to encapsulate the creation of a regular Task and its addition to the list
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def add_priority_task(self, title, description="", priority=""):
        # Method overloading to encapsulate the creation of a PriorityTask and its addition to the list
        new_priority_task = PriorityTask(title, description, priority)
        self.tasks.append(new_priority_task)

    def remove_task(self, title):
        # Method to encapsulate the removal of a task from the list
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                break

    def list_tasks(self):
        # Method to encapsulate the display of details for all tasks in the list
        print("\nTasks:")
        for task in self.tasks:
            print(task)

    def find_task(self, title):
        # Method to encapsulate the search for a regular Task in the list by title
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def find_priority_task(self, title):
        # Method to encapsulate the search for a PriorityTask in the list by title
        for task in self.tasks:
            if isinstance(task, PriorityTask) and task.title == title:
                return task
        return None





# Class representing a PriorityTask that inherits from Task
class PriorityTask(Task):
    
    def __init__(self, title, description="", priority=""):
        # Constructor to initialize a PriorityTask, utilizing the constructor of the parent class (Task)
        super().__init__(title, description)
        self.priority = priority

    def __str__(self):
        # Method overriding to customize the string representation of a PriorityTask
        return f"Priority Task: {self.title} - Status: {self.status} - Priority: {self.priority}"


# Sample usage
task_list = TaskList()


# Adding various tasks to the task list
task_list.add_task("Do homework")

task_list.add_task("Go to the gym", "Cardio workout")

task_list.add_priority_task("Buy groceries", "Milk and eggs", "high")


# Displaying the initial list of tasks
task_list.list_tasks()


# Marking a task as complete and displaying the updated task details
task_list.find_task("Go to the gym").mark_as_complete()
print(task_list.find_task("Go to the gym"))


# Displaying details of other tasks
print(task_list.find_task("Do homework"))
print(task_list.find_priority_task("Buy groceries"))
