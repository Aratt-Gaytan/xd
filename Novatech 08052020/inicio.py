import pymysql
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/nvo_nivel')
def nvo_nivel():
    return render_template("agr_nivel.html")


@app.route('/nivelacademico')
def nivelacademico():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idNivelAcademico, descripcion from nivelacademico order by descripcion')
    datos = cursor.fetchall()
    return render_template("Nivel_Academico.html", niveles=datos)


@app.route('/agrega_nivel', methods=['POST'])
def agrega_nivel():
    if request.method == 'POST':
        aux_descripcion = request.form['descripcion']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into nivelacademico (Descripcion) values (%s)', (aux_descripcion))
        conn.commit()
    return redirect(url_for('nivelacademico'))


@app.route('/ed_nivel/<string:id>')
def ed_nivel(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idNivelAcademico, descripcion from nivelacademico where idNivelAcademico = %s', (id))
    dato = cursor.fetchall()
    return render_template("edi_nivel.html", nivel=dato[0])


@app.route('/modifica_nivel/<string:id>', methods=['POST'])
def modifica_nivel(id):
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('update nivelacademico set  descripcion=%s where idNivelAcademico= %s', (descrip, id))
        conn.commit()
    return redirect(url_for('nivelacademico'))


@app.route('/bo_nivel/<string:id>')
def bo_nivel(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete  from nivelacademico where idNivelAcademico = %s', (id))
    conn.commit()
    return redirect(url_for('nivelacademico'))


@app.route("/nvo_habilidad")
def nvo_habilidad():
    return render_template("Habilidad.html")


@app.route("/agrega_habilidad", methods=["POST"])
def agrega_habilidad():
    if request.method == 'POST':
        aux_descripcion = request.form['Descripcion']

        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into habilidad (Descripcion ) values (%s)', (aux_descripcion))
        conn.commit()
    return redirect(url_for('sel_habilidades'))


@app.route('/habilidad')
def sel_habilidades():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad,Descripcion from habilidad order by descripcion')
    datos = cursor.fetchall()
    return render_template("tabla.html", habilidades=datos)


@app.route('/ed_habilidad/<string:id>')
def ed_habilidad(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad,Descripcion  from habilidad where idHabilidad = %s', (id))
    dato = cursor.fetchall()

    return render_template("editar_habilidad.html", habilidad=dato)


@app.route('/modifica_habilidad/<string:id>', methods=['POST'])
def modifica_habilidad(id):
    if request.method == 'POST':
        aux_descripcion = request.form['descripcion']

        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('update habilidad set Descripcion=%s where idHabilidad=%s',
                       (aux_descripcion, id))
        conn.commit()
    return redirect(url_for('sel_habilidades'))


@app.route('/borrar_habilidad/<string:id>')
def borrar_habilidad(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from habilidad where idHabilidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('sel_habilidades'))


@app.route('/nva_carrera')
def nva_carrera():
    return render_template("agr_carrera.html")


@app.route('/carrera')
def carrera():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera order by descripcion')
    datos = cursor.fetchall()
    return render_template("Carrera.html", niveles=datos)


@app.route('/agr_carrera', methods=['POST'])
def agrega_carrera():
    if request.method == 'POST':
        aux_descripcion = request.form['descripcion']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into carrera (Descripcion) values (%s)', (aux_descripcion))
        conn.commit()
    return redirect(url_for('carrera'))


@app.route('/ed_carrera/<string:id>')
def ed_carrera(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera where idCarrera = %s', (id))
    dato = cursor.fetchall()
    return render_template("edi_carrera.html", nivel=dato[0])


@app.route('/modifica_carrera/<string:id>', methods=['POST'])
def modifica_carrera(id):
    if request.method == 'POST':
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('update carrera set  descripcion=%s where idCarrera=%s', (descrip, id))
        conn.commit()
    return redirect(url_for('carrera'))


@app.route('/bo_carrera/<string:id>')
def bo_carrera(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from carrera where idCarrera = {0}'.format(id))
    conn.commit()
    return redirect(url_for('carrera'))


@app.route("/idioma")
def idioma():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        'select * from idioma order by Lenguaje')
    datos = cursor.fetchall()
    return render_template("idioma.html", datos=datos)


@app.route("/nvo_idioma")
def nvo_idioma():
    return render_template("agr_idioma.html")


@app.route('/ed_idioma/<string:id>')
def edi_idioma(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()

    cursor.execute(
        'select Lenguaje from idioma WHERE ididioma = %s', (id))
    idiomas = cursor.fetchall()
    print(idiomas)
    return render_template('edi_idioma.html', idiomas=idiomas, dato=id)


@app.route('/edita_idioma/<string:id>', methods=["post"])
def edita_idioma(id):
    if request.method == 'POST':
        aux_descripcion = request.form['lenguaje']

        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')

        cursor = conn.cursor()

        cursor.execute("""  UPDATE idioma SET lenguaje = %s  WHERE ididioma = %s;  """,
                       (aux_descripcion, id))
        conn.commit()
    return redirect(url_for("idioma"))


@app.route("/bo_idioma/<string:id>")
def bo_idioma(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM idioma WHERE ididioma = %s;""", (id))
    conn.commit()
    return redirect(url_for("idioma"))


@app.route("/agrega_idioma", methods=["POST"])
def agrega_idioma():
    if request.method == 'POST':
        nombre = request.form['lenguaje']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO   idioma (Lenguaje) VALUES (%s);''', (nombre))
        conn.commit()
    return redirect(url_for('idioma'))


@app.route('/estado civil')
def estado_civil():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        'select idEstadoCivil, Descripcion from estadocivil order by descripcion')
    datos = cursor.fetchall()
    return render_template("estado civil.html", datos=datos)


@app.route('/nvo_estadocivil')
def nvoestadocivil():
    return render_template('agrega_estadociv.html')


@app.route('/agr_estadociv', methods=["POST"])
def agr_estado_civ():
    if request.method == 'POST':
        aux_descripcion = request.form['descripcion']
        # print(aux_descripcion)
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()

        cursor.execute('''insert into estadocivil ( Descripcion) values (%s)''',
                       (aux_descripcion))
        conn.commit()
    return redirect(url_for("estado_civil"))


@app.route('/ed_estadociv/<string:id>')
def edi_estadociv(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        'select Descripcion from estadocivil where idEstadoCivil = %s', (id))
    des = cursor.fetchall()
    return render_template('editar_estadociv.html', des=des, dato=id)


@app.route('/edita_estadociv/<string:id>', methods=["post"])
def edita_estadociv(id):
    if request.method == 'POST':
        aux_descripcion = request.form['descripcion']

        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()

        cursor.execute("""  UPDATE estadocivil SET Descripcion = %s WHERE idEstadoCivil = %s;  """,
                       (aux_descripcion, id))
        conn.commit()
    return redirect(url_for("estado_civil"))


@app.route('/bo_estadociv/<string:id>')
def borra_estadociv(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM estadocivil WHERE idEstadoCivil = %s;""", (id))
    conn.commit()
    return redirect(url_for("estado_civil"))


@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        'select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion from puesto order by Descripcion')

    datos = cursor.fetchall()
    return render_template("puesto.html", puestos=datos)


@app.route("/agregar_puesto")
def agregar_puesto():
    return render_template("agr_puesto.html")


@app.route('/agrega_puesto', methods=["POST"])
def agrega_puesto():
    if request.method == 'POST':
        aux_des = request.form['descripcion']
        aux_sal = request.form['salario']
        aux_ben = request.form['beneficios']
        aux_bon = request.form['bonos']
        aux_aut = request.form['autorizar']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute(
            'insert into puesto (Descripcion, SalarioAnual, Beneficios, Bonos,  Aprobacion) values (%s,%s,%s,%s,%s)',
            (aux_des, aux_sal, aux_ben, aux_bon, aux_aut))
        conn.commit()
        cursor.execute(
            'select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos,Aprobacion from puesto where idPuesto=(select max(idPuesto) from puesto)')
        datos = cursor.fetchall()
        cursor.execute('select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto, c.idHabilidad, c.Experiencia '
                       ' from puesto a, habilidad b,puesto_has_habilidad c '
                       ' where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=(select max(idPuesto) from puesto)')
        datos1 = cursor.fetchall()
        cursor.execute('select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel '
                       'from puesto a, idioma b,puesto_has_idioma c '
                       'where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=(select max(idPuesto) from puesto)')
        datos2 = cursor.fetchall()
        cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()
        cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()
        return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1, pue_idis=datos2, habs=datos3,
                               idiomas=datos4)


@app.route('/modifica_puesto/<string:id>', methods=['POST'])
def modifica_puesto(id):
    if request.method == 'POST':
        aux_des = request.form['descripcion']
        aux_sal = request.form['salario']
        aux_ben = request.form['beneficios']
        aux_bon = request.form['bonos']
        aux_aut = request.form['autorizar']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute(
            'update puesto set Descripcion=%s, SalarioAnual=%s,Beneficios=%s, Bonos=%s, Aprobacion=%s where idpuesto=%s',
            (aux_des, aux_sal, aux_ben, aux_bon, aux_aut, id))

        conn.commit()
    return redirect(url_for('puesto'))


@app.route('/ed_puesto/<string:id>')
def ed_puesto(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion '
                   'from puesto where idPuesto=%s', (id))
    datos = cursor.fetchall()
    cursor.execute(
        'select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto, c.idHabilidad,c.Experiencia  from puesto a, habilidad b,puesto_has_habilidad c  where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s',
        (id))
    datos1 = cursor.fetchall()
    cursor.execute(
        'select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel from puesto a, idioma b,puesto_has_idioma c where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s',
        (id))

    datos2 = cursor.fetchall()
    cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()
    cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()
    return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1,
                           pue_idis=datos2, habs=datos3, idiomas=datos4)


@app.route('/bo_puesto/<string:id>')
def bo_puesto(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from puesto_has_idioma where idPuesto = {0}'.format(id))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto = {0}'.format(id))
    conn.commit()
    cursor.execute('delete from puesto where idPuesto = {0}'.format(id))
    conn.commit()
    return redirect(url_for('puesto'))


@app.route('/agrega_hab_pto', methods=['POST'])
def agrega_hab_pto():
    if request.method == 'POST':
        aux_pto = request.form['pto']
        aux_hab = request.form['habil']
        aux_exp = request.form['expe']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into puesto_has_habilidad (idPuesto, idHabilidad,Experiencia) values (%s,%s,%s)',
                       (aux_pto, aux_hab, aux_exp))
        conn.commit()
        cursor.execute(
            'select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos,Aprobacion from puesto where idPuesto=%s',
            (aux_pto))
        datos = cursor.fetchall()
        cursor.execute(
            'select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto,c.idHabilidad, c.Experiencia from puesto a, habilidad b,puesto_has_habilidad c  where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s',
            (aux_pto))
        datos1 = cursor.fetchall()
        cursor.execute(
            'select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma,c.Nivel from puesto a, idioma b,puesto_has_idioma c where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s',
            (aux_pto))
        datos2 = cursor.fetchall()
        cursor.execute('select idhabilidad, Descripcion from habilidad order by  Descripcion')

        datos3 = cursor.fetchall()
        cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()
        return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1, pue_idis=datos2, habs=datos3,
                               idiomas=datos4)


