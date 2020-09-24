import turtle as t

t.speed(0)
t.pensize(2)
t.hideturtle()
t.onscreenclick(t.goto)

def blank():
    t.clear()

t.onkeypress(blank,"Escape")
t.listen()
