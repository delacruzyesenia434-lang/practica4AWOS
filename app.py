from flask import Flask, render_template, request, jsonify, make_response, session

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/ingredientes')
def ingredientes():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005299_usr",
        password="!4V2rHq@rQh",
        database="u760464709_24005299_bd"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ingredientes")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))

@app.post('/ingrediente')
def ingrediente():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005299_usr",
        password="!4V2rHq@rQh",
        database="u760464709_24005299_bd"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO ingredientes (nombre) VALUES (%s)"
    val = (request.form['txtNombre'],)
    mycursor.execute(sql, val)
    mydb.commit()
    return "correcto"