@app.route('/agrega_idio_pto', methods=['POST'])
def agrega_idio_pto():
    if request.method == 'POST':
        aux_pto = request.form['ptoi']
        aux_idi = request.form['idio']
        aux_niv = request.form['nive']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO `puesto_has_idioma` (`idPuesto`, `idIdioma`, `Nivel`) values(%s,%s,%s)',
                       (aux_pto, aux_idi, aux_niv))
        conn.commit()
        cursor.execute(
            'select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos,Aprobacion from puesto where idPuesto=%s',
            (aux_pto))
        datos = cursor.fetchall()
        cursor.execute(
            'select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto,c.idHabilidad, c.Experiencia  from puesto a, habilidad b,puesto_has_habilidad c  where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s',
            (aux_pto))
        datos1 = cursor.fetchall()
        cursor.execute(
            'select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma,c.Nivel from puesto a, idioma b,puesto_has_idioma c where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s',
            (aux_pto))
        datos2 = cursor.fetchall()
        cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()
        cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()
        return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1, pue_idis=datos2, habs=datos3,
                               idiomas=datos4)


@app.route('/bo_hab_pto/<string:idP>/<string:idH>')
def bo_hab_pto(idP, idH):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s and idHabilidad=%s', (idP, idH))
    conn.commit()
    cursor.execute(
        'select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion from puesto where idPuesto=%s',
        (idP))
    datos = cursor.fetchall()
    cursor.execute(
        'select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto, c.idHabilidad,c.Experiencia  from puesto a, habilidad b,puesto_has_habilidad c  where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s',
        (idP))
    datos1 = cursor.fetchall()
    cursor.execute(
        'select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel from puesto a, idioma b,puesto_has_idioma c where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s',
        (idP))
    datos2 = cursor.fetchall()
    cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()
    cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()
    return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1, pue_idis=datos2, habs=datos3,
                           idiomas=datos4)


@app.route('/bo_idi_pto/<string:idP>/<string:idI>')
def bo_idi_pto(idP, idI):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s and idIdioma=%s', (idP, idI))
    conn.commit()
    cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion '
                   'from puesto where idPuesto=%s', (idP))
    datos = cursor.fetchall()
    cursor.execute(
        'select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto, c.idHabilidad, c.Experiencia  from puesto a, habilidad b,puesto_has_habilidad c where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s',
        (idP))
    datos1 = cursor.fetchall()
    cursor.execute(
        'select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel from puesto a, idioma b,puesto_has_idioma c where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s',
        (idP))
    datos2 = cursor.fetchall()
    cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()
    cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()
    return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1, pue_idis=datos2, habs=datos3,
                           idiomas=datos4)



