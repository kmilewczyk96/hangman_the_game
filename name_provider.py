class NameProvider:
    def __init__(self):
        self.alphabet = [i for i in range(97, 123)]
        self.name = ['_' for i in range(3)]
        self.aesthetic_name = ['_' for i in range(3)]
        self.position = 0

    def add_letter(self, letter):
        if self.name[self.position] == '_':
            self.name[self.position] = letter
        else:
            if self.position < 2:
                self.position += 1
                self.name[self.position] = letter

    def delete_letter(self):
        if self.name[self.position] != '_':
            self.name[self.position] = '_'
        else:
            if self.position > 0:
                self.position -= 1
                self.name[self.position] = '_'

    def get_name(self):
        if '_' not in self.name:
            return ''.join(self.name)
