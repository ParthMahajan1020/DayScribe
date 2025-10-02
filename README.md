# DayScribe

DayScribe is a minimalist Python-based daily task tracker that helps you organize, review, and log your daily tasks.
It allows you to track completed and incomplete tasks in a clean, human-readable CSV format. Perfect for anyone who
wants to improve productivity and keep a daily record of their tasks.

---

## Features

- Add multiple tasks for the day.
- End-of-day review: mark tasks as completed or incomplete.
- Calculates your daily **completion rate** and provides motivational messages.
- Saves all tasks in a **pretty, readable CSV file** with aligned columns.
- Ensures that tasks for the same day are grouped under a single date.
- Minimal command-line interface — fast and distraction-free.

---

## Example Output

**CSV (pretty format):**

Date , Task , Status
2025-10-02 , Go to gym , Completed
, Meet friends , Completed
, Do some coding , Incomplete


**Terminal Summary:**

✅ COMPLETED TASKS (2):
• Go to gym
• Meet friends

❌ INCOMPLETE TASKS (1):
• Do some coding

📈 Completion Rate: 66.7%
👍 Good effort! Keep it up!


---

## Installation

1. Clone the repository:

git clone https://github.com/ParthMahajan1020/DayScribe.git

2. Navigate into the project folder:

cd DayScribe

3. Run the program using Python 3:

python main.py

---

### Usage

- Enter the number of tasks for the day.

- Input each task.

- At the end of the day, mark each task as completed or incomplete.

- Your tasks will be saved automatically in a pretty CSV file (daily_tasks_pretty.csv).

---

### Motivational Messages

- 100% completion → “🏆 Perfect day! You completed all your tasks!”

- 75–99% completion → “🌟 Great job! You completed most of your tasks!”

- 50–74% completion → “👍 Good effort! Keep it up!”

---

### Future Enhancements

- Add weekly/monthly summary reports.

- Integrate priority levels for tasks.

- Add reminders/notifications for pending tasks.

- Optional GUI interface for more interactive use.

- Below 50% → “💪 Tomorrow is a new day. You can do better!”

---
