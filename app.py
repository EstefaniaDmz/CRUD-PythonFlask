from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']=3306
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='agenciaf'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indexHotel')
def indexHotel():
    sql = "SELECT * FROM hotel WHERE estatus=1;"
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)

    hoteles=cursor.fetchall()
    conn.commit()
    return render_template('hoteles/index.html', hoteles=hoteles)

@app.route('/destroyHotel/<int:id>')
def destroyHotel(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("UPDATE hotel SET estatus=0 WHERE idHotel=%s", (id))

    conn.commit()
    return redirect('/indexHotel')

@app.route('/editHotel/<int:id>')
def editHotel(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Hotel WHERE idHotel=%s", (id))
    hotel=cursor.fetchall()
    conn.commit()
    return render_template('hoteles/editar.html', hotel=hotel)

@app.route('/updateHotel', methods=['POST'])
def updateHotel():
    _nombre = request.form['nombre']
    _numeroPlazas = request.form['numeroPlazas']
    _telefono = request.form['telefono']
    _calle = request.form['calle']
    _colonia = request.form['colonia']
    _cp = request.form['cp']
    _ciudad = request.form['ciudad']
    _estado = request.form['estado']
    _pais = request.form['pais']
    id=request.form['idHotel']
    sql = "UPDATE hotel SET nombre=%s, telefono=%s, numeroPlazas=%s, calle=%s, colonia=%s, cp=%s, ciudad=%s, estado=%s, pais=%s WHERE idHotel=%s"
    datos=(_nombre,_telefono,_numeroPlazas,_calle,_colonia,_cp,_ciudad,_estado,_pais,id)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/indexHotel')

@app.route('/crearHotel')
def crearHotel():
    return render_template('hoteles/crear.html')

@app.route('/storeHotel', methods=['POST'])
def storageHotel():
    _nombre = request.form['nombre']
    _numeroPlazas = request.form['numeroPlazas']
    _telefono = request.form['telefono']
    _calle = request.form['calle']
    _colonia = request.form['colonia']
    _cp = request.form['cp']
    _ciudad = request.form['ciudad']
    _estado = request.form['estado']
    _pais = request.form['pais']
    sql = "INSERT INTO hotel(nombre, telefono, numeroPlazas, calle, colonia, cp, ciudad, estado, pais) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    datos=(_nombre,_telefono,_numeroPlazas,_calle,_colonia,_cp,_ciudad,_estado,_pais)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/indexHotel')

@app.route('/indexSucursal')
def indexSucursal():
    sql = "SELECT * FROM Sucursal WHERE estatus=1;"
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)

    sucursales=cursor.fetchall()
    conn.commit()
    return render_template('Sucursales/index.html', sucursales=sucursales)

@app.route('/destroySucursal/<int:id>')
def destroySucursal(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("UPDATE Sucursal SET estatus=0 WHERE idSucursal=%s", (id))

    conn.commit()
    return redirect('/indexSucursal')

@app.route('/editSucursal/<int:id>')
def editSucursal(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Sucursal WHERE idSucursal=%s", (id))
    sucursal=cursor.fetchall()
    conn.commit()
    return render_template('Sucursales/editar.html', sucursal=sucursal)

@app.route('/updateSucursal', methods=['POST'])
def updateSucursal():
    _nombre = request.form['nombre']
    _numeroPlazas = request.form['numeroPlazas']
    _telefono = request.form['telefono']
    _calle = request.form['calle']
    _colonia = request.form['colonia']
    _cp = request.form['cp']
    id=request.form['idSucursal']
    sql = "UPDATE Sucursal SET nombre=%s, telefono=%s, numeroPlazas=%s, calle=%s, colonia=%s, cp=%s WHERE idSucursal=%s"
    datos=(_nombre,_telefono,_numeroPlazas,_calle,_colonia,_cp,id)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/indexSucursal')

@app.route('/crearSucursal')
def crearSucursal():
    return render_template('Sucursales/crear.html')

@app.route('/storeSucursal', methods=['POST'])
def storageSucursal():
    _nombre = request.form['nombre']
    _numeroPlazas = request.form['numeroPlazas']
    _telefono = request.form['telefono']
    _calle = request.form['calle']
    _colonia = request.form['colonia']
    _cp = request.form['cp']
    sql = "INSERT INTO Sucursal(nombre, telefono, numeroPlazas, calle, colonia, cp) VALUES(%s,%s,%s,%s,%s,%s)"
    datos=(_nombre,_telefono,_numeroPlazas,_calle,_colonia,_cp)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/indexSucursal')

@app.route('/indexVuelo')
def indexVuelo():
    sql = "SELECT * FROM Vuelo WHERE estatus=1;"
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)

    vuelos=cursor.fetchall()
    conn.commit()
    return render_template('vuelos/index.html', vuelos=vuelos)

@app.route('/destroyVuelo/<int:id>')
def destroyVuelo(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("UPDATE Vuelo SET estatus=0 WHERE idVuelo=%s", (id))

    conn.commit()
    return redirect('/indexVuelo')

@app.route('/editVuelo/<int:id>')
def editVuelo(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Vuelo WHERE idVuelo=%s", (id))
    vuelo=cursor.fetchall()
    conn.commit()
    return render_template('vuelos/editar.html', vuelo=vuelo)

@app.route('/updateVuelo', methods=['POST'])
def updateVuelo():
    _fecha = request.form['fecha']
    _plazasTotales = request.form['plazasTotales']
    _hora = request.form['hora']
    _ciudadOrigen = request.form['ciudadOrigen']
    _estadoOrigen = request.form['estadoOrigen']
    _paisOrigen = request.form['paisOrigen']
    _ciudadDestino = request.form['ciudadDestino']
    _estadoDestino = request.form['estadoDestino']
    _paisDestino = request.form['paisDestino']
    id=request.form['idVuelo']
    sql = "UPDATE Vuelo SET fecha=%s, hora=%s, plazasTotales=%s, ciudadOrigen=%s, estadoOrigen=%s, paisOrigen=%s, ciudadDestino=%s, estadoDestino=%s, paisDestino=%s WHERE idVuelo=%s"
    datos=(_fecha,_hora,_plazasTotales,_ciudadOrigen,_estadoOrigen,_paisOrigen,_ciudadDestino,_estadoDestino,_paisDestino,id)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/indexVuelo')

@app.route('/crearVuelo')
def crearVuelo():
    return render_template('vuelos/crear.html')

@app.route('/storeVuelo', methods=['POST'])
def storageVuelo():
    _fecha = request.form['fecha']
    _plazasTotales = request.form['plazasTotales']
    _hora = request.form['hora']
    _ciudadOrigen = request.form['ciudadOrigen']
    _estadoOrigen = request.form['estadoOrigen']
    _paisOrigen = request.form['paisOrigen']
    _ciudadDestino = request.form['ciudadDestino']
    _estadoDestino = request.form['estadoDestino']
    _paisDestino = request.form['paisDestino']
    sql = "INSERT INTO Vuelo(fecha, hora, plazasTotales, ciudadOrigen, estadoOrigen, paisOrigen, ciudadDestino, estadoDestino, paisDestino) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    datos=(_fecha,_hora,_plazasTotales,_ciudadOrigen,_estadoOrigen,_paisOrigen,_ciudadDestino,_estadoDestino,_paisDestino)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/indexVuelo')

@app.route('/indexCliente')
def indexCliente():
    sql = "SELECT * FROM Cliente WHERE estatus=1;"
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)

    clientes=cursor.fetchall()
    conn.commit()
    return render_template('clientes/index.html', clientes=clientes)

@app.route('/destroyCliente/<int:id>')
def destroyCliente(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("UPDATE Cliente SET estatus=0 WHERE idCliente=%s", (id))

    conn.commit()
    return redirect('/indexCliente')

@app.route('/editCliente/<int:id>')
def editCliente(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Cliente WHERE idCliente=%s", (id))
    cliente=cursor.fetchall()
    conn.commit()
    return render_template('clientes/editar.html', cliente=cliente)

@app.route('/updateCliente', methods=['POST'])
def updateCliente():
    _nombre = request.form['nombre']
    _apellidoPaterno = request.form['apellidoPaterno']
    _apellidoMaterno = request.form['apellidoMaterno']
    _telefono = request.form['telefono']
    _calle = request.form['calle']
    _colonia = request.form['colonia']
    _cp = request.form['cp']
    _idHotel = request.form['idHotel']
    _regimenHotel = request.form['regimenHotel']
    _idSucursal = request.form['idSucursal']
    _idVuelo = request.form['idVuelo']
    _claseVuelo = request.form['claseVuelo']
    id=request.form['idCliente']
    sql = "UPDATE Cliente SET nombre=%s, telefono=%s, apellidoPaterno=%s, apellidoMaterno=%s, calle=%s, colonia=%s, cp=%s, idHotel=%s, regimenHotel=%s, idSucursal=%s, idVuelo=%s, claseVuelo=%s WHERE idCliente=%s"
    datos=(_nombre,_telefono,_apellidoPaterno,_apellidoMaterno,_calle,_colonia,_cp,_idHotel,_regimenHotel,_idSucursal,_idVuelo,_claseVuelo,id)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/indexCliente')

@app.route('/crearCliente')
def crearCliente():
    return render_template('clientes/crear.html')

@app.route('/storeCliente', methods=['POST'])
def storageCliente():
    _nombre = request.form['nombre']
    _apellidoPaterno = request.form['apellidoPaterno']
    _apellidoMaterno = request.form['apellidoMaterno']
    _telefono = request.form['telefono']
    _calle = request.form['calle']
    _colonia = request.form['colonia']
    _cp = request.form['cp']
    _idHotel = request.form['idHotel']
    _regimenHotel = request.form['regimenHotel']
    _idSucursal = request.form['idSucursal']
    _idVuelo = request.form['idVuelo']
    _claseVuelo = request.form['claseVuelo']
    sql = "INSERT INTO Cliente(nombre, telefono, apellidoPaterno, apellidoMaterno, calle, colonia, cp, idHotel, regimenHotel, idSucursal, idVuelo, claseVuelo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    datos=(_nombre,_telefono,_apellidoPaterno,_apellidoMaterno,_calle,_colonia,_cp,_idHotel,_regimenHotel,_idSucursal,_idVuelo,_claseVuelo)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/indexCliente')

if __name__ == '__main__':
    app.run(debug=True)