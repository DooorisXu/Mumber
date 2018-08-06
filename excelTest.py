import xlrd

mumber = xlrd.open_workbook('C:\scripts2k18\mumberPy.xlsm')
specs = mumber.sheet_by_name('pythonSpecs')
start = int((specs.cell(3,2)).value)
print(start)

mumber = xlrd.open_workbook('C:\scripts2k18\mumberPy.xlsm')
specs = mumber.sheet_by_name('pythonSpecs')
stop = int((specs.cell(4,2)).value)
print(stop)






