import sqlite3

def create_conn(db):
	return sqlite3.connect(db)
	

def execute_query(cursor, query):
	try:
		cursor.execute(query)
		print("Query Executed Successfully")
	except Exception as e:
		return {"error": e}
	
	if cursor.description:
		result={
			"column_names": [col[0] for col in cursor.description],
			"data": cursor.fetchall()
		}
		return result
	
	
def close_conn(conn):
	conn.close()
	

def run_input_queries(conn, queries):
	cursor=conn.cursor()
	results=[]
	for query in queries.split(';'):
		if query.strip():
			output=execute_query(cursor, query.strip())
			if output:
				results.append(output)
				if "error" in output:
					break
				else:
					conn.commit()
		
	cursor.close()
	return results

def get_database_schema(conn):
	cursor=conn.cursor()
	tables={}
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	for table in cursor.fetchall():
		cursor.execute(f"PRAGMA table_info({table[0]})")
		tables[table[0]]=cursor.fetchall()
	
	return tables

if __name__=="__main__":
	queries='''
		create table student (
			roll_no int primary key,
			name varchar(50),
			course varchar(50)
		);
	
		insert into student (roll_no, name, course)
		values (1, 'Anmol', 'btech'),
		(2, 'Piyush', 'bca'),
		(3, 'Harsh', 'bcom'),
		(4, 'Ritvik', 'btech');
		
		alter table student add column faculty varchar(50);
		select * from student;
	'''
	#queries="select * from Customer;"
	conn=create_conn("data.db")
	results=run_input_queries(conn, queries)
	for output in results:
		if "error" in output:
			print("error:", output["error"])
		else:
			print("result:", output)
		print()
	
	print("tables:", get_database_schema(conn))
	close_conn(conn)