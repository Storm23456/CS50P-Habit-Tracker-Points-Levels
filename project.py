import re
import sys

month_names = {'01': 'January',
               '02': 'February',
               '03': 'March',
               '04': 'April',
               '05': 'May',
               '06': 'June',
               '07': 'July',
               '08': 'August',
               '09': 'September',
               '10': 'October',
               '11': 'November',
               '12': 'December',
               }


def main():
    with open("habits.txt", "r") as file_th, open("tracker.txt", "r") as file_tr:
        habits = file_th.readlines()
        track = file_tr.readlines()
    check_format_th(habits)
    list_of_tracker = check_format_tr(track)
    habits_by_months, habits_full_year = find_stats(list_of_tracker)
    dict_of_habits, points_per_habit = reform_habits(habits)
    total_points = calculate_points(habits_full_year, points_per_habit)
    level = calculate_level(total_points)
    user_input = input("Enter month name(ex. January) or 'All time': ").strip().lower()
    new_months_names = {value.lower(): key for key, value in month_names.items()}
    if user_input == "all time":
        print("All time: ")
        if habits_full_year:
            for habit in sorted(habits_full_year, key=lambda x: int(x)):
                habit_info = dict_of_habits.get(habit)
                count_of_habit = habits_full_year[habit]
                print(f"{habit}. {habit_info}: {count_of_habit}")
        else:
            print("There's no data")
    elif user_input in new_months_names:
        month = new_months_names[user_input]
        if month in habits_by_months and habits_by_months[month]:
            print(f"{month_names[month]}")
            for habit in sorted(habits_by_months[month], key=lambda x: int(x)):
                habit_info = dict_of_habits.get(habit)
                count_of_habit = habits_by_months[month][habit]
                print(f"{habit}. {habit_info}: {count_of_habit}")
        else:
            print(f"There's no data for {user_input.title()}")
    else:
        print("Invalid month")
    print(f"Your points: {total_points}")
    print(f"Your level: {level}")


def check_format_th(habits):
    for line in habits:
        matches = re.search(r"^(\d+)\. .*;(\d+)$", line)
        if matches:
            return True
        else:
            sys.exit("Invalid data in things_to_do.txt")


def check_format_tr(track):
    list_tracker = []
    for line in track:
        matches = re.search(
            r"^((\d{2})\.(\d{2})\.\d{4}): ((\d+\([^)]*\)(,? ?(\d+\([^)]*\))?)*)|-)$", line)
        if matches:
            days = int(matches.group(2))
            months = int(matches.group(3))
            if days < 1 or days > 31:
                sys.exit("Day is out of range in tracker.txt")
            if months < 1 or months > 12:
                sys.exit("Month is out of range in tracker.txt")
            list_tracker.append(line)
        elif line.strip() == "":
            continue
        else:
            sys.exit("Invalid data in tracker.txt")
    return list_tracker


def find_stats(trackers):
    monthly_habits = {}
    full_year_habits = {}
    for tracker in trackers:
        month_match = re.search(r"^(\d{2}\.(\d{2})\.\d{4}):", tracker)
        if not month_match:
            continue
        month = month_match.group(2)
        done = re.findall(r"(?<=:|,)\s*(\d+)\(", tracker)
        if month not in monthly_habits:
            monthly_habits[month] = {}
        for habit in done:
            monthly_habits[month][habit] = monthly_habits[month].get(habit, 0) + 1
            full_year_habits[habit] = full_year_habits.get(habit, 0) + 1
    return monthly_habits, full_year_habits


def reform_habits(habits):
    dict_of_habits = {}
    points_per_habit = {}
    for habit in habits:
        match_number = re.search(r"^(\d+)\. (.*);(\d+)$", habit)
        if match_number:
            dict_of_habits[match_number.group(1)] = match_number.group(2)
            points_per_habit[match_number.group(1)] = int(match_number.group(3))
    return dict_of_habits, points_per_habit


def calculate_points(habits, points):
    total_points = 0
    for habit, count in habits.items():
        amount_of_points = points.get(habit, 0)
        total_points += count * amount_of_points
    return total_points


def calculate_level(points):
    level = 1
    points_needed = 100
    while points >= points_needed:
        level += 1
        points_needed = int(points_needed * 1.4)
    return level


if __name__ == "__main__":
    main()
