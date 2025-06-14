class Task:
    def __init__(self, id, title, priority, status="pending"):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, id, title, priority):
        # Check for duplicate IDs
        for existing_task in self.tasks:
            if existing_task.id == id:
                return None  # Don't add duplicate ID
        
        task = Task(id, title, priority)
        self.tasks.append(task)
        return task

    def update_status(self, id, new_status):
        for task in self.tasks:
            if task.id == id:
                task.status = new_status
                return True
        # Remove the bug that updates all tasks when ID not found
        return False

    def get_high_priority_tasks(self):
        high_priority = []
        for task in self.tasks:
            # Handle both string "high" and numeric priority 1 as high priority
            if task.priority == "high" or task.priority == 1:
                high_priority.append(task)
        return high_priority
