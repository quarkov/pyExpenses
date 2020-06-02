import data_retrieving as dr
import matplotlib.pyplot as plt
import numpy as np
import os


currency = "EUR"
months = {1: "January", 2: "February", 3: "March",
          4: "April", 5: "May", 6: "June", 7: "July",
          8: "August", 9: "September", 10: "October",
          11: "November", 12: "December"}


def check_dir(year):
    if not os.path.exists("pics"): os.mkdir("pics")
    if not os.path.exists(f"pics/{year}"): os.mkdir(f"pics/{year}")


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
    month_total = sum(expense_values)
    percents = [round(e_val*100/month_total, 1) for e_val in expense_values]

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.set(aspect="equal")
    ax.pie(x=expense_values,
           radius=1.,
           colors=plt.get_cmap("plasma")(np.arange(255, 1, -255//len(expense_types))),
           wedgeprops=dict(width=0.25, edgecolor='w'),
           startangle=-60,
           center=(-2, 0))

    labels = [f"{percents[i]}% ".rjust(6, " ") +
              f"({expense_values[i]} {currency})".rjust(11, " ") +
              f" - {e_type}"
              for i, e_type in enumerate(expense_types)]

    ax.legend(labels, bbox_to_anchor=(1, 0.1, 0.5, 1), loc="right")
    ax.pie([0, 0])
    ax.text(1.1, -1, f"Total spent: {month_total} {currency}", style='oblique',
            bbox={'facecolor': 'blue', 'alpha': 0.1, 'pad': 8})

    plt.title(s=f"Expenses {year}, {months[month]}",
              fontsize=14)

    check_dir(year)
    plt.savefig(f'pics/{year}/{year}_{month}.jpg')


def yearly_chart(year):
    seq = np.arange(1, 13)
    exp_by_month = [sum(prep_monthly_data(year, i)[1]) for i in range(1, 13)]

    plt.grid(False, 'major', 'y', ls='--', lw=.5, c='k', alpha=0.3)
    plt.bar(seq, exp_by_month, 0.2, color='#4b57db')

    plt.xticks(seq, months.values(), rotation=60, fontsize=8)
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    plt.title(s=f"Yearly expenses, {year}. Total - {sum(exp_by_month)} {currency}",
              bbox={'facecolor': 'blue', 'alpha': 0.1, 'pad': 4},
              fontsize=10)

    check_dir(year)
    plt.savefig(f'pics/{year}/{year}_0.jpg')


def draw_chart(year, month=None):
    if month:
        monthly_chart(year, month)
    else:
        yearly_chart(year)
