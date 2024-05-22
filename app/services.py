from .models import Estudiante, Profesor, Curso, Direccion  
from datetime import date


def crear_curso(codigo, nombre, version):
    nuevo_curso = Curso(codigo=codigo, nombre=nombre, version=version)
    nuevo_curso.save()
    return nuevo_curso

def crear_profesor(rut, nombre, apellido):
    nuevo_profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido)
    nuevo_profesor.save()
    return nuevo_profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac):
    nuevo_estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac)
    nuevo_estudiante.save()
    return nuevo_estudiante

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante):
    estudiante = Estudiante.objects.get(rut=estudiante)
    nueva_direccion = Direccion(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    nueva_direccion.save()
    return nueva_direccion   

def obtiene_estudiante(rut):
    try:
        estudiante = Estudiante.objects.get(rut=rut)
        print(f'RUT: {estudiante.rut} Nombres: {estudiante.nombre} Apellido: {estudiante.apellido} Fecha de Nacimiento: {estudiante.fecha_nac}')
    except Estudiante.DoesNotExist:
        print(f'No se encontró al estudiante con el RUT: {rut}')

def obtiene_profesor(rut):
    try:
        profesor = Profesor.objects.get(rut=rut)
        print(f'RUT: {profesor.rut} Nombres: {profesor.nombre} Apellido: {profesor.apellido}')
    except Profesor.DoesNotExist:
        print(f'No se encontró al profesor con el RUT: {rut}')

def obtiene_curso(codigo):
    try:
        curso = Curso.objects.get(codigo=codigo)
        print(f'Código: {curso.codigo} Nombre: {curso.nombre} Versión: {curso.version}')
    except:
        print(f'No se encontró al curso con el código: {codigo}')
    

def agregar_profesor_a_curso(codigo, rut):
    curso = Curso.objects.get(codigo=codigo)
    profesor = Profesor.objects.get(rut=rut)
    curso.profesor.add(profesor)
    return "Se agregó con exito el profesor al curso"

def agrega_cursos_a_estudiantes(codigo, rut):
    estudiante = Estudiante.objects.get(rut=rut)
    curso = Curso.objects.get(codigo=codigo)
    curso.estudiante.add(estudiante)
    return "Se agregó con exito el estudiante al curso"

def imprime_estudiante_curso(rut): 
    try:
        estudiante = Estudiante.objects.get(rut=rut)
        cursos_estudiante = estudiante.curso_set.all()
        print(f'RUT: {estudiante.rut} Nombre: {estudiante.nombre} {estudiante.apellido}')
        print('Cursos: ')
        for curso in cursos_estudiante:
            print(f' - {curso.nombre} - ({curso.version})')         
    except Estudiante.DoesNotExist:
        print(f'No se encontró al estudiante con el RUT: {rut}')
    
    
    