@app.route('/nvo_area')
def nvo_area():
    return render_template("agr_area.html")


@app.route('/area')
def area():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idArea, AreaNombre, AreaDescripcion from area order by AreaDescripcion')
    datos = cursor.fetchall()
    return render_template("area.html", areas=datos)


@app.route('/agrega_area', methods=['POST'])
def agrega_area():
    if request.method == 'POST':
        aux_Nombre = request.form['nombre']
        aux_Descripcion = request.form['descripcion']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into area (AreaNombre,AreaDescripcion) values (%s,%s)', (aux_Nombre, aux_Descripcion))
        conn.commit()
    return redirect(url_for('area'))


@app.route('/edita_area/<string:id>')
def edita_area(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idArea, AreaNombre, AreaDescripcion from area where idArea = %s', (id))
    dato = cursor.fetchall()
    return render_template("edi_area.html", area=dato[0])


@app.route('/modifica_area/<string:id>', methods=['POST'])
def modifica_area(id):
    if request.method == 'POST':
        nombr = request.form['nombre']
        descrip = request.form['descripcion']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('update area set  AreaNombre=%s,AreaDescripcion=%s where idArea=%s', (nombr, descrip, id))
        conn.commit()
    return redirect(url_for('area'))


@app.route('/borrar_area/<string:id>')
def borrar_area(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))


@app.route('/medio_publicidad')
def medio_publicidadl():
    return render_template("Medio de publicidad.html")


@app.route('/medio de publicidad')
def tabla_medio():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idMedioPublicidad,Descripcion from mediopublicidad order by descripcion')
    datos = cursor.fetchall()
    return render_template("tabla_publicidad.html", medios=datos)


@app.route("/agrega_medio_publicidad", methods=["POST"])
def agrega_medio_publicidad():
    if request.method == 'POST':
        aux_descripcion = request.form['des_publicidad']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into mediopublicidad (Descripcion) values (%s)', (aux_descripcion))
        conn.commit()
    return tabla_medio()


@app.route('/ed_medio/<string:id>')
def ed_medio(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idMedioPublicidad,Descripcion from mediopublicidad where idMedioPublicidad = %s', (id))
    dato = cursor.fetchall()
    return render_template("editar_medio.html", medio=dato[0])


@app.route('/modifica_medio/<string:id>', methods=['POST'])
def modifica_medio(id):
    if request.method == 'POST':
        aux_descripcion = request.form['des_publicidad']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('update mediopublicidad set Descripcion=%s where idMedioPublicidad=%s', (aux_descripcion, id))
        conn.commit()
    return redirect(url_for("tabla_medio"))


@app.route('/borrar_medio/<string:id>')
def borrar_medio(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from mediopublicidad where idMedioPublicidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for("tabla_medio"))


@app.route('/nvo_contacto')
def nvo_contacto():
    return render_template("agr_contacto.html")


@app.route('/contacto')
def contacto():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idcontacto, Nombre, Domicilio, Razon_Social,Telefono from contacto  order by Nombre')
    dato = cursor.fetchall()
    # print(dato)
    return render_template("Contacto.html", niveles=dato)


@app.route("/agrega_contacto", methods=["POST"])
def agrega_contacto():
    if request.method == 'POST':
        aux_nombre = request.form['Nombre']
        aux_domicilio = request.form['domicilio']
        aux_razon = request.form['razonsocial']
        aux_numero = request.form['Numero']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into contacto (Nombre, Domicilio, Razon_Social,Telefono) values (%s,%s,%s,%s)',
                       (aux_nombre, aux_domicilio, aux_razon, aux_numero))
        conn.commit()
    return redirect(url_for('contacto'))


@app.route('/ed_contacto/<string:id>')
def ed_contacto(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idcontacto, Nombre, Domicilio, Razon_Social,Telefono from contacto where idContacto = %s',
                   (id))
    dato = cursor.fetchall()
    return render_template("edi_contacto.html", niveles=dato, id=id)


@app.route('/modifica_contacto/<string:id>', methods=['POST'])
def modifica_contacto(id):
    if request.method == 'POST':
        descrip = request.form['Nombre']
        domic = request.form['domicilio']
        razsoc = request.form['razonsocial']
        num = request.form['Numero']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('update contacto set  Nombre=%s,Domicilio=%s,Razon_Social=%s,Telefono=%s where idContacto=%s',
                       (descrip, domic, razsoc, num, id))
        conn.commit()
    return redirect(url_for('contacto'))


@app.route('/bo_contacto/<string:id>')
def bo_contacto(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from contacto where idcontacto = {0}'.format(id))
    conn.commit()
    return redirect(url_for('contacto'))


@app.route('/datos de empresa')
def datos():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        'select Nombre_de_empresa, Descripcion,Estructura_Juridica,Razonsocial,E_mail,Domicilio,Telefono,Encargado,CIF_empresa from datos_de_empresa')
    datos = cursor.fetchall()
    return render_template("Datos.html", niveles=datos)


@app.route('/Datos_empresa')
def Datos_empresa():
    return render_template("Datos_empresa.html")


@app.route('/modifica_datos/<string:id>', methods=['POST'])
def modifica_datos(id):
    if request.method == 'POST':
        nom = request.form['Nombre_de_empresa']
        des = request.form['Descripcion']
        est = request.form['Estructura_Juridica']
        raz = request.form['Razon_social']
        ema = request.form['Email']
        dom = request.form['Domicilio']
        tel = request.form['Telefono']
        enc = request.form['Encargado']

        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute(
            'update datos_de_empresa set Nombre_de_empresa=%s, Descripcion=%s, Estructura_juridica=%s ,Razonsocial=%s, E_mail=%s, Domicilio=%s, Telefono=%s, Encargado=%s  where Nombre_de_empresa= %s ',
            (nom, des, est, raz, ema, dom, tel, enc, id))
        conn.commit()
    return redirect(url_for('datos'))


@app.route('/ed_datos/<string:id>')
def edi_datos(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        'select Nombre_de_empresa from datos_de_empresa where Nombre_de_empresa = %s', (id))
    nom = cursor.fetchall()
    cursor.execute(
        'select Descripcion from datos_de_empresa ')
    des = cursor.fetchall()
    cursor.execute(
        'select Estructura_Juridica from datos_de_empresa ')
    est = cursor.fetchall()
    cursor.execute(
        'select Razonsocial from datos_de_empresa')
    raz = cursor.fetchall()
    cursor.execute(
        'select E_mail from datos_de_empresa')
    ema = cursor.fetchall()
    cursor.execute(
        'select Domicilio from datos_de_empresa')
    dom = cursor.fetchall()
    cursor.execute(
        'select Telefono from datos_de_empresa')
    tel = cursor.fetchall()
    cursor.execute(
        'select Encargado from datos_de_empresa')
    enc = cursor.fetchall()
    cursor.execute(
        'select CIF_empresa from datos_de_empresa')
    cif = cursor.fetchall()
    return render_template('edita_empresa.html', nom=nom, des=des, est=est, raz=raz, ema=ema, dom=dom, tel=tel, enc=enc,
                           cif=cif, dato=id)


