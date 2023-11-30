class CharFlyweight:
    def __init__(self, char):
        self.char = char

class CharFactory:
    char_flyweights = {}

    @staticmethod
    def get_char(char):
        if char not in CharFactory.char_flyweights:
            CharFactory.char_flyweights[char] = CharFlyweight(char)
        return CharFactory.char_flyweights[char]

class Character:
    def __init__(self, char, font_size):
        self.char_flyweight = CharFactory.get_char(char)
        self.font_size = font_size

    def render(self):
        print(f"Character: {self.char_flyweight.char}, Font Size: {self.font_size}")

# Client code
characters = []
characters.append(Character('A', 12))
characters.append(Character('B', 14))
characters.append(Character('A', 12))  # Reusing 'A' from flyweight

for character in characters:
    character.render()