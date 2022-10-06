import sqlite3


class Operator():

	def __init__(self, database_file):
		self.storage = database_file

	def exe(self, sql_statement, *args):
		try:
			connection = sqlite3.connect(self.storage)
			cursor = connection.cursor()
			cursor.execute(sql_statement, args)
			connection.commit()
			connection.close()
		except sqlite3.OperationalError as err:
			print('Database operation failed:', sql_statement, ', with {} args.'.format(len(args)))
			print(err)

	def query(self, sql_statement, *args,  option='one'):
		try:
			connection = sqlite3.connect(self.storage)
			cursor = connection.cursor()
			cursor.execute(sql_statement, args)
			if isinstance(option, int):
				result = cursor.fetchmany(option)
			elif option == 'one':
				result = cursor.fetchone()
			elif option == 'all':
				result = cursor.fetchall()
			else:
				connection.close()
				raise 'Invalig arg for query().'
			connection.close()
			return result  # query results can be None, tuples or lists of tuples
		except sqlite3.OperationalError as err:
			print('Database operation failed:', sql_statement, ', with {} args.'.format(len(args)))
			print(err)