@app.route('/borrar_datosempresa/<string:id>')
def borrar_datosempresa(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from datos_de_empresa where Nombre_de_empresa = %s', (id))
    conn.commit()
    return redirect(url_for('datos'))


@app.route("/solicitud")
def solicitud():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('''select a.idSolicitud,a.FechaSolicitud,a.NumeroVacante,a.idArea,b.AreaDescripcion,a.idPuesto,c.Descripcion,a.idNivelAcademico,d.Descripcion,a.idCarrera,e.Descripcion,a.idEstatus_Solicitud,f.Descripcion
        from solicitud a, area b, puesto c, nivelacademico d , carrera e,  estatus_solicitud f
        where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idNivelAcademico=a.idNivelAcademico and f.idEstatus_Solicitud=a.idEstatus_Solicitud and a.idCarrera=e.idCarrera order by a.idEstatus_Solicitud''')
    datos = cursor.fetchall()
    print(datos)
    return render_template('solicitud.html', datos=datos)


@app.route("/nvo_solicitud")
def nvo_solicitud():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select idArea, AreaDescripcion from area')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto, Descripcion from puesto')
    datos1 = cursor.fetchall()
    cursor.execute('select idCarrera, Descripcion from carrera')
    datos2 = cursor.fetchall()
    cursor.execute('select idNivelAcademico, Descripcion from nivelacademico')
    datos3 = cursor.fetchall()
    return render_template("agr_solicitud.html", areas=datos, puestos=datos1, carreras=datos2, niveles=datos3)


@app.route("/agr_solicitud", methods=["POST"])
def agrega_solicitud():
    if request.method == 'POST':

        aux_fecha = request.form['Fecha']
        aux_area = request.form['area']
        aux_puesto = request.form['puesto']
        aux_carrera = request.form['Carrera']
        aux_vacantes = request.form['vacantes']
        aux_nivel = request.form['nivel']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('select Aprobacion from puesto where idPuesto = %s;', (aux_puesto))
        auto = cursor.fetchone()
        print(auto)
        if auto[0] == 0:
            cursor.execute(
                'insert into solicitud (FechaSolicitud,NumeroVacante,idArea,idPuesto,idNivelAcademico,idCarrera,idEstatus_Solicitud) values (%s,%s,%s,%s,%s,%s,1)',
                (aux_fecha, aux_vacantes, aux_area, aux_puesto, aux_nivel, aux_carrera))
            conn.commit()
        else:
            cursor.execute(
                'insert into solicitud (FechaSolicitud,NumeroVacante,idArea,idPuesto,idNivelAcademico,idCarrera,idEstatus_Solicitud) values (%s,%s,%s,%s,%s,%s,2)',
                (aux_fecha, aux_vacantes, aux_area, aux_puesto, aux_nivel, aux_carrera))
            conn.commit()
    return redirect(url_for('solicitud'))


