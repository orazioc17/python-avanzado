from time import sleep


def fibonacci_generator(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    max = max

    while True:

        if max:
            if n1 + n2 > max:
                break

        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':
    fibonacci = fibonacci_generator(1000)
    for element in fibonacci:
        print(element)
        sleep(0.4)
