import turtle
window = turtle.Screen()
square = turtle.Turtle()


medida=int(input("ingresar"))

medida2=int(input("segundovalor"))




   if medida > 0:

    square.forward({medida})
    square.left({90})
    square.forward({medida})
    square.left({90})

    turtle.mainloop()