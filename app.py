from flask import Flask, jsonify, request, redirect, url_for
from pymysql import connect, cursors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/success')
def success():
	return "提交成功"

@app.route('/mysql/<string:stu_id>')
def get_mysql(stu_id):
	print(stu_id)
	sql = 'select * from cs_register where stu_id=' + stu_id
	print(sql)
	try:
		data = find_mysql(sql)
		print(data)
		return jsonify(data[0])
	except Exception as e:
		return jsonify(e)

@app.route('/register', methods=["GET", "POST"])
def register():
	info = [
		"stu_name",
		"stu_id",
		"home",
		"major",
		"email",
		"school",
		"department",
		"experience",
		"rewards",
		"wishes",
	]
	result = []
	for i in info:
		r = request.form.get(i)
		if (r == None or r == ''):
			result.append("No value")
		else:
			result.append(r)
	result = str(result).replace('[','(').replace(']',')')
	print(result)
	sql = "insert into cs_register values %s"%(result)
	print(sql)
	insert_mysql(sql)
	return redirect("/success")

def conn_mysql():
	conn = connect(host='localhost', port=3306, user='root', password='22kon', database='test')
	cur = conn.cursor()
	return conn,cur

def insert_mysql(sql):
	conn,cur = conn_mysql()
	cur.execute(sql)
	conn.commit()

def find_mysql(sql):
	conn,cur = conn_mysql()
	cur.execute(sql)
	data = sql_fetch_json(cur)
	# sql_result = cur.fetchall()
	# result = []
	# for i in sql_result:
	# 	result.append(i)
	return data

def sql_fetch_json(cursor: cursors.Cursor):
    """
    Convert the pymysql SELECT result to json format
    :param cursor:
    :return:
    """
    keys = []
    for column in cursor.description:
        keys.append(column[0])
    key_number = len(keys)

    json_data = []
    for row in cursor.fetchall():
        item = dict()
        for q in range(key_number):
            item[keys[q]] = row[q]
        json_data.append(item)

    return json_data

if __name__ == '__main__':
	app.run()