from mysql import connector
import functools

class Model:
    # A data model to MySQL for an cine DB
    def __init__(self, config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connector_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connector_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    '''
    **********************************
    *        Metodos usuarios        *
    **********************************
    '''
    def create_user(self, name, last1, last2, email, password, admin):
        try:
            sql = 'INSERT INTO usuarios(`nombre`, `a_paterno`, `a_materno`, `correo`, `contraseña`, `is_admin`) VALUES(%s, %s, %s, %s, %s, %s)'
            vals = ( name, last1, last2, email, password, admin)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    # Sirve para el login
    def read_a_admin(self, emaill, password):
        try:
            sql = ' SELECT usuarios.usuario_id, usuarios.is_admin FROM usuarios WHERE usuarios.correo = %s and usuarios.contraseña = %s'
            vals = (emaill, password)
            self.cursor.execute(sql, vals)

            # Regresa el valor para saber si es admin o user
            records = self.cursor.fetchone()
            return records
        
        except connector.Error as err:
            return err 

    def read_a_user(self, id_user):
        try:
            sql = 'SELECT * FROM usuarios WHERE usuario_id = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def read_all_user(self):
        try:
            sql = 'SELECT * FROM usuarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_user_name(self, name, last1):
        try:
            sql = 'SELECT * FROM usuarios WHERE nombre = %s AND a_paterno = %s'
            vals = (name, last1)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 
    
    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE usuarios SET '+','.join(fields)+' WHERE usuario_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
            
        except connector.Error as err:
            self.cnx.rollback()
            return err  

    def delete_user(self, id_user):
        try:
            sql = 'DELETE FROM usuarios WHERE usuario_id = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err

    '''
    ***********************************
    *      Metodos clasificacion      *
    ***********************************
    '''
    def create_classification(self, clasificacion, descr):
        try:
            sql = 'INSERT INTO clasificacion(`clasificacion`, `descr`) VALUES(%s, %s)'
            vals = (clasificacion, descr)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_classification(self, id_clasificacion):
        try:
            sql = 'SELECT * FROM clasificacion WHERE clasificacion_id = %s'
            vals = (id_clasificacion,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        
        except connector.Error as err:
            return err

    def read_all_classification(self):
        try:
            sql = 'SELECT * FROM clasificacion'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def read_clasification_name(self, name):
        try:
            sql = 'SELECT * FROM clasificacion WHERE clasificacion = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def update_classification(self, fields, vals):
        try:
            sql = 'UPDATE clasificacion SET ' + ','.join(fields) + 'WHERE clasificacion_id = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_classification(self, id_classification):
        try:
            sql = 'DELETE FROM clasificacion WHERE clasificacion_id = %s'
            vals = (id_classification,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    '''
    ******************************
    *      Metodos pelicula      *
    ******************************
    '''
    def create_movie(self, clasification, title, date, sinopsis):
        try:
            sql = 'INSERT INTO pelicula(`clasificacion_id`, `titulo`, `fecha`, `sinopsis`) VALUES(%s, %s, %s, %s)'
            vals = (clasification, title, date, sinopsis)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_movie(self, id_movie):
        try:
            sql = 'SELECT pelicula.pelicula_id, clasificacion.clasificacion, pelicula.titulo, pelicula.fecha, pelicula.sinopsis from pelicula JOIN clasificacion ON pelicula.clasificacion_id = clasificacion.clasificacion_id AND pelicula.pelicula_id = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        
        except connector.Error as err:
            return err

    def read_all_movies(self):
        try:
            sql = 'SELECT pelicula.pelicula_id, clasificacion.clasificacion, pelicula.titulo, pelicula.fecha, pelicula.sinopsis from pelicula JOIN clasificacion ON pelicula.clasificacion_id = clasificacion.clasificacion_id'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_movie_clasification(self, clasificacion):
        try:
            sql = 'SELECT pelicula.pelicula_id, clasificacion.clasificacion, pelicula.titulo, pelicula.fecha, pelicula.sinopsis FROM pelicula JOIN clasificacion ON pelicula.clasificacion_id = clasificacion.clasificacion_id WHERE clasificacion.clasificacion = %s'
            vals = (clasificacion,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_movie_name(self, name):
        try:
            sql = 'SELECT * FROM pelicula WHERE titulo = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE pelicula SET '+','.join(fields)+' WHERE pelicula_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
            
        except connector.Error as err:
            self.cnx.rollback()
            return err  

    def delete_movie(self, movie_id):
        try:
            sql = 'DELETE FROM pelicula WHERE pelicula_id = %s'
            vals = (movie_id,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err  

    '''
    ******************************
    *      Metodos idioma      *
    ******************************
    '''
    def create_language(self, descr):
        try:
            sql = 'INSERT INTO idioma(`descr`) VALUES(%s)'
            vals = (descr,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_languague(self, languague_id):
        try:
            sql = 'SELECT * FROM idioma WHERE idioma_id = %s'
            vals = (languague_id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err 

    def read_all_lamguage(self):
        try:
            sql = 'SELECT * FROM idioma'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_language_name(self, name):
        try:
            sql = 'SELECT * FROM idioma WHERE descr = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def update_language(self, fields, vals):
        try:
            sql = 'UPDATE idioma SET '+','.join(fields)+' WHERE idioma_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
            
        except connector.Error as err:
            self.cnx.rollback()
            return err  

    def delete_language(self, languague_id):
        try:
            sql = 'DELETE FROM idioma WHERE idioma_id = %s'
            vals = (languague_id,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err

    '''
    ******************************
    *      Metodos asientos      *
    ******************************
    '''
    def create_seat(self, row, colum):
        try:
            sql = 'INSERT INTO asiento(`fila`, `columna`) VALUES(%s, %s)'
            vals = (row, colum)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_seat = self.cursor.lastrowid
            return id_seat

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_all_seat(self):
        try:
            sql = 'SELECT * FROM asiento'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def seat_available(self, lista, seat):
        if seat in lista:
            return False
        else:
            return True

    def update_seat(self, fields, vals):
        try:
            sql = 'UPDATE asiento SET ' +','.join(fields)+' WHERE asiento_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err 

    '''
    ******************************
    *      Metodos Sala      *
    ******************************  
    '''
    def create_hall(self, row, colum):
        id_seat = self.create_seat(row, colum)   
        try:
            sql = 'INSERT INTO sala(`asiento_id`) VALUES(%s)'
            vals = (id_seat, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True         

        except connector.Error as err:
            self.cnx.rollback() 
            return err   

    def read_a_hall(self, id_hall):
        try:
            sql = 'SELECT sala.sala_id, asiento.fila, asiento.columna FROM sala JOIN asiento ON sala.asiento_id = asiento.asiento_id AND sala.sala_id = %s;'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err 

    # Devuelve las filas y columas de la tabla asientos
    def read_seat_hall(self, id_proyection):
        try:
            sql = 'SELECT asiento.fila, asiento.columna FROM proyeccion JOIN sala ON proyeccion.sala_id = sala.sala_id JOIN asiento ON sala.asiento_id = asiento.asiento_id WHERE proyeccion.proyeccion_id = %s'
            vals = (id_proyection,)
            self.cursor.execute(sql, vals)
            
            f = self.cursor.fetchall()
            row = functools.reduce(lambda sub, ele: sub * 10 + ele, f)
            return row
        
        except connector.Error as err:
            return err

    def read_all_hall(self):
        try:
            sql = 'SELECT sala.sala_id, asiento.fila, asiento.columna FROM sala JOIN asiento ON sala.asiento_id = asiento.asiento_id'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_hall_size(self, row, col):
        try:
            sql = 'SELECT sala.sala_id, asiento.fila, asiento.columna FROM sala JOIN asiento ON sala.asiento_id = asiento.asiento_id WHERE asiento.fila = %s AND asiento.columna = %s'
            vals = (row, col)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        
        except connector.Error as err:
            return err

    def delete_hall(self, id_hall):
        try:
            sql = 'DELETE FROM asiento WHERE asiento_id = %s'
            vals = tuple(id_hall,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    '''
    *******************************
    *        Metodos Fecha        *
    *******************************  
    '''
    def create_date(self, date):
        try:
            sql = 'INSERT INTO fecha(`fecha`) VALUES(%s)'
            vals = (date,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_date(self, id_date):
        try:
            sql = 'SELECT * FROM fecha WHERE fecha_id = %s'
            vals = (id_date,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err 

    def read_all_date(self):
        try:
            sql = 'SELECT * FROM fecha'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_date_range(self, date_ini, date_end):
        try:
            sql = 'SELECT * FROM fecha WHERE fecha >= %s and fecha <= %s'
            vals = (date_ini, date_end)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        
        except connector.Error as err:
            return err 

    def update_date(self, fields, vals):
        try:
            sql = 'UPDATE fecha SET '+','.join(fields)+' WHERE fecha_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
            
        except connector.Error as err:
            self.cnx.rollback()
            return err  

    def delete_date(self, id_date):
        try:
            sql = 'DELETE FROM fecha WHERE fecha_id = %s'
            vals = (id_date,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err

    '''
    ************************************
    *        Metodos proyeccion        *
    ************************************  
    '''
    def create_proyeccion(self, id_movie, idioma_id, id_hall, id_date, hour):
        try:
            sql = 'INSERT INTO proyeccion(`pelicula_id`, `idioma_id`, `sala_id`, `fecha_id`, `hora`) VALUES(%s, %s, %s, %s, %s)'
            vals = (id_movie, idioma_id, id_hall, id_date, hour)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_proyeccion(self, id_proyection):
        try:
            sql = 'SELECT proyeccion.proyeccion_id, pelicula.titulo, idioma.descr, sala.sala_id, fecha.fecha, proyeccion.hora FROM proyeccion JOIN pelicula ON proyeccion.pelicula_id = pelicula.pelicula_id JOIN idioma ON proyeccion.idioma_id = idioma.idioma_id JOIN sala ON proyeccion.sala_id = sala.sala_id JOIN fecha ON proyeccion.fecha_id = fecha.fecha_id WHERE proyeccion.proyeccion_id = %s'
            vals = (id_proyection,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err 

    def read_all_proyection(self):
        try:
            sql = ' SELECT proyeccion.proyeccion_id, pelicula.titulo, idioma.descr, sala.sala_id, fecha.fecha, proyeccion.hora FROM proyeccion JOIN pelicula ON proyeccion.pelicula_id = pelicula.pelicula_id JOIN idioma ON proyeccion.idioma_id = idioma.idioma_id JOIN sala ON proyeccion.sala_id = sala.sala_id JOIN fecha ON proyeccion.fecha_id = fecha.fecha_id'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_proyection_name(self, name):
        try:
            sql = 'SELECT proyeccion.proyeccion_id, pelicula.titulo, idioma.descr, sala.sala_id, fecha.fecha, proyeccion.hora FROM proyeccion JOIN pelicula ON proyeccion.pelicula_id = pelicula.pelicula_id JOIN idioma ON proyeccion.idioma_id = idioma.idioma_id JOIN sala ON proyeccion.sala_id = sala.sala_id JOIN fecha ON proyeccion.fecha_id = fecha.fecha_id WHERE pelicula.titulo = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err   

    def read_proyection_date(self, date):
        try:
            sql = 'SELECT proyeccion.proyeccion_id, pelicula.titulo, idioma.descr, sala.sala_id, fecha.fecha, proyeccion.hora FROM proyeccion JOIN pelicula ON proyeccion.pelicula_id = pelicula.pelicula_id JOIN idioma ON proyeccion.idioma_id = idioma.idioma_id JOIN sala ON proyeccion.sala_id = sala.sala_id JOIN fecha ON proyeccion.fecha_id = fecha.fecha_id WHERE fecha.fecha = %s'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err  

    def read_proyection_time(self, time, movie):
        try:
            sql = 'SELECT proyeccion.proyeccion_id, pelicula.titulo, idioma.descr, sala.sala_id, fecha.fecha, proyeccion.hora FROM proyeccion JOIN pelicula ON proyeccion.pelicula_id = pelicula.pelicula_id JOIN idioma ON proyeccion.idioma_id = idioma.idioma_id JOIN sala ON proyeccion.sala_id = sala.sala_id JOIN fecha ON proyeccion.fecha_id = fecha.fecha_id WHERE proyeccion.hora = %s AND pelicula.titulo = %s'
            vals = (time, movie)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err  

    def update_proyection(self, fields, vals):
        try:
            sql = 'UPDATE proyeccion SET '+','.join(fields)+' WHERE proyeccion_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
            
        except connector.Error as err:
            self.cnx.rollback()
            return err  

    def delete_proyection(self, id_proyection):
        try:
            sql = 'DELETE FROM proyeccion WHERE proyeccion_id = %s'
            vals = (id_proyection,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err

    '''
    *********************************
    *        Metodos compras        *
    *********************************  
    '''
    def crate_purchase(self, id_user, id_ticket, total_cost):
        try:
            sql = 'INSERT INTO compras(`usuario_id`, `ticket_id`,  `costo_total`) VALUES(%s, %s, %s)'
            vals = (id_user, id_ticket, total_cost)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def read_all_pruchase(self, id_user):
        try:
            sql = 'SELECT compras.compra_id, ticket.ticket_id, pelicula.titulo, compras.costo_total FROM compras JOIN pelicula ON compras.compra_id = pelicula.pelicula_id JOIN ticket ON compras.ticket_id = ticket.ticket_id JOIN usuarios ON compras.usuario_id = usuarios.usuario_id WHERE usuarios.usuario_id = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            self.cnx.rollback()
            return err 

    '''
    ********************************
    *        Metodos ticket        *
    ********************************  
    '''
    def crate_ticket(self, id_proyection, seat, cost):
        try:
            sql = 'INSERT INTO ticket(`proyeccion_id`, `asiento`, `costo`) VALUES(%s, %s, %s)'
            vals = (id_proyection, seat, cost)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def read_a_ticket(self, id_ticket):
        try:
            sql = 'SELECT ticket.ticket_id, ticket.asiento, proyeccion.sala_id, pelicula.titulo, fecha.fecha, proyeccion.hora FROM ticket JOIN proyeccion ON ticket.proyeccion_id = proyeccion.proyeccion_id JOIN pelicula ON proyeccion.pelicula_id = pelicula.pelicula_id JOIN fecha ON proyeccion.fecha_id = fecha.fecha_id WHERE ticket.ticket_id = %s'
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records

        except connector.Error as err:
            return err

    def read_a_ticket_user(self, id_user):
        try:
            sql = 'SELECT ticket.ticket_id, ticket.asiento, proyeccion.sala_id, pelicula.titulo, fecha.fecha, proyeccion.hora FROM ticket JOIN proyeccion ON ticket.proyeccion_id = proyeccion.proyeccion_id JOIN pelicula ON proyeccion.pelicula_id = pelicula.pelicula_id JOIN fecha ON proyeccion.fecha_id = fecha.fecha_id JOIN compras JOIN usuarios WHERE ticket.ticket_id = 1 AND ticket.ticket_id = compras.ticket_id AND usuarios.usuario_id = compras.usuario_id AND usuarios.usuario_id = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
            
        except connector.Error as err:
            return err

    # leerBoletoIdFunc
    def read_ticket_proyection(self, id_proyection):
        try:
            sql = 'SELECT * FROM ticket WHERE proyeccion_id = %s'
            #sql = 'SELECT ticket.asiento FROM ticket WHERE ticket.proyeccion_id = %s'
            vals = (id_proyection,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def read_ticket_seat(self, seat):
        try:
            sql = 'SELECT * FROM ticket WHERE asiento = %s'
            vals = (seat,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
            
        except connector.Error as err:
            return err