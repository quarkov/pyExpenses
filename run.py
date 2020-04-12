#!/usr/bin/python3

import charts
import sys


if __name__ == "__main__":
    try:
        y = int(sys.argv[1])
    except IndexError:
        y = 2020

    try:
        m = int(sys.argv[2])
    except IndexError:
        m = None

    if m:
        charts.monthly_chart(year=y, month=m)
    else:
        charts.yearly_chart(year=y)
