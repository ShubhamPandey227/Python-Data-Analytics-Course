from turtle import *
speed ('fastest')
pencolor ('blue')

side = 6

#hexagon
for i in range (6) :
    pensize(5)
    fd(100)
    for i in range(6) :
        pensize(4)
        fd(50)
        fillcolor('Aqua')
        begin_fill()
        for i in range(6):
            pensize(3)
            fd(25)
            lt(60)
            for i in range(6) :
                pensize(2)
                fd(25)
                rt(60)
                for i in range (6) :
                    pensize(1)
                    fd(25)
                    lt(60)
        rt(60)
    rt(60)
hideturtle()
mainloop()