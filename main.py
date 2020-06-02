import os
import sys
from charts import draw_chart
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from PySide2.QtGui import *
from PySide2.QtCore import *


def load_ui():
    ui_file_name = "app.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    ui = loader.load(ui_file)
    ui_file.close()
    return ui


def populate_tree_widget(ui):
    years = sorted(os.listdir('data'), reverse=True)
    for y in years:
        year = QTreeWidgetItem(ui.treeWidget, [y])
        months = sorted(f_name.split('.')[0] for f_name in os.listdir(f'test data/{y}') if f_name.endswith('.csv'))
        [QTreeWidgetItem(year, [m]) for m in months]


def render_report():
    query = ui.treeWidget.currentItem().text(0)
    try:
        year, month = map(int, query.split('_'))
    except ValueError:
        year, month = int(query), 0

    path = f"pics/{year}/{year}_{month}.jpg"
    if not os.path.exists(path):
        draw_chart(year, month)

    os.chdir(f"pics/{year}")
    f_name = str(year) + "_" + str(month) + '.jpg'
    pixmap = QPixmap(f_name)
    ui.picLabel.setPixmap(pixmap)
    os.chdir('../..')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = load_ui()
    populate_tree_widget(ui)
    ui.treeWidget.itemDoubleClicked.connect(render_report)
    ui.show()
    sys.exit(app.exec_())
