class PersonFile:
    def __init__(self, first_name, last_name, birth):
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.birth}'
