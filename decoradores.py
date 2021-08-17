from typing import Callable


def mayusculas(func: Callable) -> Callable:
    def envoltura(texto: str) -> str:
        return func(texto).upper()
    
    return envoltura


@mayusculas
def mensaje(nombre: str) -> str:
    return f'{nombre}, recibiste un mensaje'


def run():
    print(mensaje('cesar'))


if __name__ == '__main__':
    run()