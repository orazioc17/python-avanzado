from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()

        total_time = final_time - initial_time
        print(f'La funcion tardo {total_time.total_seconds()} ejecutandose')

    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    print(a + b)


@execution_time
def saludo(nombre: str ='Cesar') -> str:
    print(f'Hola {nombre}')


def run():
    random_func()
    suma(1, 2)
    saludo()
    saludo(nombre='Orazio')


if __name__ == '__main__':
    run()