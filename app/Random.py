import random
import math


class RandomValue:

    def randomPrime(self):
        """retorna um número primo randômico"""

        randPrime = random.randint(10000, 100000)

        while not self.isPrime(randPrime):
            randPrime += 1

        return randPrime

    def randomExp(self, p, q):
        """retorna um expoente randômico"""

        φ = (p - 1) * (q - 1)
        exp = random.randint(1000, φ - 1)  # o expoente deve ser maior que 1000 e menor que φ

        while not self.isCoPrime(φ, exp):
            exp -= 1

        return exp

    @staticmethod
    def isPrime(x):
        """verifica se x é um número primo"""

        if x == 1 or x == 0: return False
        i = 2
        while i <= math.sqrt(x):
            if x % i == 0: return False
            i += 1
        return True

    @classmethod
    def isCoPrime(cls, Dividendo, divisor):
        """verifica se o Dividendo e o divisor são coprimos"""

        if divisor == 0: return False
        resto = Dividendo % divisor
        if resto == 0:
            if divisor == 1:
                return True
            else:
                return False

        return cls.isCoPrime(divisor, resto)

