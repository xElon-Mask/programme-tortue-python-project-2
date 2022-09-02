import turtle

t = turtle.Turtle()

# faire une fonction escalier qui va prendre en compte la taille et le nombre de repetitions de marches

"""t.forward(100)
t.left(90)
t.forward(50)
t.backward(100)
"""
# exo 1 : faire un escalier avec des marches de 30 pixels de hauteur et 30 pixels de largeur, sur 5 marches

for i in range(0, 5):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
t.forward(30)

turtle.done()

