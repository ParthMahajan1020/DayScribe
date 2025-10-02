import csv
from datetime import datetime

# Daily Task Organizer - Debugged & Cleaned
def main():
    checklist = []
    completed_tasks = []
    incomplete_tasks = []
    
    # User adds tasks
    while True:
        try:
            n = int(input("How many tasks do you want to add today? "))
            if n < 0:
                print("Please enter a positive number.")
                continue
            elif n == 0:
                print("No tasks to add. Exiting program.")
                return
            break
        except ValueError:
            print("Please enter a valid number.")
    
    for i in range(n):
        while True:
            task = input(f"Enter task {i+1}: ").strip()
            if task:
                checklist.append(task)
                break
            else:
                print("Task cannot be empty. Please enter a valid task.")
    
    # Display checklist
    print("\n" + "="*30)
    print("TODAY'S CHECKLIST:")
    print("="*30)
    for i, task in enumerate(checklist, 1):
        print(f"{i}. {task}")
    
    # End of day review
    print("\n" + "="*30)
    print("END OF DAY REVIEW")
    print("="*30)
    for task in checklist:
        while True:
            status = input(f"Did you complete '{task}'? (y/n): ").lower().strip()
            if status in ['y', 'yes']:
                completed_tasks.append(task)
                break
            elif status in ['n', 'no']:
                incomplete_tasks.append(task)
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    # Results
    print("\n" + "="*40)
    print("DAILY SUMMARY")
    print("="*40)
    
    def print_tasks(title, tasks):
        print(title)
        if tasks:
            for task in tasks:
                print(f"   • {task}")
        else:
            print("   None")
    
    print_tasks(f"✅ COMPLETED TASKS ({len(completed_tasks)}):", completed_tasks)
    print_tasks(f"\n❌ INCOMPLETE TASKS ({len(incomplete_tasks)}):", incomplete_tasks)
    
    # Completion rate
    completion_rate = (len(completed_tasks) / len(checklist)) * 100 if checklist else 0
    print(f"\n📈 Completion Rate: {completion_rate:.1f}%")
    
    # Motivation
    if completion_rate == 100:
        print("🏆 Perfect day! You completed all your tasks!")
    elif completion_rate >= 75:
        print("🌟 Great job! You completed most of your tasks!")
    elif completion_rate >= 50:
        print("👍 Good effort! Keep it up!")
    else:
        print("💪 Tomorrow is a new day. You can do better!")

    # --- Save results to CSV (single date block) ---
    today = datetime.now().strftime("%Y-%m-%d")
    filename = "daily_tasks_record.csv"

    # Read existing content
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    with open(filename, "a") as f:
        # If today's date not in file, write header + date
        if today not in content:
            f.write(f"\nDate       , Task                 , Status\n")
            first_task = True
            for task in completed_tasks:
                if first_task:
                    f.write(f"{today.ljust(11)} , {task.ljust(20)} , Completed\n")
                    first_task = False
                else:
                    f.write(f"{''.ljust(11)} , {task.ljust(20)} , Completed\n")
            for task in incomplete_tasks:
                if first_task:
                    f.write(f"{today.ljust(11)} , {task.ljust(20)} , Incomplete\n")
                    first_task = False
                else:
                    f.write(f"{''.ljust(11)} , {task.ljust(20)} , Incomplete\n")
        else:
            for task in completed_tasks:
                f.write(f"{''.ljust(11)} , {task.ljust(20)} , Completed\n")
            for task in incomplete_tasks:
                f.write(f"{''.ljust(11)} , {task.ljust(20)} , Incomplete\n")

    print(f"📂 Record CSV report saved to {filename}")



if __name__ == "__main__":
    main()
