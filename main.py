import turtle

t = turtle.Turtle()

# faire une fonction escalier qui va prendre en compte la taille et le nombre de repetitions de marches

def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

"""t.forward(100)
t.left(90)
t.forward(50)
t.backward(100)
"""
# exo 1 : faire un escalier avec des marches de 30 pixels de hauteur et 30 pixels de largeur, sur 5 marches

"""for i in range(0, 5):
        t.forward(30)
        t.left(90)
        t.forward(30)
        t.right(90)
    t.forward(30)"""

# escalier(30, 5)

# exo 2 : faire un carré avec comme paramètre la taille du carré

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)



#carre(100)

# exo 3 : définir une fonction qui permet d'afficher plusieurs carrés
def carres(taille_depart, nb):
    # taille = (i + 1) * taille_depart
    for i in range(0, nb):
        taille = (i + 1) * taille_depart
        carre(taille)
        

carres(50, 5)

turtle.done()

