from msilib.schema import Error
import os
from turtle import st
from app.char_codec import CharCodec


class RSA:

    def encrypt(self, n: int, e: int, content: str) -> str:

        outputContent = ""
        # RUN ORIGINAL FILE
        for M in content:
            C = self.__QuickMod(ord(M), e, n)
            outputContent += str(C) + ' '

        return outputContent[:-1] # retorna sem o último caractere

    def encryptChar(self, n: int, e: int, M: str) -> str:
        C = self.__QuickMod(ord(M), e, n)
        return C

    def decrypt(self, p: int, q: int, e: int, content: str) -> str:
        
        outputContent = ""
        # GETS THE INVERSE KEY
        d = self.__inverse(e, (p - 1) * (q - 1))

        # RUN ENCRYPTED MESSAGE        
        contentValues = content.split()
        for C in contentValues:
            M = self.__QuickMod(int(C), d, p * q)            
            # convert int to bytes type and write in output file
            outputContent += chr(M)

        return outputContent

    def decryptChar(self, p: int, q: int, e: int, C: str) -> str:
        d = self.__inverse(e, (p - 1) * (q - 1))
        M = self.__QuickMod(int(C), d, p * q)
        return str(M)

    @staticmethod
    def __QuickMod(base, exp, n):
        """retorna o resultado de base^exp mod(n) através da exponenciação rápida"""

        result = 1
        while exp > 0:
            if exp & 1:
                result = (result * base) % n
            base = (base ** 2) % n
            exp = exp >> 1

        return result


    @classmethod
    def __linearOperation(cls, a, b, mdc, i):
        """resolve a operação linear do tipo mdc(a, b) = sa + tb = 1"""
        t = -int(a / b)
        r = a % b
        mdc.append([1, a, t, b])

        if r == 1:
            return mdc

        # recebe a ultima operação do mdc cujo resultado é 1 ( mdc(a, b) = sa + tb = 1 )
        inverseLine = cls.__linearOperation(b, r, mdc, i + 1)

        s = inverseLine[i][0]
        t = inverseLine[i][2]
        inverseLine[i - 1][0] *= t
        inverseLine[i - 1][2] *= t
        inverseLine[i - 1][2] += s

        inverseLine.remove(inverseLine[i])
        return inverseLine  # retorna a última lista com o inverso incluso

    def __inverse(self, e, φ):
        """recebe e, φ; retorna inverso de e ≡ 1 mod(φ)"""
        inverseLine = self.__linearOperation(e, φ, [], 1)
        inverse = inverseLine[0][0]

        if inverse < 0:
            return inverse + φ
        if inverse > φ:
            return inverse % φ
        else:
            return inverse
