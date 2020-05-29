from model.model import Model

class View:
    # A view for cine DB
    def start(self):
        print('*****************************************')
        print('*      Bienvenido a nuestro Cine        *')
        print('*****************************************')

    def end(self):
        print('******************')
        print('* Hasta la vista *')
        print('******************')

    def option(self, last):
        print('Seleccione una opción (1-'+last+'): ', end = '')
    
    def not_void_option(self):
        print('¡Opción no valida\nIntente de nuevo¡')

    def ask(self, output):
        print(output, end = '')
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    #___________________ Vista usuario administrador______________________#
    def menu_admin(self):
        print('*****************************')
        print('*     Menu Administrador    *')
        print('*****************************')
        print('1. Adminsitrar usuarios.')
        print('2. Clasificaciones.')
        print('3. Peliculas.')
        print('4. Idioma.')
        print('5. Salas')
        print('6. Fechas.')
        print('7. Proyecciones.')
        print('8. Salir.')
    
    # Mostrar administrador.
    def show_a_admin(self, record):
        print(f'{record[0]:<3}|{record[1]:<14}|{record[2]:<14}|')

    def show_admin_header(self, header):
        print(header.center(53, '*'))
        print('ID'.ljust(3) + '|' + 'Nombre'.ljust(14) + '|' + 'Apellido'.ljust(14) + '|')
        print('-'*33)    

    def show_admin_footer(self):
        print('-'*33)

    #_________________________ Vista usuarios ___________________________#
    def user_admin(self):
        print('****************************')
        print('*     Sub menu usuarios    *')
        print('****************************')
        print('1. Crear usuarios')
        print('2. Ver un usuario.')
        print('3. Ver todos los usuarios.')
        print('4. Buscar usuario por nombre.')
        print('5. Actualizar usuario.')
        print('6. Borrar usuario.')
        print('7. Salir.')

    def show_a_user(self, record):
        print(f'{record[0]:<3}|{record[1]:<14}|{record[2]:<18}|{record[3]:<18}|{record[4]:<18}|{record[6]:<12}|')

    def show_user_header(self, header):
        print(header.center(53, '*'))
        print('ID'.ljust(3) + '|' + 'Nombre'.ljust(14) + '|' + 'Apellido paterno'.ljust(18) + '|' + 'Apellido materno'.ljust(18) + '|' + 'Correo'.ljust(18) + '|' + 'Tipo usuario'.ljust(12) + '|')
        print('-'*89)    

    def show_user_midder(self):
        print('-'*89)

    def show_user_footer(self):
        print('-'*89)

    #______________________ Vista clasificacion ______________________#
    def clasification_menu(self):
        print('*******************************')
        print('* -- Submenu Clasificacion -- *')
        print('*******************************')
        print('1. Agregar clasificacion.')
        print('2. Mostrar una clasificacion.')
        print('3. Mostrar todas las clasificaciones.')
        print('4. Mostrar una clasificacion por nombre.')
        print('5. Actualizar clasificacion.')
        print('6. Borrar clasificacion.')
        print('7. Regresar.')

    def show_a_clasificacion(self, record):
        print(f'{record[0]:<3}|{record[1]:<14}|{record[2]:<60}|')

    def show_clasification_header(self, header):
        print(header.center(78, '*'))
        print('ID'.ljust(3) + '|' + 'Clasificacion'.ljust(14) + '|' + 'Descr'.ljust(60) + '|')
        print('-'*80)

    def show_clasification_midder(self):
        print('-'*80)

    def show_clasification_footer(self):
        print('-'*80)

    #------------------- Vista de peliculas ---------------------------#
    def movies_menu(self):
        print('************************')
        print('* -- Submenu Peliculas -- *')
        print('************************')
        print('1. Agregar pelicula.')
        print('2. Mostrar una pelicula.')
        print('3. Mostrar todas las peliculas.')
        print('4. Buscar pelicula por clasificación.')
        print('5. Buscar pelicula por nombre')
        print('6. Actualizar pelicula.')
        print('7. Borrar pelicula.')
        print('8. Regresar.')

    def show_a_movie(self, record):
        print(f'{record[0]:<3}|{record[2]:<20}|{record[1]:<15}|{record[3]}| {record[4]:<50}|')
     
    def show_movie_header(self, header):
        print(header.center(53, '*'))
        print('ID'.ljust(3) + '|' + 'Titulo'.ljust(20) + '|' + 'Clasificacion'.ljust(15) + '|' + 'Fecha'.ljust(10) + '|' + ' ' + 'Sinopsis'.ljust(50) + '|')
        print('-'*104)

    def show_movie_midder(self):
        print('-'*104)

    def show_movie_footer(self):
        print('*'*104)

    #______________________ Vista de idiomas __________________________#
    def idioma_menu(self):
        print('********************************')
        print('* --    Submenu Idiomas     -- *')
        print('********************************')
        print('1. Agregar idioma.')
        print('2. Mostrar un idioma.')
        print('3. Mostrar todos los idiomas.')
        print('4. Buscar idioma por nombre.')
        print('5. Actualizar idioma.')
        print('6. Borrar idioma.')
        print('7. Regresar.')

    def show_a_idioma(self, record):
        print(f'{record[0]:<3}|{record[1]:<6}|')

    def show_idioma_header(self, header):
        print(header.center(78, '*'))
        print('ID'.ljust(3) + '|' + 'Idioma'.ljust(6) + '|')
        print('-'*11)

    def show_idioma_midder(self):
        print('-'*11)

    def show_idioma_footer(self):
        print('-'*11)

    #________________________ Vista salas __________________________#
    def salas_menu(self):
        print('***********************************')
        print('* --     Submenu salas         -- *')
        print('***********************************')
        print('1. Agregar sala.')
        print('2. Ver una sala.')
        print('3. Ver todas las salas.')
        print('4. Ver sala por tamaño')
        print('5. Actualizar sala.')
        print('6. Borrar sala.')
        print('7. Regresar.')

    def show_a_hall(self, record):
        print(f'{record[0]:<3}|{record[1]:<5}|{record[2]:<8}|')     
      
    def show_hall_header(self, header):
        print(header.center(20, '*'))
        print('ID'.ljust(3) + '|' + 'Fila'.ljust(5) + '|' + 'Columna'.ljust(8) + '|')
        print('-'*19)

    def show_hall_midder(self):
        print('-'*19)

    def show_hall_footer(self):
        print('*'*19)

    #_________________________ Vista fecha __________________________#
    def fecha_menu(self):
        print('*************************************')
        print('* --        Submenu fecha        -- *')
        print('*************************************')
        print('1. Agregar fecha.')
        print('2. Ver una fecha.')
        print('3. Ver todas las fechas.')
        print('4. Ver una fecha en un rango.')
        print('5. Actualizar fecha.')
        print('6. Borrar fecha.')
        print('7. Regresar.')

    def show_a_date(self, record):
        print(f'{record[0]:<3}|{record[1]}|')     

    def show_date_header(self, header):
        print(header.center(18, '*'))
        print('ID'.ljust(3) + '|' + 'Fecha'.ljust(10) + '|')
        print('-'*15)

    def show_date_midder(self):
        print('-'*15)

    def show_date_footer(self):
        print('*'*15)

    #------------------- Vista proyeccion ---------------------------#
    def proyeccion_menu(self):
        print('******************************************')
        print('* --        Submenu proyeccion        -- *')
        print('******************************************')
        print('1. Agregar proyeccion.')
        print('2. Ver una proyeccion.')
        print('3. Ver todas las proyecciones.')
        print('4. Ver proyeccion nombre.')
        print('5. Ver proyecciones fecha.')
        print('6. Actualizar proyeccion.')
        print('7. Borrar proyeccion.')
        print('8. Regresar.')

    def show_a_proyection(self, record):
        print(f'{record[0]:<3}|{record[1]:<10}|{record[2]:<6}|{record[3]:<4}|{record[4]}| {record[5]:<6}|')

    def show_proyection_header(self, header):
        print(header.center(18, '*'))
        print('ID'.ljust(3) + '|' + 'Pelicula'.ljust(10) + '|' + 'Idioma'.ljust(4) + '|' + 'Sala'.ljust(3) + '|' + ' Fecha'.ljust(10) + '|' + 'Hora'.ljust(7) + '|')
        print('-'*46)

    def show_proyection_midder(self):
        print('-'*46)

    def show_proyection_footer(self):
        print('*'*46)


    #________________________ Vista usuario __________________________#
    def menu_user(self):
        print('*****************************')
        print('*        Menu Usuario       *')
        print('*****************************')
        print('1. Ver pelicula.')
        print('2. Proyecciones')
        print('3. Boleto.')
        print('4. Salir.')

    #_____________________ Vista peliculas usuario ______________________#
    def movies_user(self):
        print('***********************************')
        print('***      Submenu Peliculas      ***')
        print('***********************************')
        print('1. Ver todas las peliculas')
        print('2. Ver una pelicula.')
        print('3. Buscar pelicula por clasificacion.')
        print('4. Buscar pelicula por nombre.')
        print('5. Salir.')

    #___________________ Vista proyecciones usuario ____________________#
    def proyection_user(self):
        print('**************************************')
        print('***      Submenu Proyecciones      ***')
        print('**************************************')
        print('1. Ver todas las proyecciones.')
        print('2. Ver una proyeccion.')
        print('3. Buscar una proyeccion por nombre pelicula.')
        print('4. Buscar proyeccion por fecha.')
        print('5. Buscar proyeccion por hora.')
        print('6. Salir.')

    #__________________________ Vista boletos _________________________#
    def ticket_menu(self):
        print('**************************************')
        print('* --        Submenu boleto        -- *')
        print('**************************************')
        print('1. Comprar boleto.')
        print('2. Ver un ticket')
        print('3. Ver todas mis compras.')
        print('4. Regresar.')

    def show_a_ticket(self, record):
        print('ID: ', record[0])
        print('Asiento: ', record[1])
        print('Sala: ', record[2])
        print('Pelicula: ', record[3])
        print('Fecha: ', record[4])
        print('Hora: ', record[5])
    
    def show_a_purchase(self, record):
        print('ID compra: ', record[0])
        print('ID ticket: ', record[1])
        print('Pelicula: ', record[2])
        print('Total: ', record[3])

    def show_ticket_header(self, header):
        print(header.center(18, '*'))
        print('-'*18)

    def show_ticket_midder(self):
        print('-'*18)

    def show_ticket_footer(self):
        print('*'*18)