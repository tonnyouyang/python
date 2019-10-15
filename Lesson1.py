from xlutils.copy import copy
import xlrd

tex = xlrd.open_workbook("d:/PYTHON-TEST/testone.xls", formatting_info=True)

tem_sheet = tex.sheet_by_index(0)

new_excel = copy(tex)
new_sheet = new_excel.get_sheet(0)

new_sheet.write(2, 1, 55)
new_sheet.write(3, 1, 'best')
new_sheet.write(4, 1, 45)
new_sheet.write(5, 1, 95)

new_excel.save('d:/PYTHON-TEST/tianx.xls')
