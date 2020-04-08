import data_retrieving as dr
import matplotlib.pyplot as plt
import numpy as np


def prep_monthly_data(year, month):
    """Converts monthly data dictionary retrieved with aggregate_by_month(year, month) function into
    a list [(expense_type, value_for_month)] which is then being sorted by value_for_month
    Returns two tuples:
    (exp_type_1, .... exp_type_n)
    (value_for_month_1, ...., value_for_month_n)
    """
    data = [(k, v) for k, v in dr.aggregate_by_month(year=year, month=month).items()]
    data.sort(key=lambda x: x[1])
    exp_types = [ch[0] for ch in data]
    exp_values = [round(ch[1]) for ch in data]
    return exp_types, exp_values


def monthly_chart(year, month):
    expense_types, expense_values = prep_monthly_data(year=year, month=month)

    fig, ax = plt.subplots()
    size = 0.25
    cmap = plt.get_cmap("tab20c")
    colors = cmap(np.arange(len(expense_types)))
    ax.pie(expense_values, radius=1, colors=colors, wedgeprops=dict(width=size, edgecolor='w'))
    ax.set(aspect="equal", title=f"Monthly expenses for {month} {year}")
    plt.show()


monthly_chart(2018, 8)
