import time


class Fibonacci:

    def __init__(self, max=None):
        self.max = max
    
    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.num2 <= self.max:

            if self.num1 + self.num2 > self.max:
                raise StopIteration
            else:

                if self.counter == 0:
                    self.counter += 1
                    return self.num1
                elif self.counter == 1:
                    self.counter += 1
                    return self.num2
                else:
                    self.aux = self.num1 + self.num2
                    self.num1, self.num2 = self.num2, self.aux
                    self.counter += 1
            
                    return self.aux
        else:
            raise StopIteration



if __name__ == '__main__':
    fibo = Fibonacci(100000)

    for number in fibo:
        print(number)
        time.sleep(0.3)

    fibo2 = Fibonacci(500)

    for number in fibo2:
        print(number)
        time.sleep(0.1)