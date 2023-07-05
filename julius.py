import string

class Caesar:
    characters: list =  list(string.ascii_letters)
    def __init__(self, plain: str, key: int = 0) -> None:
        self.plain = list(plain.strip())
        self.key = key

    def encryption(self) -> None:
        text_list: list = self.plain
        encrypted = ''
        for char in text_list:
            if char != ' ':         
                encrypted += "".join(Caesar.characters[(Caesar.characters.index(char) + self.key) % 26]).upper() + ''
            else:
                encrypted += char
        return encrypted

if __name__=='__main__':
    message = input('Enter Message: ')
    enc = Caesar(message, 3)
    print(enc.encryption())


