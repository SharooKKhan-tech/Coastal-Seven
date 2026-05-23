from task_manager import TaskManager
from ai_helper import AIHelper
from utils import clear_screen


def display_menu():
    print("\n========== STUDENT TASK TRACKER ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    print("============================================")


def main():
    task_manager = TaskManager()
    ai_helper = AIHelper()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")

            task_manager.add_task(task)

            print("\nTask added successfully!")

            recommendations = ai_helper.get_recommendations(task)

            print("\nAI Recommendations:")
            print(recommendations)

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_manager.view_tasks()
            index = int(input("Enter task number to delete: "))
            task_manager.delete_task(index)

        elif choice == "4":
            task_manager.view_tasks()
            index = int(input("Enter task number to mark completed: "))
            task_manager.mark_completed(index)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
if __name__ == "__main__":
    main()