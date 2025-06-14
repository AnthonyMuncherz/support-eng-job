class TaskDisplay {
  constructor(tasks) {
    this.tasks = tasks;
  }

    displayTasks() {
    if (!this.tasks || this.tasks.length === 0) {
      return "";  // Return empty string instead of undefined
    }
    return this.tasks.map(task => `${task.id}: ${task.title} (${task.priority})`).join("\n");
  }

  filterByPriority(priority) {
    // Handle case-insensitive priority filtering
    return this.tasks.filter(task => task.priority.toLowerCase() === priority.toLowerCase());
  }

  getTaskCount() {
    return this.tasks.length;  // Return number, not string
  }
}

module.exports = TaskDisplay;
