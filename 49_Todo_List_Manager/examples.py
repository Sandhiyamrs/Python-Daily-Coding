from file1_todo_list_manager import TodoManager

todo = TodoManager("tasks.json")

todo.add_task("Finish Python project")
todo.add_task("Push code to GitHub")
todo.mark_done(1)

todo.show_tasks()
