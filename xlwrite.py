import xlsxwriter
global row
class Excel:
	def __init__(self,workbook):
		self.workbook = workbook
		#self.workseet = workseet

	def create_workbook(self):
		self.created_workbook = xlsxwriter.Workbook('{}'.format(self.workbook))
		return self.created_workbook

	def create_worksheet(self,sheet_name):
		self.worksheet = self.created_workbook.add_worksheet('{}'.format(sheet_name))
		return self.worksheet

	def create_columns(self,*argv,format_color = None):
		row_number = 0
		for i,name in zip(range(0, len(argv)),argv):
			self.worksheet.write(row_number, i, '{}'.format(name),format_color)

	def write_row(self,variable, names, format_color =None):
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)
			self.worksheet.write(row,2, '{}'.format(data),format_color)

	def close_workbook(self):
		return self.created_workbook.close()




lst = ['1','3','7','5']
lst1 = ['1','4444','7','8']
excel =Excel('test.xlsx')

excel.create_workbook()
excel.create_worksheet('This is a test')
excel.create_columns('This','is','how','we','do','it')
row = 0
for i, j in zip(lst,lst1):
	excel.write_row(y1=i,y2=j)


excel.close_workbook()
