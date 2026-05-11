# Habit Tracker: Points & Levels

<img width="1011" height="783" alt="CS50P_Certificate" src="https://github.com/user-attachments/assets/56a3ef2d-0624-42b1-8ec7-e5ed8d9bc266" />

#### Description:

This is my final project for HarvardX CS50P. It reads your habits and their point values from `habits.txt`, and your daily completions from `tracker.txt`. You can view stats for any month or all time, see how many times each habit was done, your total points, and your current level. Each new level requires more points than the last.

#### How the Program works?

- **Habits and Points**: In `habits.txt`, each habit is listed with a unique number, description, and point value(e.g. `2. Read for 20 minutes;3`)
- **Tracking**: In `tracker.txt`, you log which habits you completed each day. Each entry starts with a date, followed by habit numbers and a short description(e.g. `01.01.2025: 1(Walked around the neighborhood), 2(Read a mystery novel)`).

When you run the program, it validates and parses both files using regular expressions. You can choose to view your statistics for any month or for all time. The program displays how many times each habit was completed, your total points, and your current level. The level system is designed so that each new level requires more points than the previous one.

### Project Structure:

- project.py - Main Python script.
- test_project.py - Contains automated tests for all major functions in project.py
- requirements.txt - Lists all Python libraries needed to run and test the program
- habits.txt - List of all habits to track.
- tracker.txt - Daily log of which habits you completed.
- README.md - Documentation file.

### Usage
1. **Edit `habits.txt`** to define your habits and their point value
2. **Log your daily completions** in `tracker.txt`.
3. **Run the program** with: python project.py
4. **When prompted**, enter a month name (e.g., `January`) or `All time`.
5. **View your results**: The program will show how many times each habit was completed, your total points, and your current level.

### Installation

First create a python virtual environment and then install the requirements:
```
pip install -r requirements.txt
```
Run the program script:
```
python project.py
```
Test the program script:
```
pytest test_project.py
```

### Testing

All functions are tested using pytest in `test_project.py`. Tests cover input validation, statistics, points, and level progression, as well as handling of invalid input.

### Acknowledgments

My heartfelt gratitude to David Malan and the CS50 staff for their outstanding teaching and support.

### Author: Andrii Sereda
