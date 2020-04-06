import os
from datetime import datetime
from collections import defaultdict
import csv


def year_is_valid(year):
    if type(year) != int: raise TypeError(f"Year should be int, not {type(year)}")
    return 1900 <= year <= datetime.now().year


def month_is_valid(month):
    if type(month) != int: raise TypeError(f"Month should be int, not {type(month)}")
    return 1 <= month <= 12


def normalize_path(year, month):
    """Returns relevant path to a data file.
    """
    if not year_is_valid(year):
        raise ValueError(f"Year should be in range [1900; {datetime.now().year}]")
    if not month_is_valid(month):
        raise ValueError(f"Month should be in range [1; 12]")

    filename = f"{year}_{month}.csv" if month > 9 else f"{year}_0{month}.csv"
    path = f"data/{year}/{filename}"
    return path


def path_to_data(year, month):
    """Checks if data file exists for given year and month.
    """
    path = normalize_path(year, month)
    if not os.path.exists(path): raise FileNotFoundError(f"No file found here: {path}")
    return path


def by_month(year, month):
    """Aggregates data for given year and month.
    Reads a relevant csv file with data (if exists).
    Returns a dictionary {"expense_type": monthly_expenses}.
    """
    path = path_to_data(year, month)
    monthly_expenses = defaultdict(float)
    with open(path) as file:
        data = csv.DictReader(file)
        for row in data:
            exp_type, exp_value = row["type"], float(row["euro"])
            monthly_expenses[exp_type] += round(exp_value, 1)
    return monthly_expenses
