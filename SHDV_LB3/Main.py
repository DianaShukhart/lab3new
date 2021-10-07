#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                item = self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0

        # находим максимальное число и его координаты
        # [0] - максимальное число, [1] - строка максимума, [2] - столбец максимума
        list_information_min_num = find_min(self.tableWidget)

        if not list_information_min_num:
            self.label_error.setText('Введены неправильные данные!')
        else:
            # выводим на кэран информацию о расположении максимального числа
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_min_num[0]) + ' [' +
                str(list_information_min_num[1]) + ';' + str(list_information_min_num[2]) + ']')

    def solve(self):
        # Нашли минимальное число
        list_information_min_num = find_min(self.tableWidget)

        if not list_information_min_num:
            self.label_error.setText('Введены некорректные данные!')
        else:
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_min_num[0]) + ' [' +
                str(list_information_min_num[1]) + ';' + str(list_information_min_num[2]) + ']')

            # -*- решение задания -*-
            row = 0

            while row < self.tableWidget.rowCount():
                item = self.tableWidget.item(row, 1).text()
                # преобразовать в число все типы для првоерки
                item = int(item)
                min_num = int(list_information_min_num[0]) # int - convert to number
                if item == min_num:
                    # новая переменная для цикла, чтобы цикл начался с начала
                    row2 = 0
                    while row2 < self.tableWidget.rowCount():
                        self.tableWidget.setItem(row2, 1, QTableWidgetItem(str("0"))) # заменяет на 0
                        row2 += 1
                #self.label_sum.setText('Сумма единиц перед максимальным элементом: ' + str(number_of_units))
                row += 1

        self.label_error.setText('')


def find_min(table_widget):
    """
    находим максимальное число из таблицы и его координаты
    :param table_widget: таблица
    :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
            то None
    """

    row_max_number = 0  # номер строки, в котором находится максимальне число
    col_max_number = 0  # номер столбца, в котором находится максимальне число
    max_num = float(table_widget.item(row_max_number, col_max_number).text())  # Максимальное значение

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number < max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number]
    except Exception:
        return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
