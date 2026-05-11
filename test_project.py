from project import check_format_th, check_format_tr, find_stats, reform_habits, calculate_points, calculate_level
import pytest


def test_check_format_th():
    habits = [
        "1. Walk 10,000 steps;5\n",
        "2. Read for 20 minutes;3\n"
    ]
    assert check_format_th(habits) == True

    habits = [
        "1 Walk 10,000 steps5\n",
        "2    Read for 20 minutes;3\n"
    ]
    with pytest.raises(SystemExit):
        check_format_th(habits)


def test_check_format_tr():
    track = [
        "01.01.2025: 1(Walked around the neighborhood)\n",
        "02.01.2025: 3(Meditated before work)\n"
    ]
    result = check_format_tr(track)
    assert result == track

    track = [
        "32.01.2025: 1(Walked around the neighborhood)\n",
        "02.13.2025: 3(Meditated before work)\n"
    ]
    with pytest.raises(SystemExit):
        check_format_tr(track)


def test_find_stats():
    trackers = [
        "01.01.2025: 1(Walked), 2(Read)\n",
        "02.01.2025: 1(Walked)\n",
        "01.02.2025: 1(Walked)\n"
    ]
    monthly_habits, full_year_habits = find_stats(trackers)
    assert monthly_habits["01"]["1"] == 2
    assert monthly_habits["01"]["2"] == 1
    assert monthly_habits["02"]["1"] == 1
    assert "03" not in monthly_habits
    assert full_year_habits["1"] == 3
    assert full_year_habits["2"] == 1


def test_reform_habits():
    habits = [
        "1. Walk 10,000 steps;5\n",
        "2. Read for 20 minutes;3\n"
    ]
    dict_of_habits, points_per_habit = reform_habits(habits)
    assert points_per_habit["1"] == 5
    assert points_per_habit["2"] == 3
    assert dict_of_habits["1"] == "Walk 10,000 steps"
    assert dict_of_habits["2"] == "Read for 20 minutes"


def test_calculate_points():
    habits = {"1": 2, "2": 3}
    points = {"1": 5, "2": 4}
    assert calculate_points(habits, points) == 22


def test_calculate_level():
    assert calculate_level(0) == 1
    assert calculate_level(100) == 2
    assert calculate_level(200) == 4
    assert calculate_level(500) > 5
