import os


class RSA:

    def encrypt(self, n, e, file_name):

        # OPEN INPUT FILE AND OUTPUT FILE
        file = open(file_name, 'rb')
        outputFile = open(f'{file_name}.rsa', 'w')

        # RUN ORIGINAL FILE
        while 1:
            M = file.read(1)
            if not M:
                break
            C = self.QuickMod(ord(M), e, n)
            outputFile.write(f'{C} ')

        file.close()
        outputFile.close()

    def decrypt(self, p, q, e, file_name):

        # OPEN INPUT FILE AND OUTPUT FILE
        file = open(file_name, 'r')
        output_file = open(f'(original){file_name[:-3]}', 'wb')

        # GETS THE INVERSE KEY
        d = self.inverse(e, (p - 1) * (q - 1))

        # RUN ENCRYPTED FILE/MESSAGE
        for line in file:
            lineValues = line.split()
            for C in lineValues:
                M = self.QuickMod(int(C), d, p * q)

                # convert int to bytes type and write in output file
                output_file.write(M.to_bytes(1, byteorder='big'))

        file.close()
        output_file.close()

    @staticmethod
    def dir():
        'lista os arquivos do diretório relativo'
        for f in os.listdir():
            print(f)

    @staticmethod
    def QuickMod(base, exp, n):
        """retorna o resultado de base^exp mod(n) através da exponenciação rápida"""

        result = 1
        while exp > 0:
            if exp & 1:
                result = (result * base) % n
            base = (base ** 2) % n
            exp = exp >> 1

        return result

    @classmethod
    def linearOperation(cls, a, b, mdc, i):
        """resolve a operação linear do tipo mdc(a, b) = sa + tb = 1"""
        t = -int(a / b)
        r = a % b
        mdc.append([1, a, t, b])

        if r == 1:
            return mdc

        # recebe a ultima operação do mdc cujo resultado é 1 ( mdc(a, b) = sa + tb = 1 )
        inverseLine = cls.linearOperation(b, r, mdc, i + 1)

        s = inverseLine[i][0]
        t = inverseLine[i][2]
        inverseLine[i - 1][0] *= t
        inverseLine[i - 1][2] *= t
        inverseLine[i - 1][2] += s

        inverseLine.remove(inverseLine[i])
        return inverseLine  # retorna a última lista com o inverso incluso

    def inverse(self, e, φ):
        """recebe e, φ; retorna inverso de e ≡ 1 mod(φ)"""
        inverseLine = self.linearOperation(e, φ, [], 1)
        inverse = inverseLine[0][0]

        if inverse < 0:
            return inverse + φ
        if inverse > φ:
            return inverse % φ
        else:
            return inverse
