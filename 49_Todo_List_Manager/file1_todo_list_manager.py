import json
import os
from datetime import datetime

class TodoManager:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """Save todos to file."""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=4)
    
    def add_todo(self, task, priority='Medium', due_date=None):
        """Add a new todo."""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'priority': priority,
            'due_date': due_date,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.todos.append(todo)
        self.save_todos()
        return todo['id']
    
    def view_todos(self, filter_status=None, filter_priority=None):
        """View all todos with optional filters."""
        filtered_todos = self.todos
        
        if filter_status is not None:
            filtered_todos = [t for t in filtered_todos if t['completed'] == filter_status]
        
        if filter_priority:
            filtered_todos = [t for t in filtered_todos if t['priority'] == filter_priority]
        
        return filtered_todos
    
    def complete_todo(self, todo_id):
        """Mark todo as complete."""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                return True
        return False
    
    def delete_todo(self, todo_id):
        """Delete a todo."""
        self.todos = [t for t in self.todos if t['id'] != todo_id]
        self.save_todos()
        return True
    
    def display_todos(self, todos):
        """Display todos in formatted way."""
        if not todos:
            print("No tasks found!")
            return
        
        print("\n" + "="*80)
        print(f"{'ID':<5} {'Task':<30} {'Priority':<10} {'Due Date':<12} {'Status':<10}")
        print("="*80)
        
        for todo in todos:
            status = "✓ Done" if todo['completed'] else "⧖ Pending"
            due = todo['due_date'] if todo['due_date'] else 'N/A'
            task = todo['task'][:27] + '...' if len(todo['task']) > 30 else todo['task']
            
            print(f"{todo['id']:<5} {task:<30} {todo['priority']:<10} {due:<12} {status:<10}")
        
        print("="*80 + "\n")

def main():
    manager = TodoManager()
    
    while True:
        print("\n=== Todo List Manager ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
        print("5. Complete Task")
        print("6. Delete Task")
        print("7. Filter by Priority")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            task = input("Enter task: ").strip()
            print("\nPriority: 1-High, 2-Medium, 3-Low")
            priority_choice = input("Enter priority (1-3): ").strip()
            
            priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
            priority = priority_map.get(priority_choice, 'Medium')
            
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter: ").strip()
            due_date = due_date if due_date else None
            
            todo_id = manager.add_todo(task, priority, due_date)
            print(f"\n✓ Task added with ID: {todo_id}")
        
        elif choice == '2':
            todos = manager.view_todos()
            manager.display_todos(todos)
        
        elif choice == '3':
            todos = manager.view_todos(filter_status=False)
            manager.display_todos(todos)
        
        elif choice == '4':
            todos = manager.view_todos(filter_status=True)
            manager.display_todos(todos)
        
        elif choice == '5':
            todo_id = int(input("Enter task ID to complete: ").strip())
            if manager.complete_todo(todo_id):
                print("\n✓ Task marked as complete!")
            else:
                print("\n✗ Task not found!")
        
        elif choice == '6':
            todo_id = int(input("Enter task ID to delete: ").strip())
            manager.delete_todo(todo_id)
            print("\n✓ Task deleted!")
        
        elif choice == '7':
            print("\n1-High, 2-Medium, 3-Low")
            priority_choice = input("Enter priority: ").strip()
            priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
            priority = priority_map.get(priority_choice, 'Medium')
            
            todos = manager.view_todos(filter_priority=priority)
            manager.display_todos(todos)
        
        elif choice == '8':
            print("\nGoodbye!")
            break
        
        else:
            print("\n✗ Invalid choice!")

if __name__ == "__main__":
    main()
