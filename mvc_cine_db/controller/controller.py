from model.model import Model
from view.view import View
import os
import string as s
import functools

class Controller:
    # A controller for a cine DB
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.menu()
        self.view.end()

    #______________________ Controlador General ______________________#
    def menu(self):
        a, b = self.ask_login()

        if b == 0:
            self.clear()
            self.user_menu(a)
        elif b == 1:
           self.admin_menu(a)

    def ask_login(self):
        o = '0'

        while o != '2':
            self.view.msg('1. Iniciar sesion.')
            self.view.msg('2. Crear cuenta.')
            self.view.option('2')
    
            o = input()
            if o == '1':
                opc = '0'
                while opc != False:
                    self.view.msg("Login")
                    self.view.ask('Correo: ')
                    email = input()
                    self.view.ask('Contrasena: ')
                    password = input()
                    
                    user = self.model.read_a_admin(email, password)
                    if type(user) == tuple:
                        print('Usuario correcto')
                        return user
                    else:
                        print('Contrasena o correo incorrecto') 
                        o = True
            elif o == '2':
                name, last1, last2, email, password = self.ask_acount()

                out = self.model.create_user(name, last1, last2, email, password, '0')
                if out == True:
                    self.view.ok(name + ' ' + last1 + ' ', ' agregado')
                    user = self.model.read_a_admin(email, password)
                    return user
                else: 
                    self.view.error('No se pudo agregar el usuario.')
            else:
                self.view.not_void_option()

    def clear(self):
        os.system("pause")
        os.system("cls")

    def update_list(self, fs, vs):
        fields = []
        vals = []

        for f,v in zip(fs, vs):
            if v != '':
                fields.append(f + ' = %s')
                vals.append(v)
        
        return fields, vals

    '''
    **************************************************
    ****      Controlador Cine Administrador      ****     
    **************************************************
    '''    
    def admin_menu(self, a):
        o = '0'
        while o != '8':
            # Mostramos los datos del administrador
            user = self.model.read_a_user(a)
            self.view.show_admin_header('Administrador en uso')
            self.view.show_a_admin(user)
            self.view.show_admin_footer()

            self.view.menu_admin()
            self.view.option('8')

            o = input()
            if o == '1':
                self.admin_user()
                self.clear()
            elif o == '2':
                self.clasification_menu()
                self.clear()
            elif o == '3':
                self.movie_menu()
                self.clear()
            elif o == '4':
                self.language_menu()
                self.clear()
            elif o == '5':
                self.hall_menu()
                self.clear()
            elif o == '6':
                self.date_menu()
                self.clear()
            elif o == '7':
                self.proyection_menu()
                self.clear()
            elif o == '8':
                return
            else:
                self.view.not_void_option()
        return

    '''
    ****************************************
    ****      Controlador Usuarios      ****     
    ****************************************
    '''
    def admin_user(self):
        o = '0'
        while o != '7':
            self.view.user_admin()
            self.view.option('7')

            o = input()
            if o == '1':
                self.create_user()
            elif o == '2':
                self.read_a_user()
            elif o == '3':
                self.read_all_user()
            elif o == '4':
                self.read_user_name()
            elif o == '5':
                self.update_user()
            elif o == '6':
                self.delete_user()
            elif o == '7':
                return
            else:
                self.view.not_void_option()
        return

    def ask_user(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        last1 = input()
        self.view.ask('Apellido materno: ')
        last2 = input()
        self.view.ask('Correo: ')
        email = input()
        self.view.ask('Contraseña: ')
        password = input()
        self.view.ask('¿Que tipo de usuario es?\n0. Usuario\n1. Administrador')
        self.view.ask('Tipo de usuario: ')
        is_admin = input()
        return [name, last1, last2, email, password, is_admin]

    def create_user(self):
        name, last1, last2, email, password, is_admin = self.ask_user()

        out = self.model.create_user(name, last1, last2, email, password, is_admin)
        if out == True:
           self.view.ok(name + ' ' + last1 + ' ', ' agregado')
        else: 
            self.view.error('No se pudo agregar el usuario.')
        return

    def read_a_user(self):
        self.view.ask('ID usuario: ')
        id_user = input()

        user = self.model.read_a_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header('Datos del usuario ' + id_user + '')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Problema al leer usario')
        return 
    
    def read_all_user(self):
        users = self.model.read_all_user()
        if type(users) == list:
            self.view.show_user_header('Todos los usuarios')
            
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('Problema al leer los usuarios')

    def read_user_name(self):   
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        last1 = input()

        users  = self.model.read_user_name(name, last1)
        if type(users) == list:
            self.view.show_user_header('Usuarios con el nombre: ' + name + ' ' + last1 + ' ')
            
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()

            return name, last1
        else:
            self.view.error('Problema al leer los usuariso')
        return

    def update_user(self):
        self.view.ask('ID usuario a modificar: ')
        id_user = input()

        user = self.model.read_a_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header('Datos del usuario ' + id_user + ' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else: 
            if user == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Problema al leer los usuarios')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para omitir el campo): ')
        whole_vals = self.ask_user()
        fields, vals = self.update_list(['nombre', 'a_paterno', 'a_materno', 'correo', 'contraseña', 'is_admin'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)

        out = self.model.update_user(fields, vals)
        if out == True:
            self.view.ok(id_user, ' Actualizado')
        else:
            self.view.error('No se pudo actulizar el usuario')
        return 

    def delete_user(self):
        self.view.ask('ID usuario a borrar: ')
        id_user = input()

        count = self.model.delete_user(id_user)
        if count != 0:
            self.view.ok(id_user, ' se borro')
        else:
            if count == 0:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Problema al borrar el usuario')

    '''
    *********************************************
    ****      Controlador Clasificacion      ****     
    *********************************************
    '''
    def clasification_menu(self):
        o = '0'
        while o != '7':
            self.view.clasification_menu()
            self.view.option('7')

            o = input()
            if o == '1':
                self.create_clasification()
            elif o == '2':
                self.read_a_clasification()
            elif o == '3':
                self.read_all_clasification()
            elif o == '4':
                self.read_a_clasification_name()
            elif o == '5':
                self.update_clasification()
            elif o == '6':
                self.delete_clasification()
            elif o == '7':
                return 
            else:
                self.view.not_void_option()
        return

    def ask_clasification(self):
        self.view.ask('Clasificacion: ')
        clasificacion = input()
        self.view.ask('Descripcion: ')
        descr = input()
        return [clasificacion, descr]

    def create_clasification(self):
        clasificacion, descr = self.ask_clasification()
        
        out = self.model.create_classification(clasificacion, descr)
        if out == True:
            self.view.ok(clasificacion+' ', 'agregado')
        else:
            self.view.error('No se pudo agregar la clasificacion')
        return

    def read_a_clasification(self):
        self.view.ask('ID clasificacion: ')
        id_clasification = input()

        clasification = self.model.read_a_classification(id_clasification)
        if type(clasification) == tuple:
            self.view.show_clasification_header('Datos clasificaion ' +  id_clasification + ' ')
            self.view.show_a_clasificacion(clasification)
            self.view.show_clasification_midder()
            self.view.show_clasification_footer()
        else:
            if clasification == None:
                self.view.error('La clasificacion no existe')
            else:
                self.view.error('Problema al leer las clasificacion')
        return

    def read_all_clasification(self):
        clasifications = self.model.read_all_classification()
        if type(clasifications) == list:
            self.view.show_clasification_header('Todas las clasificaciones')
            
            for clasification in clasifications:
                self.view.show_a_clasificacion(clasification)
                self.view.show_clasification_midder()
            self.view.show_clasification_footer()
        else:
            self.view.error('Problema al leer las clasificaciones')

    def read_a_clasification_name(self):
        self.view.ask('Nombre: ')
        name = input()

        clasifications  = self.model.read_clasification_name(name)   
        if type(clasifications) == list:
            self.view.show_clasification_header('Clasificacion: ' + name + ' ' )

            for clasification in clasifications:
                self.view.show_a_clasificacion(clasification)
                self.view.show_clasification_midder()
            self.view.show_clasification_footer()
            
        else:
            self.view.error('Problema al leer los usuariso')
        return

    def update_clasification(self):
        self.view.ask('ID clasificacion a modificar: ')
        id_clasification = input()

        clasification = self.model.read_a_classification(id_clasification)
        if type(clasification) == tuple:
            self.view.show_clasification_header('Datos de la clasificacion ' + id_clasification + ' ')
            self.view.show_a_clasificacion(clasification)
            self.view.show_clasification_midder()
            self.view.show_clasification_footer()
        else: 
            if clasification == None:
                self.view.error('La clasificacion no existe')
            else:
                self.view.error('Problema al leer las clasificacion')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para omitir el campo): ')
        whole_vals = self.ask_clasification()
        fields, vals = self.update_list(['clasificacion', 'descr'], whole_vals)
        vals.append(id_clasification)
        vals = tuple(vals)

        out = self.model.update_classification(fields, vals)
        if out == True:
            self.view.ok(id_clasification, ' Actualizado')
        else:
            self.view.error('No se pudo actulizar la clasificacion')
        return 

    def delete_clasification(self):
        self.view.ask('ID clasificacion a borrar: ')
        id_clasification = input()

        count = self.model.delete_classification(id_clasification)
        if count != 0:
            self.view.ok(id_clasification, ' se borro')
        else:
            if count == 0:
                self.view.error('La clasificacion no existe')
            else:
                self.view.error('Problema al borrar la clasificacion')

    '''
    *****************************************
    ****      Controlador peliculas      ****     
    *****************************************
    '''      
    def movie_menu(self):
        o = '0'
        while o != '8':
            self.view.movies_menu()
            self.view.option('8')
            
            o = input()
            if o == '1':
                self.create_movie()
                self.clear()
            elif  o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_all_movies()
            elif o == '4':
                self.read_movie_clasification()
            elif o == '5':
                self.read_movies_name()
            elif o == '6':
                self.update_movie()
            elif o == '7':
                self.delete_movie()
            elif o == '8':
               return
            else:
                self.view.not_void_option()
        return

    def ask_movie(self):
        self.read_all_clasification()
        self.view.ask('Clasificacion:')
        clasification = input()
        self.view.ask('Titulo: ')
        title = input()
        self.view.ask('Fecha(yy-mm-dd): ')
        date = input()
        self.view.ask('Sinopsis: ')
        sinopsis = input()
        return [clasification, title, date, sinopsis]

    def create_movie(self):
        clasificacion, titulo, fecha, sinopsis = self.ask_movie()
        
        out = self.model.create_movie(clasificacion, titulo, fecha, sinopsis)
        if out == True:
            self.view.ok(titulo+' '+' ', 'agregado')
        else:
            self.view.error('No se pudo agregar la pelicula')
        return 

    def read_a_movie(self):
        self.view.ask('ID pelicula: ')
        id_movie = input()

        movie = self.model.read_a_movie(id_movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula ' +  id_movie + ' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('La pelicula no existe.')
            else:
                self.view.error('Problema al leer la pelicula')
        return

    def read_all_movies(self):
        peliculas = self.model.read_all_movies()
        if type(peliculas) == list:
            self.view.show_movie_header('Todas las peliculas')
            
            for movie in peliculas:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer las peliculas')

    def read_movie_clasification(self):
        self.view.ask('Clasificación: ')
        clasification = input()

        movies = self.model.read_movie_clasification(clasification)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas con la calsificacion: ' + clasification + ' ')

            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer las peliculas.')
        return 

    def read_movies_name(self):
        self.view.ask('Titulo: ')
        name = input()

        movies  = self.model.read_movie_name(name)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas con el nombre: ' + name + ' ')
            
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer las peliculas')
        return

    def update_movie(self):
        self.view.ask('ID pelicula a modificar: ')
        id_movie = input()

        movie = self.model.read_a_movie(id_movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula ' + id_movie + ' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else: 
            if movie == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer las peliculas')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para omitir el campo): ')
        whole_vals = self.ask_movie()
        fields, vals = self.update_list(['clasificacion_id', 'titulo', 'fecha', 'sinopsis'], whole_vals)
        vals.append(id_movie)
        vals = tuple(vals)

        out = self.model.update_movie(fields, vals)
        if out == True:
            self.view.ok(id_movie, ' Actualizado')
        else:
            self.view.error('No se pudo actulizar la pelicula')
        return 

    def delete_movie(self):
        self.view.ask('ID pelicula a borrar: ')
        id_movie = input()

        count = self.model.delete_movie(id_movie)
        if count != 0:
            self.view.ok(id_movie, ' se borro')
        else:
            if count == 0:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al borrar la pelicula')

    '''
    **************************************
    ****      Controlador idioma      ****     
    **************************************
    '''
    def language_menu(self):
        o = '0'
        while o != '7':
            self.view.idioma_menu()
            self.view.option('7')

            o = input()
            if o == '1':
                self.create_language()
            elif o == '2':
                self.read_a_language()
            elif o == '3':
                self.read_all_language()
            elif o == '4':
                self.read_language_name()
            elif o == '5':
                self.update_language()
            elif o == '6':
                self.delete_language() 
            elif o == '7':
                return
            else:
                self.view.not_void_option()
        return

    def ask_idioma(self):
        self.view.ask('Idioma: ')
        language = input()
        return [language]

    def create_language(self):
        descr, = self.ask_idioma()
        
        out = self.model.create_language(descr)
        if out == True:
            self.view.ok(descr+' ', 'agregado')
        else:
            self.view.error('No se pudo agregar el idioma')
        return
        
    def read_a_language(self):
        self.view.ask('ID idioma: ')
        id_language = input()

        idioma = self.model.read_a_languague(id_language)
        if type(idioma) == tuple:
            self.view.show_idioma_header('Datos del idioma ' + id_language + '')
            self.view.show_a_idioma(idioma)
            self.view.show_idioma_midder()
            self.view.show_idioma_footer()
        else:
            if idioma == None:
                self.view.error('El idioma no existe')
            else:
                self.view.error('Problema al leer el idioma')
        return

    def read_all_language(self):
        languages = self.model.read_all_lamguage()
        if type(languages) == list:
            self.view.show_idioma_header('Todos los idiomas')
            
            for language in languages:
                self.view.show_a_idioma(language)
                self.view.show_idioma_midder()
            self.view.show_idioma_footer()
        else:
            self.view.error('Problema al leer los idiomas')

    def read_language_name(self):
        self.view.ask('Nombre del idioma: ')
        language = input()

        languages = self.model.read_language_name(language)
        if type(languages) == list:
            self.view.show_idioma_header('Idioma: ' + language + '')

            for i in languages:
                self.view.show_a_idioma(i)
                self.view.show_idioma_midder()
            self.view.show_idioma_footer()
        else:
            self.view.error('Problemas al leer el idioma.')
        return

    def update_language(self):
        self.view.ask('ID idioma a modificar: ')
        id_language = input()

        language = self.model.read_a_languague(id_language)
        print(language)
        if type(language) == tuple:
            self.view.show_idioma_header('Datos del idioma ' + id_language + ' ')
            self.view.show_a_idioma(language)
            self.view.show_idioma_midder()
            self.view.show_idioma_footer()
        else: 
            if language == None:
                self.view.error('El idioma no existe')
            else:
                self.view.error('Problema al leer los idiomas')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para omitir el campo): ')
        whole_vals = self.ask_idioma()
        fields, vals = self.update_list(['descr'], whole_vals)
        vals.append(id_language)
        vals = tuple(vals)

        out = self.model.update_language(fields, vals)
        if out == True:
            self.view.ok(id_language, ' Actualizado')
        else:
            self.view.error('No se pudo actulizar el idioma')
        return 

    def delete_language(self):
        self.view.ask('ID lenguaje a borrar: ')
        id_language = input()

        count = self.model.delete_language(id_language)
        if count != 0:
            self.view.ok(id_language, ' se borro')
        else:
            if count == 0:
                self.view.error('El idioma no existe')
            else:
                self.view.error('Problema al borrar el idioma')
    
    '''
    **************************************
    ****        Controlador salas       **    
    **************************************
    '''
    def hall_menu(self):
        o = '0'
        while o != '7':
            self.view.salas_menu()
            self.view.option('7')

            o = input()
            if o == '1':
                self.create_hall()
            elif o == '2':
                self.read_a_hall()
            elif o == '3':
                self.read_all_hall()
            elif o == '4':
                self.read_hall_size()
            elif o == '5':
                self.update_hall()
            elif o == '6':
                self.delete_hall()
            elif o == '7':
                return
            else:
                self.view.not_void_option()
        return

    def ask_seat(self):
        self.view.ask('Fila: ')
        row = input()
        self.view.ask("Columna: ")
        colum = input()
        return [row, colum]

    def create_hall(self):
        fila, columna = self.ask_seat()

        out = self.model.create_hall(fila, columna)
        if out == True:
            print('Se creo la sala correctamente.')
        else:
            self.view.error("No se pudo agregar la sala")

    def read_a_hall(self):
        self.view.ask('ID sala: ')
        id_hall = input()

        hall = self.model.read_a_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header('Datos de la sala ' + id_hall + '')
            self.view.show_a_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al leer la sala')
        return

    def read_all_hall(self):
        halls = self.model.read_all_hall()
        if type(halls) == list:
            self.view.show_hall_header('Todas las salas')
            
            for hall in halls:
                self.view.show_a_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('Problema al leer las salas')

    def read_hall_size(self):
        self.view.ask('Fila: ')
        row = input()
        self.view.ask('Columna: ')
        col = input()

        halls = self.model.read_hall_size(row, col)
        if type(halls) == list:
            self.view.show_hall_header('Salas con fila: ' + row + ' columna: ' + col + '')

            for hall in halls:
                self.view.show_a_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('La sala no existe.')
            else:
                self.view.error('Problema al leer las salas.')

    def update_hall(self):
        self.view.ask('ID sala a modificar: ')
        id_hall = input()

        hall = self.model.read_a_hall(id_hall)
        print(hall)
        if type(hall) == tuple:
            self.view.show_hall_header('Datos de la sala ' + id_hall + ' ')
            self.view.show_a_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else: 
            if hall == None:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al leer la sala')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para omitir el campo): ')
        whole_vals = self.ask_seat()
        fields, vals = self.update_list(['fila', 'columna'], whole_vals)
        vals.append(id_hall)
        vals = tuple(vals)

        out = self.model.update_seat(fields, vals)
        if out == True:
            self.view.ok(id_hall, ' Actualizado')
        else:
            self.view.error('No se pudo actulizar el contacto')
        return 

    def delete_hall(self):
        self.view.ask('ID sala a borrar: ')
        id_hall = input()

        count = self.model.delete_hall(id_hall)
        if count != 0:
            self.view.ok(id_hall, ' se borro')
        else:
            if count == 0:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al borrar la sala')

    '''
    *************************************
    ****       Controlador Fecha       **    
    *************************************
    '''
    def date_menu(self):
        o = '0'
        while o != '7':
            self.view.fecha_menu()
            self.view.option('7')

            o = input()
            if o == '1':
                self.create_date()
            elif o == '2':
                self.read_a_date()
            elif o == '3':
                self.read_all_date()
            elif o == '4':
                self.read_date_range()
            elif o == '5':
                self.update_date()
            elif o == '6':
                self.delete_date()
            elif o == '7':
                return
            else:
                self.view.not_void_option()
        return

    def ask_date(self):
        self.view.ask('Fecha proyeccion(yy-mm-dd): ')
        date = input()
        return [date]

    def create_date(self):
        fecha, = self.ask_date()

        out = self.model.create_date(fecha)
        if out == True:
            self.view.ok(fecha+' '+' ', 'agregado')
        else:
            self.view.error('No se pudo agregar la fecha')
        return
    
    def read_a_date(self):
        self.view.ask('ID fecha: ')
        id_date = input()

        date = self.model.read_a_date(id_date)
        if type(date) == tuple:
            self.view.show_date_header('Datos de la fecha ' + id_date + '')
            self.view.show_a_date(date)
            self.view.show_date_midder()
            self.view.show_date_footer()
        else:
            if date == None:
                self.view.error('La fecha no existe')
            else:
                self.view.error('Problema al leer la fecha')
        return

    def read_all_date(self):
        dates = self.model.read_all_date()
        if type(dates) == list:
            self.view.show_date_header('Todas las fechas')
            
            for date in dates:
                self.view.show_a_date(date)
                self.view.show_date_midder()
            self.view.show_date_footer()
        else:
            self.view.error('Problema al leer las citas')

    def read_date_range(self):
        self.view.ask('Fecha inicial: ')
        date_ini = input()
        self.view.ask('Fecha final: ')
        date_end = input()

        dates = self.model.read_date_range(date_ini, date_end)
        if type(dates) == list:
            self.view.show_date_header('Fechas entre: ' + date_ini + ' y ' + date_end + ' ')
            for date in dates:
                self.view.show_a_date(date)
                self.view.show_date_midder()
            self.view.show_date_footer()
        else:
            self.view.error('Problema al leer las fechas')
        return

    def update_date(self):
        self.view.ask('ID fecha a modificar: ')
        id_date = input()

        date = self.model.read_a_date(id_date)
        if type(date) == tuple:
            self.view.show_date_header('Datos de la fecha ' + id_date + ' ')
            self.view.show_a_date(date)
            self.view.show_date_midder()
            self.view.show_date_footer()
        else:
            if date == None:
                self.view.error('La fehca no existe')
            else:
                self.view.error('Problema al leer la fecha')
            return
        
        self.view.msg('Ingresa valores')
        whole_vals = self.ask_date()
        fields, vals = self.update_list(['fecha'], whole_vals)
        vals.append(id_date)
        vals = tuple(vals)

        out = self.model.update_date(fields, vals)
        print(out)
        if out == True:
            self.view.ok(id_date, 'Actualizada')
        else:
            self.view.error('No se pudo actualizat la fecha')
        return 

    def delete_date(self):
        self.view.ask('ID fecha a borrar: ')
        id_date = input()

        count = self.model.delete_date(id_date)
        if count != 0:
            self.view.ok(id_date, ' se borro')
        else:
            if count == 0:
                self.view.error('La fecha no existe')
            else:
                self.view.error('Problema al borrar la fecha')

    '''
    ******************************************
    ****      Controlador proyeccion      ****     
    ******************************************
    ''' 
    def proyection_menu(self):
        o = '0'
        while o != '8':
            self.view.proyeccion_menu()
            self.view.option('8')

            o = input()
            if o == '1':
                self.create_proyection()
            elif o == '2':
                self.read_a_proyection()
            elif o == '3':
                self.read_all_proyection()
            elif o == '4':
                self.read_proyection_name()
            elif o == '5':
                self.read_proyection_date()
            elif o == '6':
                self.update_proyection()
            elif o == '7':
                self.delete_proyection()
            elif o == '8':
                return
            else:
                self.view.not_void_option()
        return 

    def ask_proyection(self):
        self.read_all_movies()
        self.view.ask('Pelicula: ')
        movie = input()
        self.read_all_language()
        self.view.ask('Idioma: ')
        language = input()
        self.read_all_hall()
        self.view.ask('Sala: ')
        hall = input()
        self.read_all_date()
        self.view.ask('Fecha: ')
        date = input()
        self.view.ask('Hora: ')
        hour = input()
        return [movie, language, hall, date, hour]

    def create_proyection(self):
        pelicula, idioma, sala, fecha, hora = self.ask_proyection()
        
        out = self.model.create_proyeccion(pelicula, idioma, sala, fecha, hora)
        if out == True:
            self.view.ok(pelicula + ' ', 'agregado')
        else:
            self.view.error('No se pudo agregar la proyeccion')
        return

    def read_a_proyection(self):
        self.view.ask('ID proyeccion: ')
        id_proyection = input()

        proyection = self.model.read_a_proyeccion(id_proyection)
        if type(proyection) == tuple:
            self.view.show_proyection_header('Datos del la proyeccion ' +  id_proyection + ' ')
            self.view.show_a_proyection(proyection)
            self.view.show_proyection_midder()
            self.view.show_proyection_footer()
        else:
            if proyection == None:
                self.view.error('La proyeccion no existe')
            else:
                self.view.error('Problema al leer la proyeccion')
        return

    def read_all_proyection(self):
        proyections = self.model.read_all_proyection()
        if type(proyections) == list:
            self.view.show_proyection_header('Todos las proyecciones')
            
            for proyection in proyections:
                self.view.show_a_proyection(proyection)
                self.view.show_proyection_midder()
            self.view.show_proyection_footer()
        else:
            self.view.error('Problema al leer las proyecciones')

    def read_proyection_name(self):
        self.view.ask('Nombre: ')
        name = input()

        proyections  = self.model.read_proyection_name(name)
        if type(proyections) == list:
            self.view.show_proyection_header('Proyecciones de: ' + name + ' ')
            
            for proyection in proyections:
                self.view.show_a_proyection(proyection)
                self.view.show_proyection_midder()
            self.view.show_proyection_footer()
        else:
            self.view.error('Problema al leer las proyecciones.')
        return

    def read_proyection_date(self):
        self.view.ask('Fecha (yy-mm-dd): ')
        date = input()

        proyections  = self.model.read_proyection_date(date)
        if type(proyections) == list:
            self.view.show_proyection_header('Proyecciones en la fecha: ' + date + ' ')
            
            for proyection in proyections:
                self.view.show_a_proyection(proyection)
                self.view.show_proyection_midder()
            self.view.show_proyection_footer()
        else:
            self.view.error('Problema al leer las proyecciones.')
        return

    def read_proyection_time(self):
        self.view.ask('Hora: ')
        time = input()
        self.view.ask('Pelicula: ')
        movie = input()

        movie = self.model.read_proyection_time(time, movie)
        if type(movie) == list:
            self.view.show_proyection_header('Proyecciones en la hora: ' + time + ' ')
            
            for proyection in movie:
                self.view.show_a_proyection(proyection)
                self.view.show_proyection_midder()
            self.view.show_proyection_footer()
        else:
            self.view.error('Problema al leer las proyecciones.')
        return

    def update_proyection(self):
        self.view.ask('ID proyeccion a modificar: ')
        id_proyection = input()

        proyection = self.model.read_a_proyeccion(id_proyection)
        if type(proyection) == tuple:
            self.view.show_proyection_header('Datos de la proyeccion ' + id_proyection + ' ')
            self.view.show_a_proyection(proyection)
            self.view.show_proyection_midder()
            self.view.show_proyection_footer()
        else:
            if proyection == None:
                self.view.error('La proyeccion no existe')
            else:
                self.view.error('Problema al leer la proyeccion')
            return
        
        self.view.msg('Ingresa los valores a modificar (vacio para omitir el campo): ')
        whole_vals = self.ask_proyection()
        fields, vals = self.update_list(['pelicula_id', 'idioma_id', 'sala_id', 'fecha_id', 'hora'], whole_vals)
        vals.append(id_proyection)
        vals = tuple(vals)

        out = self.model.update_proyection(fields, vals)
        if out == True:
            self.view.ok(id_proyection, ' Actualizado')
        else:
            self.view.error('No se pudo actulizar la proyeccion.')
        return 

    def delete_proyection(self):
        self.view.ask('ID proyeccion a borrar: ')
        id_proyeccion = input()

        count = self.model.delete_proyection(id_proyeccion)
        if count != 0:
            self.view.ok(id_proyeccion, ' se borro')
        else:
            if count == 0:
                self.view.error('La proyeccion no existe.')
            else:
                self.view.error('Problema al borrar la proyeccion.')

    '''
    *********************************************
    ****      Controlador Cine Usuarios      ****     
    ********************************************* 
    '''
    def user_menu(self, a):
        o = '0'
        while o != 4:
            # Mostramos los datos del usuario.
            user = self.model.read_a_user(a)
            self.view.show_admin_header('Usuario en uso.')
            self.view.show_a_admin(user)
            self.view.show_admin_footer()

            self.view.menu_user()
            self.view.option('4')

            o = input()
            if o == '1':
                self.movies_user()
                self.clear()
            elif o == '2':
                self.proyection_user()
                self.clear()
            elif o == '3':
                self.ticket_menu(a)
                self.clear()
            elif o == '4':
                return
            else:
                self.view.not_void_option()
        return

    def ask_acount(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        last1 = input()
        self.view.ask('Apellido materno: ')
        last2 = input()
        self.view.ask('Correo: ')
        email = input()
        self.view.ask('Contraseña: ')
        password = input()
        return [name, last1, last2, email, password]


    '''
    *************************************************
    ****      Controlador peliculas usuario      ****     
    *************************************************
    ''' 
    def movies_user(self):
        o = '0'
        while o != '5':
            self.view.movies_user()
            self.view.option('5')

            o = input()
            if o == '1':
                self.read_all_movies()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_movie_clasification()
            elif o == '4':
                self.read_movies_name()
            elif o == '5':
                return
            else:
                self.view.not_void_option()
        return
    
    '''
    **************************************************
    ****      Controlador proyeccion usuario      ****     
    **************************************************
    ''' 
    def proyection_user(self):
        o = '0'
        while o != '6':
            self.view.proyection_user()
            self.view.option('6')

            o = input()
            if o == '1':
                self.read_all_proyection()
            elif o == '2':
                self.read_a_proyection()
            elif o == '3':
                self.read_proyection_name()
            elif o == '4':
                self.read_proyection_date()
            elif o == '5':
                self.read_proyection_time()
            elif o == '6':
                return
            else:
                self.view.not_void_option()
        return
    
    '''
    ***************************************
    ****      Controlador boleto       ****     
    ***************************************
    '''     
    def ticket_menu(self, a):
        o = '0'
        while o != '4':
            self.view.ticket_menu()
            self.view.option('4')

            o = input()
            if o == '1':
                self.create_ticket(a)
            elif o == '2':
                self.read_ticket(a)
            elif o == '3':
                self.read_all_purchase(a)
            elif o == '4':
                return
            else:
                self.view.not_void_option()
        return

    def ask_ticket(self):
        o = True
        while o != False:
            # Escoge un boleto dependiendo si es adulto o no
            self.view.msg('\n1. Boleto adulto: $60\n2. Boleto nino: $30')
            self.view.ask('Opc: ')
            a = input()

            precio = 0
            if a == '1':
                precio = precio + 60
                o = True   
                return precio 
            elif a == '2':
                precio = precio + 30
                o = True
                return precio
            else:
                self.view.not_void_option()
        return precio

    def create_ticket(self, a):
        user = self.model.read_a_user(a)
        if type(user) == tuple:
            # Selecciona una función
            self.read_all_proyection()
            self.view.ask('Selecciona tu funcion: ')
            id_proyection = input()

            precio = self.ask_ticket()

            # Toma los valores de la fila y columna de la sala
            fila, columna = self.model.read_seat_hall(id_proyection)

            # Crea una matriz y muestra los asientos
            self.view.msg('------------Pantalla-----------')
            sala = []
            for i in range(fila):
                seats = []
                for j in range(columna):
                    n_seats = []
                    n_seats.append(s.ascii_lowercase[i])
                    n_seats.append(str(j))
                    s_create = ''.join(n_seats)
                    seats.append(s_create)
                sala.append(seats)

            selected_seat = self.model.read_ticket_proyection(id_proyection)
            occupied_seats = []
            for seats in selected_seat:
                occupied_seats.append(seats[2])

            m1 = []
            if occupied_seats != None:
                for fila in sala:
                    for seat in occupied_seats:
                        if seat in fila:
                            indx = fila.index(seat)
                            fila[indx] = 'X'
                            m1.append(seat)    
                    print(fila)
            else:
                for fila in sala:
                    print(sala)

            self.view.ask('\nSeleccione un asiento (X ocupado): ')
            select_s = input()

            x = self.model.seat_available(occupied_seats, select_s)
            while x != True:
                self.view.ask('Asiento ocupado, seleccione otro asiento: ')
                select_s = input()
                x = self.model.seat_available(occupied_seats, select_s)

            # Crea boleto
            self.model.crate_ticket(id_proyection, select_s, precio)

            ticket_seat = self.model.read_ticket_seat(select_s)
            id_ticket_s = ticket_seat[0]

            # Crear compra de usuario
            self.model.crate_purchase(a, id_ticket_s, precio)
            selected_seat = self.model.read_ticket_proyection(id_proyection)

            for seat in selected_seat:
                occupied_seats.append(seat[2])
            
            ticket_record = self.model.read_a_ticket(id_proyection)
            self.view.show_ticket_header('Tu ticket:')
            self.view.show_a_ticket(ticket_record)

        else:
            self.view.error('Problema al crear el ticket.')

    def read_ticket(self, a):
        self.view.ask('ID ticket: ')
        id_ticket = input()

        ticket = self.model.read_a_ticket_user(a)
        if type(ticket) == tuple:
            self.view.show_ticket_header('Datos del ticket ' +  id_ticket + ' ')
            self.view.show_a_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('El ticket no existe')
            else:
                self.view.error('Problema al leer el ticket')
        return

    def read_all_purchase(self, a):
        purchase = self.model.read_all_pruchase(a)
        if type(purchase) == list:
            self.view.show_ticket_header('Todas las compras.')

            for user in purchase:
                self.view.show_a_purchase(user)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('Problema al leer tus compras.')