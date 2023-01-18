import pandas as pd
import requests
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('green')
t.pencolor('red')
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
# adding another commit
while True:
    t.forward(a)
    t.right(b)
    a+= 3
    b+= 1
    if b ==210:
        break
    t.hideturtle()
turtle.done()


# class Person:
#
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#
# p1 = Person('john',70)
# print(p1.name)
# print(p1.age)
