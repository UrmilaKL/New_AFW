

import openpyxl

def get_cell_data(path, sheet, row, col):
    try:
        wb = openpyxl.load_workbook(path)
        p = wb[sheet].cell(row,col).value
        return p
    except:
        return ""

v = get_cell_data("../test_data/input.xlsx","Sheet1",1,1)
print(v)