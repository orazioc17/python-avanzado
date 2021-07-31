def repetir_string(n: int):

    def repetir(string: str) -> str:
        assert type(string) == str, 'Solo puedes utilizar cadenas'
        return n * string

    return repetir


def run():
    repetir_5 = repetir_string(5)

    print(repetir_5('Facundo'))


if __name__ == '__main__':
    run()