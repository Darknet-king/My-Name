import turtle

''' 
╭─╮ ┬┈┬ ╭╮╭ ╭─╮ ┬─╮ ┈ ╭╮┈ ┬┈┬ ┈ ╭─╮ ╭─╮ ╭┬╮ ┬┈┬ 
│┈│ │││ │││ ├┤┈ ├┬╯ ┈ ├┴╮ ╰┬╯ ┈ ╰─╮ ├┤┈ ┈│┈ ├─┤  
╰─╯ ╰┴╯ ╯╰╯ ╰─╯ ┴╰─ ┈ ╰─╯ ┈┴┈ ┈ ╰─╯ ╰─╯ ┈┴┈ ┴┈┴  

    My Codes Don't Copy......              '''

Sl=turtle.getscreen()
S=turtle.Turtle()
turtle.bgcolor('black')
S.speed(2)
S.penup()
S.pen(pencolor='red',fillcolor='red',pensize='4')

# M
S.lt(180)
S.fd(330)
S.rt(90)
S.pendown()
S.fd(200)
S.rt(140)
S.fd(100)
S.lt(100)
S.fd(100)
S.rt(140)
S.fd(200)
S.lt(90)
S.penup()


# I

S.fd(40)
S.lt(90)
S.pendown()
S.fd(200)
S.rt(90)
S.penup()

# L 

S.fd(40)
S.rt(90)
S.pendown()
S.fd(200)
S.lt(90)
S.fd(100)
S.penup()
S.fd(30)

# A

S.fd(130)
S.pendown()
S.goto(40,180)
S.goto(-5,0)
S.fd(150)
S.penup()

# N

S.fd(40)
S.pendown()
S.lt(90)
S.fd(200)
S.goto(300,0)
S.fd(200)
S.penup()
S.fd(30)

# BORDER

S.pen(pencolor='white',fillcolor='white',pensize='4')
S.pendown()
S.lt(90)
S.fd(700)
S.penup()
S.goto(-350,-30)
S.pendown()
S.rt(180)
S.fd(700)

turtle.done()
