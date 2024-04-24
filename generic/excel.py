import openpyxl
class Excel:
    @staticmethod
    def get_cell_data(path, sheet, row, col):
        try:
            wb = openpyxl.load_workbook(path)
            p = wb[sheet].cell(row, col).value
            return p
        except:
            return ""