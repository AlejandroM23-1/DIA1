class Curso:
    def __init__(self, nombre, duracion, link):
        self.nombre= nombre
        self.duracion= duracion
        self.link= link

    def __str__(self):
        return f"{self.nombre} [{self.duracion} horas] {self.link}"

cursos_l= [
    Curso("Introducción a Linux", 15, "https://linux-introduction.com"),
    Curso("Python", 43, "https://python.org"),
    Curso("Introducción al Hacking", 53, "https://hacking-cibertec.com")
]

def lista_cursos():
    for curso in cursos_l:
        print(curso)
