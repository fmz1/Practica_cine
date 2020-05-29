from model.model import Model
from controller.controller import Controller
import string as s

m = Model()

'''
# Pruebas usuarios
m.create_user('Francisco', 'Zarate', 'Lopez', 'fco@gmail.com', '1234', '1')
m.create_user('Carlos', 'Cano', 'Almanza', 'cano@hotmail.com', '4321', '0')
m.create_user('Carlos', 'Almanza', 'Guerrero', 'kano@hotmail.com', '1312', '0')

#Pruebas clasificacion
m.create_classification('AA', 'Pelliculas para todo el publico y que sean comprensibles para niños')
m.create_classification('A', 'Publico en general')
m.create_classification('B', 'Películas para adolescentes de 12 años en adelante.')
m.create_classification('B15', 'Película no recomendable para menores de 15 años de edad.')
m.create_classification('C' , 'Películas para adultos de 18 años en adelante')

#Pruebas pelicula
m.create_movie(1, 'SHREK', '2001-06-29', 'Un ogro llamado Shrek vive en su pantano, ')
m.create_movie(5, 'Matrix', '1999-03-19', 'Un experto en computadoras')
m.create_movie(2, 'game', '2020-04-26', 'Sinopsis pelicula')

#Pruebas idioma
m.create_language('LAT')
m.create_language('ESP')
m.create_language('ING')
m.create_language('JP')

#Pruebas sala
m.create_hall(5, 2)
m.create_hall(4, 5)
m.create_hall(3, 5)

#Pruebas fecha
m.create_date('2020-05-20')
m.create_date('2020-05-21')
m.create_date('2020-05-22')
m.create_date('2020-05-23')

# Pruebas proyecciones.
m.create_proyeccion(1, 1, 1, 3, '12:00')
m.create_proyeccion(2, 1, 1, 1, '14:00')
m.create_proyeccion(3, 3, 2, 4, '12:00')
'''

c = Controller()
c.start()

m.close_db()