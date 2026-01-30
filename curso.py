class Curso:
    def __init__(self, nombre, duracion, link):
        self.nombre= nombre
        self.duracion= duracion
        self.link= link

    def __str__(self):
        return f"{self.nombre} [{self.duracion} horas] {self.link}"
