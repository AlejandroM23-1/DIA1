from curso import *
def lista_cursos():
    cursos_l= [
    Curso("Introducción a Linux", 15, "https://linux-introduction.com"),
    Curso("Python", 43, "https://python.org"),
    Curso("Introducción al Hacking", 53, "https://hacking-cibertec.com")
    ]
    for curso in cursos_l:
        print(curso)
lista_cursos()
