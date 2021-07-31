from typing import Dict, List, Tuple

"""Este static typing se implemento desde la version 6"""


def ejemplo_mas_complejo():
    CoordinatesType = List[Dict[str,Tuple[int,int]]]

    coordinates: CoordinatesType = [
        {
            'coord1': (1,2),
            'coord2': (3,5)
        },
        {
            'coord1': (0,1),
            'coord2': (2,5)
        },
    ]


def static_typing():
    positives: List[int] = [1,2,3,4,5]

    users: Dict[str, int] = {
        'argentina': 1,
        'mexico': 34,
        'colombia': 42,
    }

    countries: List[Dict[str,str]] = [
        {
            'name': 'Argentina',
            'people': '6423948'
        },
        {
            'name': 'Mexico',
            'people': '64232343948'
        },
        {
            'name': 'Colombia',
            'people': '6428'
        },
    ]

    numbers: Tuple[int, float, int] = (1,1.1,2)


def suma(a: int, b: int) -> int:
    """Ejemplo de funcion con tipado estatico, se declaran los tipos en los 
    parametros y con la flechita el tipo de dato que retorna la funcion
    """
    return a + b


def run():
    a: int = 2
    b: str = 'Hola mundo'
    c: bool = False

    if not c:
        print(f'La variable a es de tipo {type(a)} y contiene el valor {a}')
        print(f'La variable a es de tipo {type(b)} y contiene el valor {b}')
        print(f'La variable a es de tipo {type(c)} y contiene el valor {c}')

    print(suma(2,6))
    print(suma(2,3.5))


if __name__ == '__main__':
    run()