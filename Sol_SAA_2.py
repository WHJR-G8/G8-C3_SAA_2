import turtle

radius = 20

for i in range(3):

    while radius >= 40:
        radius += 10
        turtle.pencolor('red')
        turtle.circle(radius)
        break
        
    radius += 20
    turtle.pencolor('green')
    turtle.circle(radius)
