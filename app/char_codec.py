
class CharCodec:

    @staticmethod
    def bytesToStr(file, remove_char=-1):
        str=""
        while True:
            byte = file.read(1)

            if not byte:
                break
            
            # transforma byte em inteiro
            num = ord(byte)

            if num == remove_char:
                continue

            # transforma inteiro em char
            char = chr(num)
            str += char
        
        return str
    
    @staticmethod
    def bytesToChar(file=None, byte=None):
        if byte is None:
            byte = file.read(1)

        num = ord(byte)
        char = chr(num)

        return char
