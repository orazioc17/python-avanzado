from datetime import datetime
import pandas as pd
from pandas._config.config import options

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

ANIOS_TO_HORAS = 8760


def convert_horas(func):
    def wrapper(*args, **kwargs):
        anios = func(*args, **kwargs)
        horas = anios * ANIOS_TO_HORAS
        return f'Esta persona tiene {horas} horas de edad' 
    return wrapper


class Persona:

    def __init__(self, nombre='', anio_nacimiento=1900):
        self.__nombre = nombre
        self.__anio_nacimiento = anio_nacimiento
        self.__anio_actual = datetime.now().year
        self.__anios= self.__anio_actual - self.__anio_nacimiento
    
    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def get_nacimiento(self) -> str:
        return self.__anio_nacimiento

    def set_nacimiento(self, anio_nacimiento: int):
        self.__anio_nacimiento = anio_nacimiento
        self.__anios = self.__anio_actual - self.__anio_nacimiento

    def get_actual(self) -> float:
        return self.__anio_actual

    def set_actual(self, anio_actual: str):
        self.__anio_actual = anio_actual

    @convert_horas
    def get_edad(self):
        return self.__anios 


class Estudiante(Persona):

    def __init__(self, nombre, anio_nacimiento, nota1, nota2, nota3):
        super().__init__(nombre=nombre, anio_nacimiento=anio_nacimiento)
        self.nota1: int = nota1
        self.nota2: int = nota2
        self.nota3: int = nota3

    def get_nombre(self) -> str:
        return super().get_nombre()
    
    def get_edad(self):
        return super().get_edad()

    def total(self):
        nota1 = self.nota1 * 0.3
        nota2 = self.nota2 * 0.3
        nota3 = self.nota3 * 0.4
        total = nota1 + nota2 + nota3
        nombre = self.get_nombre()
        return f'La nota final de {nombre} es {total}'

    
def run():
    orazio = Estudiante(nombre='Orazio', anio_nacimiento=1999, nota1=19, nota2=20, nota3=12)
    paula = Estudiante(nombre='Paula', anio_nacimiento=1999, nota1=20, nota2=20, nota3=20)
    pippo = Estudiante(nombre='Filippo', anio_nacimiento=2001, nota1=13, nota2=9, nota3=12)
    salva = Estudiante(nombre='Salvatore', anio_nacimiento=2001, nota1=1, nota2=2, nota3=4)
    caro = Estudiante(nombre='Carolina', anio_nacimiento=1981, nota1=11, nota2=20, nota3=16)
    papa = Estudiante(nombre='Sebastiano', anio_nacimiento=1976, nota1=19, nota2=19, nota3=10)
    nonna = Estudiante(nombre='Nonna', anio_nacimiento=1960, nota1=19, nota2=20, nota3=12)
    abuela = Estudiante(nombre='Abuela', anio_nacimiento=1965, nota1=1, nota2=7, nota3=14)
    pao = Estudiante(nombre='Paola', anio_nacimiento=2008, nota1=10, nota2=20, nota3=3)

    cols = ['Nombre', 'Edad', 'Nota 1', 'Nota 2', 'Nota 3', 'Definitiva']

    lista_estudiantes = [
        orazio,
        paula,
        pippo,
        salva,
        caro,
        papa,
        nonna,
        abuela,
        pao
    ]

    vals = []

    for estudiante in lista_estudiantes:
        lista = []

        lista.append(estudiante.get_nombre())
        lista.append(estudiante.get_edad())
        lista.append(estudiante.nota1)
        lista.append(estudiante.nota2)
        lista.append(estudiante.nota3)
        lista.append(estudiante.total())

        vals.append(lista)

    df_estudiantes = pd.DataFrame(vals, columns=cols, index=[estudiante.get_nombre() for estudiante in lista_estudiantes])

    print(df_estudiantes)


if __name__ == '__main__':
    run()