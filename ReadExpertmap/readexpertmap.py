import xlrd


def readExpertMap(charter):
    dataXlsx = xlrd.open_workbook("z-score/data/expert/专家图.xlsx")
    table = dataXlsx.sheet_by_name("Sheet1")
    return table.cell(int(charter), 2).value


