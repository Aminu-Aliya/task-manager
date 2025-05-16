class Task:
    def __init__(self, title, deadline, priority):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.status = "Pending"

    def mark_as_completed(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "title": self.title,
            "deadline": self.deadline,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["title"], data["deadline"], data["priority"])
        task.status = data["status"]
        return task