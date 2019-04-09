import pyodbc 
import csv

class SQL: 		
	def ExportQueryToCSV(self, inputFile, outputFile):
        
		conn = pyodbc.connect('Driver={SQL Server};'
							  'Server=dblinx;'
							  'Database=Linx;'
							  'Trusted_Connection=yes;')

		cursor = conn.cursor()

		f = open(inputFile + ".sql", "r")
		query = f.read()

		tmp = cursor.execute(query)
		columns = [i[0] for i in cursor.description]
		results = tmp.fetchall()

		with open(outputFile + '.csv', 'w', newline='') as fp:
			a = csv.writer(fp, delimiter=';')
			a.writerow(columns)
			a.writerows(results)
			
	def InsertExample(self, cod_obc, cod_erp, data, filial, almox, usuario, projeto):
		conn = pyodbc.connect('Driver={SQL Server};'
							  'Server=dblinx;'
							  'Database=Linx;'
							  'Trusted_Connection=yes;')

		cursor = conn.cursor()

		cursor.execute("INSERT INTO OBC_REQUISICOES(COD_REQUISICAO_OBC, COD_REQUISICAO_ERP, DATA_REQUISICAO, CODIGO_FILIAL_ERP, CODIGO_ALMOXARIFADO_ERP, USUARIO, PROJETO)" 
					   "VALUES (?, ?, ?, ?, ?, ?, ?)", cod_obc, cod_erp, data, filial, almox, usuario, projeto)
		conn.commit()

