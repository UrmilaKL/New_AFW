from generic.base_setup import Base_Setup
from generic.excel import Excel

class Test1(Base_Setup):
    def test1(self):
        p = Excel.get_cell_data("../test_data/input.xlsx","Sheet1",1,1)
        print("Data from Excel", p)
        print(self.driver.title)
