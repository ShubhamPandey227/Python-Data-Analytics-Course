from turtle import *
speed ('slowest')
fillcolor('Aqua')
side = 5

begin_fill()
for i in range(side) :
    fd(100)
    lt(360/side)
end_fill()
hideturtle()
mainloop()