import random
import math
import time

class RandomValue:

    def getPrime(self, security_level):

        data_base = {
            0: "prime\\less safe.txt",
            1: "prime\\balanced.txt",
            2: "prime\\safe.txt",
            3: "prime\\safest.txt"
        }

        try:
            prime_db = open(data_base[security_level], "r")
            prime_list = prime_db.read().split()
            return int(prime_list[random.randint(0, len(prime_list))])

        except FileNotFoundError:
            print("File or directory not found")
            return -1

    def prime(self, start, end):
        """retorna um número primo randômico"""

        while True:
            prime = 6*random.randint(start, end) - 1
            if self.isPrime2(prime):
                return prime
       
    def exp(self, p, q):
        """retorna um expoente randômico"""

        φ = (p - 1) * (q - 1)
        exp = random.randint(φ - p, φ - 1)  # o expoente deve ser maior que 1000 e menor que φ

        while not self.isCoPrime(φ, exp):
            exp -= 1

        return exp

    @staticmethod
    def isPrime(x):
        """verifica se x é um número primo"""

        if x % 2 == 0:
            return False

        i = 3
        root = math.sqrt(x)
        while i <= root:
            if x % i == 0: return False
            i += 2
            
        return True

    def isPrime2(self, n):

        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False

        i = 5
        w = 2

        while i * i <= n:
            if n % i == 0:
                return False

            i += w
            w = 6 - w

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

