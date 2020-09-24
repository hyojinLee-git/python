import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(200):
    a=random.randint(1,360)
    t.setheading(a) #left도 가능
    t.forward(10)