@app.route("/ed_solicitud/<string:id>")
def ed_solicitud(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select *from solicitud where idSolicitud=%s', (id))
    datos4 = cursor.fetchall()

    cursor.execute('select idArea, AreaDescripcion from area')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto, Descripcion from puesto')
    datos1 = cursor.fetchall()
    cursor.execute('select idCarrera, Descripcion from carrera')
    datos2 = cursor.fetchall()
    cursor.execute('select idNivelAcademico, Descripcion from nivelacademico')
    datos3 = cursor.fetchall()
    cursor.execute('select idEstatus_Solicitud, Descripcion from estatus_solicitud')
    datos5 = cursor.fetchall()

    return render_template("edi_solicitud.html", areas=datos, puestos=datos1, carreras=datos2, niveles=datos3,
                           solicitud=datos4, estatuses=datos5)


@app.route("/edita_solicitud/<string:id>", methods=["POST"])
def edita_solicitud(id):
    if request.method == 'POST':
        aux_fecha = request.form['Fecha']
        aux_area = request.form['area']
        aux_puesto = request.form['puesto']
        aux_carrera = request.form['Carrera']
        aux_vacantes = request.form['vacantes']
        aux_nivel = request.form['nivel']
        aux_estatus = request.form['estatus']

        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute(
            '''update solicitud set FechaSolicitud=%s,NumeroVacante=%s,idArea=%s,idPuesto=%s,idNivelAcademico=%s,idCarrera=%s,idEstatus_Solicitud=%s where idSolicitud=%s ''',
            (aux_fecha, aux_vacantes, aux_area, aux_puesto, aux_nivel, aux_carrera, aux_estatus, id))
        conn.commit()
    return redirect(url_for('solicitud'))


@app.route("/bo_solicitud/<string:id>")
def borra_solicitud(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from solicitud where idSolicitud=%s', (id))
    conn.commit()
    return redirect(url_for("solicitud"))


@app.route("/faltante")
def faltante():
    return render_template("faltante.html")


@app.route("/Autorizacion")
def Autorizacion():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('''select a.idSolicitud,a.FechaSolicitud,a.NumeroVacante,a.idArea,b.AreaDescripcion,a.idPuesto,c.Descripcion,a.idNivelAcademico,d.Descripcion,a.idCarrera,e.Descripcion,a.idEstatus_Solicitud,f.Descripcion
        from solicitud a, area b, puesto c, nivelacademico d , carrera e,  estatus_solicitud f
        where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idNivelAcademico=a.idNivelAcademico and f.idEstatus_Solicitud=a.idEstatus_Solicitud and a.idCarrera=e.idCarrera order by a.idEstatus_Solicitud''')
    datos = cursor.fetchall()

    return render_template("autoriza.html", datos=datos)


@app.route("/auto_solicitud/<string:id>")
def auto_solicitud(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(''' update solicitud set idEstatus_solicitud=2 where idSolicitud=%s''', (id))
    conn.commit()

    return redirect(url_for('Autorizacion'))


@app.route("/can_solicitud/<string:id>")
def can_solicitud(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(''' update solicitud set idEstatus_solicitud=6 where idSolicitud=%s''', (id))
    conn.commit()
    return redirect(url_for('Autorizacion'))

    ### PUBLICACIÓN DE LA SOLICITUD


@app.route('/a_publicar')
def a_publicar():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud'
        ' and (a.idEstatus_Solicitud=2 or a.idEstatus_Solicitud=3) order by a.idEstatus_Solicitud')

    datos = cursor.fetchall()
    return render_template("publicacion.html", solicitudes=datos)


@app.route('/crea_pub/<string:id>')
def crea_pub(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud'
        ' and (a.idEstatus_Solicitud=2 or a.idEstatus_Solicitud=3) and idSolicitud=%s', (id))

    dato = cursor.fetchone()
    cursor.execute(
        ' SELECT a.idAnuncio, a.Num_Solicitantes, a.FechaPublicacion, a.FechaCierre, b.Nombre, c.Descripcion '
        ' from anuncio a, contacto b, mediopublicidad c '
        ' where b.idcontacto=a.idcontacto and c.idMedioPublicidad=a.idMedioPublicidad and a.idSolicitud=%s', (id))
    datos = cursor.fetchall()

    cursor.execute(' select idcontacto, nombre from contacto order by nombre ')
    datos1 = cursor.fetchall()
    cursor.execute(' select idMedioPublicidad, Descripcion from mediopublicidad order by Descripcion ')
    datos2 = cursor.fetchall()
    return render_template("crea_publicacion.html", sol=dato, publicaciones=datos, contactos=datos1, medios=datos2)


@app.route('/agrega_publicacion', methods=['POST'])
def agrega_publicacion():
    if request.method == 'POST':
        aux_sol = request.form['n_solicitud']
        aux_fep = request.form['fecha_pub']
        aux_fec = request.form['fecha_cie']
        aux_solicitantes = request.form['n_solicitantes']
        aux_con = request.form['contacto']
        aux_med = request.form['medio']

        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()

        # El Puesto requiere de Autorizacion
        cursor.execute(
            ' insert into anuncio (idSolicitud, Num_Solicitantes, FechaPublicacion, FechaCierre, idcontacto, idMedioPublicidad) '
            ' values (%s,%s,%s,%s,%s,%s)', (aux_sol, aux_solicitantes, aux_fep, aux_fec, aux_con, aux_med))
        conn.commit()
        cursor.execute(' update solicitud set idEstatus_Solicitud=3 where idSolicitud=%s', (aux_sol))
        conn.commit()
        cursor.execute(
            ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
            ' from solicitud a, area b, puesto c, estatus_solicitud d '
            ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud'
            ' and (a.idEstatus_Solicitud=2 or a.idEstatus_Solicitud=3) and idSolicitud=%s', (aux_sol))

        dato = cursor.fetchone()
        cursor.execute(
            ' SELECT a.idAnuncio, a.Num_Solicitantes, a.FechaPublicacion, a.FechaCierre, b.Nombre, c.Descripcion '
            ' from anuncio a, contacto b, mediopublicidad c '
            ' where b.idcontacto=a.idcontacto and c.idMedioPublicidad=a.idMedioPublicidad and a.idSolicitud=%s',
            (aux_sol))
        datos = cursor.fetchall()

        cursor.execute(' select idcontacto, nombre from contacto order by nombre ')
        datos1 = cursor.fetchall()
        cursor.execute(' select idMedioPublicidad, Descripcion from mediopublicidad order by Descripcion ')
        datos2 = cursor.fetchall()
        return render_template("crea_publicacion.html", sol=dato, publicaciones=datos, contactos=datos1, medios=datos2)


@app.route('/bo_publicacion/<string:id>')
def bo_publicacion(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(' select idSolicitud from anuncio where idanuncio = {0}'.format(id))
    aux_sol = cursor.fetchone()
    cursor = conn.cursor()
    cursor.execute(' delete from anuncio where idanuncio = {0}'.format(id))
    conn.commit()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud'
        ' and (a.idEstatus_Solicitud=2 or a.idEstatus_Solicitud=3) and idSolicitud=%s', (aux_sol[0]))

    dato = cursor.fetchone()
    cursor.execute(
        ' SELECT a.idAnuncio, a.Num_Solicitantes, a.FechaPublicacion, a.FechaCierre, b.Nombre, c.Descripcion '
        ' from anuncio a, contacto b, mediopublicidad c '
        ' where b.idcontacto=a.idcontacto and c.idMedioPublicidad=a.idMedioPublicidad and a.idSolicitud=%s',
        (aux_sol[0]))
    datos = cursor.fetchall()

    cursor.execute(' select idcontacto, nombre from contacto order by nombre ')
    datos1 = cursor.fetchall()
    cursor.execute(' select idMedioPublicidad, Descripcion from mediopublicidad order by Descripcion ')
    datos2 = cursor.fetchall()
    return render_template("crea_publicacion.html", sol=dato, publicaciones=datos, contactos=datos1, medios=datos2)


@app.route("/candidato")
def candidato():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(' select CURP,RFC, Domicilio, E_mail,  Sexo, Edad from candidato order by CURP')
    datos = cursor.fetchall()

    return render_template("candidato.html", candidatos=datos)


@app.route("/agregar_candidato")
def agregar_candidato():
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('select * from estadocivil order by Descripcion')
    datos = cursor.fetchall()
    return render_template("agr_candidato.html", datos=datos)


@app.route("/agrega_candidato", methods=["POST"])
def agrega_candidato():
    if request.method == 'POST':
        aux_curp = request.form['curp']
        aux_nombre = request.form['nombre']
        aux_rfc = request.form['rfc']
        aux_telefono = request.form['telefono']
        aux_domicilio = request.form['domicilio']
        aux_nss = request.form['nss']
        aux_edad = request.form['edad']
        aux_sexo = request.form['sexo']
        aux_estadociv = request.form['estadoc']
        aux_email = request.form['email']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('''insert into candidato(CURP,RFC, Nombre,Domicilio, Telefono,E_mail,
            Sexo,Edad,NSS,idEstadoCivil) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                       (aux_curp, aux_rfc, aux_nombre, aux_domicilio,
                        aux_telefono, aux_email, aux_sexo, aux_edad, aux_nss, aux_estadociv))
        conn.commit()
        cursor.execute(
            ' select CURP,RFC, Nombre,Domicilio, Telefono,E_mail, Sexo,Edad,NSS,idEstadoCivil from candidato where CURP=%s',
            (aux_curp))
        datos = cursor.fetchall()
        cursor.execute(' select * from habilidad ')
        datos1 = cursor.fetchall()
        cursor.execute(' select * from idioma ')
        datos2 = cursor.fetchall()
       
        datos3 = cursor.fetchall()
        cursor.execute(' select * from nivelacademico ')
        datos4 = cursor.fetchall()
        cursor.execute('select a.CURP, b.idIdioma,b.Lenguaje,c.CURP, c.idIdioma, c.Nivel '
                       'from candidato a, idioma b,candidato_has_idioma c '
                       'where a.CURP=c.CURP and b.idIdioma=c.idIdioma and a.CURP=%s ', (aux_curp))
        datos5 = cursor.fetchall()
        cursor.execute('select a.CURP, b.idHabilidad,b.Descripcion,c.CURP, c.idHabilidad, c.Experiencia '
                       'from candidato a, habilidad b,candidato_has_habilidad c '
                       'where a.CURP=c.CURP and b.idHabilidad=c.idHabilidad and a.CURP=%s ', (aux_curp))
        datos6 = cursor.fetchall()
        cursor.execute('select * from estadocivil order by Descripcion')
        datos7 = cursor.fetchall()
        
        cursor.execute(
            'select a.CURP, b.idNivelAcademico,b.Descripcion,c.Institucion,c.CURP, c.idNivelAcademico,c.idCarrera ,d.Descripcion '
            'from candidato a, nivelacademico b,candidato_has_nivelacademico c, carrera d '
            ' where a.CURP=c.CURP and b.idNivelAcademico=c.idNivelacademico and c.idCarrera = d.idCarrera and a.CURP=%s ',
            (aux_curp))
        datos9 = cursor.fetchall()
        cursor.execute('select * from carrera order by Descripcion')
        datos10 = cursor.fetchall()
        return render_template("edi_candidato.html", datos=datos, habs=datos1, idiomas=datos2, 
                               niveles=datos4, idis=datos5, can_habs=datos6, estados=datos7,
                               nivelesC=datos9, carrerasN=datos10)


@app.route("/ed_candidato/<string:id>")
def ed_candidato(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute(
        ' select CURP,RFC, Nombre,Domicilio, Telefono,E_mail, Sexo,Edad,NSS,Fotografia,idEstadoCivil from candidato where CURP=%s',
        (id))
    datos = cursor.fetchall()
    cursor.execute(' select * from habilidad ')
    datos1 = cursor.fetchall()
    cursor.execute(' select * from idioma ')
    datos2 = cursor.fetchall()
    
    cursor.execute(' select * from nivelacademico ')
    datos4 = cursor.fetchall()
    cursor.execute('select a.CURP, b.idIdioma,b.Lenguaje,c.CURP, c.idIdioma, c.Nivel '
                   'from candidato a, idioma b,candidato_has_idioma c '
                   'where a.CURP=c.CURP and b.idIdioma=c.idIdioma and a.CURP=%s ', (id))
    datos5 = cursor.fetchall()
    cursor.execute('select a.CURP, b.idHabilidad,b.Descripcion,c.CURP, c.idHabilidad, c.Experiencia '
                   'from candidato a, habilidad b,candidato_has_habilidad c '
                   'where a.CURP=c.CURP and b.idHabilidad=c.idHabilidad and a.CURP=%s ', (id))
    datos6 = cursor.fetchall()
    cursor.execute('select * from estadocivil order by Descripcion')
    datos7 = cursor.fetchall()

    cursor.execute(
        'select a.CURP, b.idNivelAcademico,b.Descripcion,c.Institucion,c.CURP, c.idNivelAcademico,c.idCarrera ,d.Descripcion '
        'from candidato a, nivelacademico b,candidato_has_nivelacademico c, carrera d '
        ' where a.CURP=c.CURP and b.idNivelAcademico=c.idNivelacademico and c.idCarrera = d.idCarrera and a.CURP=%s ',
        (id))
    datos9 = cursor.fetchall()
    cursor.execute('select * from carrera order by Descripcion')
    datos10 = cursor.fetchall()
    return render_template("edi_candidato.html", datos=datos, habs=datos1, idiomas=datos2,
                           niveles=datos4, idis=datos5, can_habs=datos6, estados=datos7, 
                           nivelesC=datos9, carrerasN=datos10)


@app.route("/modifica_candidato/<string:id>", methods=["POST"])
def modifica_candidato(id):
    if request.method == 'POST':
        aux_curp = request.form['curp']
        print(aux_curp)
        aux_nombre = request.form['nombre']
        print(aux_nombre)
        aux_rfc = request.form['rfc']
        print(aux_rfc)
        aux_telefono = request.form['telefono']
        print(aux_telefono)
        aux_domicilio = request.form['domicilio']
        print(aux_domicilio)
        aux_nss = request.form['nss']
        print(aux_nss)
        aux_edad = request.form['edad']
        print(aux_edad)
        aux_estadociv = request.form['estadoc']
        print(aux_estadociv)
        aux_email = request.form['email']
        print(aux_email)
        aux_sexo = request.form['sexo']
        print(aux_sexo)



        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('UPDATE candidato SET Curp =%s, RFC =%s, Nombre =%s, Domicilio =%s, Telefono =%s, E_mail =%s, Sexo =%s, Edad =%s, NSS =%s, idEstadoCivil=%s WHERE Curp =%s' ,
        (aux_curp, aux_rfc, aux_nombre, aux_domicilio,
        aux_telefono, aux_email, aux_sexo, aux_edad, aux_nss, aux_estadociv,aux_curp))
        conn.commit()

        return redirect(url_for('candidato'))


@app.route("/agrega_hab_candidato/<string:id>/<string:idh>", methods=["POST"])
def agrega_hab_candidato(id, idh):
    if request.method == 'POST':
        aux_pto = request.form['can']
        aux_hab = request.form['habil']
        aux_exp = request.form['expe']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into candidato_has_habilidad (CURP, idHabilidad,Experiencia) values (%s,%s,%s)',
                       (aux_pto, aux_hab, aux_exp))
        conn.commit()
        cursor.execute(
            ' select CURP,RFC, Nombre,Domicilio, Telefono,E_mail, Sexo,Edad,NSS,Fotografia,idEstadoCivil from candidato where CURP=%s',
            (id))
        datos = cursor.fetchall()
        cursor.execute(' select * from habilidad ')
        datos1 = cursor.fetchall()
        cursor.execute(' select * from idioma ')
        datos2 = cursor.fetchall()
        
        cursor.execute(' select * from nivelacademico ')
        datos4 = cursor.fetchall()
        cursor.execute('select a.CURP, b.idIdioma,b.Lenguaje,c.CURP, c.idIdioma, c.Nivel '
                       'from candidato a, idioma b,candidato_has_idioma c '
                       'where a.CURP=c.CURP and b.idIdioma=c.idIdioma and a.CURP=%s ', (id))
        datos5 = cursor.fetchall()
        cursor.execute('select a.CURP, b.idHabilidad,b.Descripcion,c.CURP, c.idHabilidad, c.Experiencia '
                       'from candidato a, habilidad b,candidato_has_habilidad c '
                       'where a.CURP=c.CURP and b.idHabilidad=c.idHabilidad and a.CURP=%s ', (id))
        datos6 = cursor.fetchall()
        cursor.execute('select * from estadocivil order by Descripcion')
        datos7 = cursor.fetchall()
        
        cursor.execute(
            'select a.CURP, b.idNivelAcademico,b.Descripcion,c.Institucion,c.CURP, c.idNivelAcademico,c.idCarrera ,d.Descripcion '
            'from candidato a, nivelacademico b,candidato_has_nivelacademico c, carrera d '
            ' where a.CURP=c.CURP and b.idNivelAcademico=c.idNivelacademico and c.idCarrera = d.idCarrera and a.CURP=%s ',
            (id))
        datos9 = cursor.fetchall()
        cursor.execute('select * from carrera order by Descripcion')
        datos10 = cursor.fetchall()
        return render_template("edi_candidato.html", datos=datos, habs=datos1, idiomas=datos2,
                               niveles=datos4, idis=datos5, can_habs=datos6, estados=datos7,
                               nivelesC=datos9, carrerasN=datos10)


@app.route("/bo_hab_can/<string:id>/<string:idh>")
def bo_hab_can(id, idh):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from candidato_has_habilidad where CURP =%s and idHabilidad=%s', (id, idh))
    conn.commit()
    cursor.execute(
        ' select CURP,RFC, Nombre,Domicilio, Telefono,E_mail, Sexo,Edad,NSS,Fotografia,idEstadoCivil from candidato where CURP=%s',
        (id))
    datos = cursor.fetchall()
    cursor.execute(' select * from habilidad ')
    datos1 = cursor.fetchall()
    cursor.execute(' select * from idioma ')
    datos2 = cursor.fetchall()

    cursor.execute(' select * from nivelacademico ')
    datos4 = cursor.fetchall()
    cursor.execute('select a.CURP, b.idIdioma,b.Lenguaje,c.CURP, c.idIdioma, c.Nivel '
                   'from candidato a, idioma b,candidato_has_idioma c '
                   'where a.CURP=c.CURP and b.idIdioma=c.idIdioma and a.CURP=%s ', (id))
    datos5 = cursor.fetchall()
    cursor.execute('select a.CURP, b.idHabilidad,b.Descripcion,c.CURP, c.idHabilidad, c.Experiencia '
                   'from candidato a, habilidad b,candidato_has_habilidad c '
                   'where a.CURP=c.CURP and b.idHabilidad=c.idHabilidad and a.CURP=%s ', (id))
    datos6 = cursor.fetchall()
    cursor.execute('select * from estadocivil order by Descripcion')
    datos7 = cursor.fetchall()
    
    cursor.execute(
        'select a.CURP, b.idNivelAcademico,b.Descripcion,c.Institucion,c.CURP, c.idNivelAcademico,c.idCarrera ,d.Descripcion '
        'from candidato a, nivelacademico b,candidato_has_nivelacademico c, carrera d '
        ' where a.CURP=c.CURP and b.idNivelAcademico=c.idNivelacademico and c.idCarrera = d.idCarrera and a.CURP=%s ',
        (id))
    datos9 = cursor.fetchall()
    cursor.execute('select * from carrera order by Descripcion')
    datos10 = cursor.fetchall()
    return render_template("edi_candidato.html", datos=datos, habs=datos1, idiomas=datos2,
                           niveles=datos4, idis=datos5, can_habs=datos6, estados=datos7,
                           nivelesC=datos9, carrerasN=datos10)


@app.route("/agrega_idio_can/<string:id>/<string:idi>", methods=["POST"])
def agrega_idio_candidato(id, idi):
    if request.method == 'POST':
        aux_pto = request.form['cani']
        aux_hab = request.form['idio']
        aux_exp = request.form['nive']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute('insert into candidato_has_idioma (CURP, idIdioma,Nivel) values (%s,%s,%s)',
                       (aux_pto, aux_hab, aux_exp))
        conn.commit()
        cursor.execute(
            ' select CURP,RFC, Nombre,Domicilio, Telefono,E_mail, Sexo,Edad,NSS,Fotografia,idEstadoCivil from candidato where CURP=%s',
            (id))
        datos = cursor.fetchall()
        cursor.execute(' select * from habilidad ')
        datos1 = cursor.fetchall()
        cursor.execute(' select * from idioma ')
        datos2 = cursor.fetchall()
        
        cursor.execute(' select * from nivelacademico ')
        datos4 = cursor.fetchall()
        cursor.execute('select a.CURP, b.idIdioma,b.Lenguaje,c.CURP, c.idIdioma, c.Nivel '
                       'from candidato a, idioma b,candidato_has_idioma c '
                       'where a.CURP=c.CURP and b.idIdioma=c.idIdioma and a.CURP=%s ', (id))
        datos5 = cursor.fetchall()
        cursor.execute('select a.CURP, b.idHabilidad,b.Descripcion,c.CURP, c.idHabilidad, c.Experiencia '
                       'from candidato a, habilidad b,candidato_has_habilidad c '
                       'where a.CURP=c.CURP and b.idHabilidad=c.idHabilidad and a.CURP=%s ', (id))
        datos6 = cursor.fetchall()
        cursor.execute('select * from estadocivil order by Descripcion')
        datos7 = cursor.fetchall()
        
        cursor.execute(
            'select a.CURP, b.idNivelAcademico,b.Descripcion,c.Institucion,c.CURP, c.idNivelAcademico,c.idCarrera ,d.Descripcion '
            'from candidato a, nivelacademico b,candidato_has_nivelacademico c, carrera d '
            ' where a.CURP=c.CURP and b.idNivelAcademico=c.idNivelacademico and c.idCarrera = d.idCarrera and a.CURP=%s ',
            (id))
        datos9 = cursor.fetchall()
        cursor.execute('select * from carrera order by Descripcion')
        datos10 = cursor.fetchall()
        return render_template("edi_candidato.html", datos=datos, habs=datos1, idiomas=datos2, 
                               niveles=datos4, idis=datos5, can_habs=datos6, estados=datos7,
                               nivelesC=datos9, carrerasN=datos10)


@app.route("/bo_idi_can/<string:id>/<string:idi>")
def bo_idio_can(id, idi):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from candidato_has_idioma where CURP =%s and idIdioma=%s', (id, idi))
    conn.commit()
    cursor.execute(
        ' select CURP,RFC, Nombre,Domicilio, Telefono,E_mail, Sexo,Edad,NSS,Fotografia,idEstadoCivil from candidato where CURP=%s',
        (id))
    datos = cursor.fetchall()
    cursor.execute(' select * from habilidad ')
    datos1 = cursor.fetchall()
    cursor.execute(' select * from idioma ')
    datos2 = cursor.fetchall()
    
    cursor.execute(' select * from nivelacademico ')
    datos4 = cursor.fetchall()
    cursor.execute('select a.CURP, b.idIdioma,b.Lenguaje,c.CURP, c.idIdioma, c.Nivel '
                   'from candidato a, idioma b,candidato_has_idioma c '
                   'where a.CURP=c.CURP and b.idIdioma=c.idIdioma and a.CURP=%s ', (id))
    datos5 = cursor.fetchall()
    cursor.execute('select a.CURP, b.idHabilidad,b.Descripcion,c.CURP, c.idHabilidad, c.Experiencia '
                   'from candidato a, habilidad b,candidato_has_habilidad c '
                   'where a.CURP=c.CURP and b.idHabilidad=c.idHabilidad and a.CURP=%s ', (id))
    datos6 = cursor.fetchall()
    cursor.execute('select * from estadocivil order by Descripcion')
    datos7 = cursor.fetchall()
  
    cursor.execute(
        'select a.CURP, b.idNivelAcademico,b.Descripcion,c.Institucion,c.CURP, c.idNivelAcademico,c.idCarrera ,d.Descripcion '
        'from candidato a, nivelacademico b,candidato_has_nivelacademico c, carrera d '
        ' where a.CURP=c.CURP and b.idNivelAcademico=c.idNivelacademico and c.idCarrera = d.idCarrera and a.CURP=%s ',
        (id))
    datos9 = cursor.fetchall()
    cursor.execute('select * from carrera order by Descripcion')
    datos10 = cursor.fetchall()
    return render_template("edi_candidato.html", datos=datos, habs=datos1, idiomas=datos2,
                           niveles=datos4, idis=datos5, can_habs=datos6, estados=datos7,
                           nivelesC=datos9, carrerasN=datos10)



@app.route("/agrega_nivel_can/<string:id>/<string:idn>", methods=["POST"])
def agrega_nivel_candidato(id, idn):
    if request.method == 'POST':
        aux_pto = request.form['cannv']
        aux_hab = request.form['nv']
        aux_car = request.form['car']
        aux_ins = request.form['ins']
        conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
        cursor = conn.cursor()
        cursor.execute(
            'insert into candidato_has_nivelacademico (CURP, idNivelAcademico,idCarrera,institucion) values (%s,%s,%s,%s)',
            (aux_pto, aux_hab, aux_car, aux_ins))
        conn.commit()
        cursor.execute(
            ' select CURP,RFC, Nombre,Domicilio, Telefono,E_mail, Sexo,Edad,NSS,Fotografia,idEstadoCivil from candidato where CURP=%s',
            (id))
        datos = cursor.fetchall()
        cursor.execute(' select * from habilidad ')
        datos1 = cursor.fetchall()
        cursor.execute(' select * from idioma ')
        datos2 = cursor.fetchall()
        
        cursor.execute(' select * from nivelacademico ')
        datos4 = cursor.fetchall()
        cursor.execute('select a.CURP, b.idIdioma,b.Lenguaje,c.CURP, c.idIdioma, c.Nivel '
                       'from candidato a, idioma b,candidato_has_idioma c '
                       'where a.CURP=c.CURP and b.idIdioma=c.idIdioma and a.CURP=%s ', (id))
        datos5 = cursor.fetchall()
        cursor.execute('select a.CURP, b.idHabilidad,b.Descripcion,c.CURP, c.idHabilidad, c.Experiencia '
                       'from candidato a, habilidad b,candidato_has_habilidad c '
                       'where a.CURP=c.CURP and b.idHabilidad=c.idHabilidad and a.CURP=%s ', (id))
        datos6 = cursor.fetchall()
        cursor.execute('select * from estadocivil order by Descripcion')
        datos7 = cursor.fetchall()
        cursor.execute(
            'select a.CURP, b.idNivelAcademico,b.Descripcion,c.Institucion,c.CURP, c.idNivelAcademico,c.idCarrera ,d.Descripcion '
            'from candidato a, nivelacademico b,candidato_has_nivelacademico c, carrera d '
            ' where a.CURP=c.CURP and b.idNivelAcademico=c.idNivelacademico and c.idCarrera = d.idCarrera and a.CURP=%s ',
            (id))
        datos9 = cursor.fetchall()
        cursor.execute('select * from carrera order by Descripcion')
        datos10 = cursor.fetchall()
        return render_template("edi_candidato.html", datos=datos, habs=datos1, idiomas=datos2, 
                               niveles=datos4, idis=datos5, can_habs=datos6, estados=datos7, 
                               nivelesC=datos9, carrerasN=datos10)

@app.route("/bo_nivel_can/<string:id>/<string:idn>/<string:idc>")
def bo_nivel_can(id, idn, idc):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from candidato_has_nivelacademico where CURP =%s and idNivelAcademico=%s and idCarrera=%s',
                   (id, idn, idc))
    conn.commit()
    cursor.execute(
        ' select CURP,RFC, Nombre,Domicilio, Telefono,E_mail, Sexo,Edad,NSS,Fotografia,idEstadoCivil from candidato where CURP=%s',
        (id))
    datos = cursor.fetchall()
    cursor.execute(' select * from habilidad ')
    datos1 = cursor.fetchall()
    cursor.execute(' select * from idioma ')
    datos2 = cursor.fetchall()
 
    cursor.execute(' select * from nivelacademico ')
    datos4 = cursor.fetchall()
    cursor.execute('select a.CURP, b.idIdioma,b.Lenguaje,c.CURP, c.idIdioma, c.Nivel '
                   'from candidato a, idioma b,candidato_has_idioma c '
                   'where a.CURP=c.CURP and b.idIdioma=c.idIdioma and a.CURP=%s ', (id))
    datos5 = cursor.fetchall()
    cursor.execute('select a.CURP, b.idHabilidad,b.Descripcion,c.CURP, c.idHabilidad, c.Experiencia '
                   'from candidato a, habilidad b,candidato_has_habilidad c '
                   'where a.CURP=c.CURP and b.idHabilidad=c.idHabilidad and a.CURP=%s ', (id))
    datos6 = cursor.fetchall()
    cursor.execute('select * from estadocivil order by Descripcion')
    datos7 = cursor.fetchall()

    cursor.execute(
        'select a.CURP, b.idNivelAcademico,b.Descripcion,c.Institucion,c.CURP, c.idNivelAcademico,c.idCarrera ,d.Descripcion '
        'from candidato a, nivelacademico b,candidato_has_nivelacademico c, carrera d '
        ' where a.CURP=c.CURP and b.idNivelAcademico=c.idNivelacademico and c.idCarrera = d.idCarrera and a.CURP=%s ',
        (id))
    datos9 = cursor.fetchall()
    cursor.execute('select * from carrera order by Descripcion')
    datos10 = cursor.fetchall()
    return render_template("edi_candidato.html", datos=datos, habs=datos1, idiomas=datos2,
                           niveles=datos4, idis=datos5, can_habs=datos6, estados=datos7,
                           nivelesC=datos9, carrerasN=datos10)

@app.route('/bo_candidato/<string:id>')
def bo_candidato(id):
    conn = pymysql.connect(host='NovaTech.mysql.pythonanywhere-services.com', user='NovaTech', passwd='tacosdechile', db='NovaTech$default')
    cursor = conn.cursor()
    cursor.execute('delete from candidato_has_idioma where CURP = %s',(id))
    conn.commit()
    cursor.execute('delete from candidato_has_habilidad where CURP = %s',(id))
    conn.commit()
    cursor.execute('delete from candidato_has_nivelacademico where CURP =  %s',(id))
    conn.commit()
    cursor.execute('delete from candidato where CURP =  %s',(id))
    conn.commit()
    return redirect(url_for('candidato'))


if __name__ == "__main__":
    app.run(debug=True)