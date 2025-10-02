import csv
from datetime import datetime  # For storing date of tasks

# Main function for Daily Task Organizer
def main():
    checklist = []          # Stores all tasks entered for today
    completed_tasks = []    # Stores tasks marked as completed
    incomplete_tasks = []   # Stores tasks marked as incomplete
    
    # --- Step 1: User adds tasks ---
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
    
    # Input each task with validation
    for i in range(n):
        while True:
            task = input(f"Enter task {i+1}: ").strip()
            if task:  # Ensure task is not empty
                checklist.append(task)
                break
            else:
                print("Task cannot be empty. Please enter a valid task.")
    
    # --- Step 2: Display today's checklist ---
    print("\n" + "="*30)
    print("TODAY'S CHECKLIST:")
    print("="*30)
    for i, task in enumerate(checklist, 1):
        print(f"{i}. {task}")
    
    # --- Step 3: End of day review ---
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
    
    # --- Step 4: Print daily summary ---
    print("\n" + "="*40)
    print("DAILY SUMMARY")
    print("="*40)
    
    # Helper function to print completed/incomplete tasks
    def print_tasks(title, tasks):
        print(title)
        if tasks:
            for task in tasks:
                print(f"   • {task}")
        else:
            print("   None")
    
    print_tasks(f"✅ COMPLETED TASKS ({len(completed_tasks)}):", completed_tasks)
    print_tasks(f"\n❌ INCOMPLETE TASKS ({len(incomplete_tasks)}):", incomplete_tasks)
    
    # Completion rate and motivation messages
    completion_rate = (len(completed_tasks) / len(checklist)) * 100 if checklist else 0
    print(f"\n📈 Completion Rate: {completion_rate:.1f}%")
    
    if completion_rate == 100:
        print("🏆 Perfect day! You completed all your tasks!")
    elif completion_rate >= 75:
        print("🌟 Great job! You completed most of your tasks!")
    elif completion_rate >= 50:
        print("👍 Good effort! Keep it up!")
    else:
        print("💪 Tomorrow is a new day. You can do better!")

    # --- Step 5: Save tasks to CSV (pretty format, single date block) ---
    today = datetime.now().strftime("%Y-%m-%d")  # Get current date
    filename = "daily_tasks_record.csv"

    # Read existing content to check if today's date already exists
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    # Open CSV for appending
    with open(filename, "a") as f:
        if today not in content:
            # If today's date not in file, write header + date
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
            # Append tasks under today's existing block (no new header/date)
            for task in completed_tasks:
                f.write(f"{''.ljust(11)} , {task.ljust(20)} , Completed\n")
            for task in incomplete_tasks:
                f.write(f"{''.ljust(11)} , {task.ljust(20)} , Incomplete\n")

    print(f"📂 Record CSV report saved to {filename}")


# Run the program
if __name__ == "__main__":
    main()
