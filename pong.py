import turtle
apontos = bpontos = 0
#inicialização da tela
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle a
paddlea = turtle.Turtle()
paddlea.speed(0)
paddlea.shape("square")
paddlea.color("red")
paddlea.shapesize(stretch_wid=5, stretch_len=1)
paddlea.penup()
paddlea.goto(-350, 0)

#paddle b
paddleb = turtle.Turtle()
paddleb.speed(0)
paddleb.shape("square")
paddleb.color("blue")
paddleb.shapesize(stretch_wid=5, stretch_len=1)
paddleb.penup()
paddleb.goto(350, 0)

#ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

#Função movimentar a paddlea
def paddlea_moveup():
    y = paddlea.ycor()
    y += 20
    paddlea.sety(y)
def paddlea_movedown():
    y = paddlea.ycor()
    y -= 20
    paddlea.sety(y)

#movimentar paddle b
def paddleb_moveup():
    y = paddleb.ycor()
    y += 20
    paddleb.sety(y)
def paddleb_movedown():
    y = paddleb.ycor()
    y -= 20
    paddleb.sety(y)

#Controle de teclado
wn.listen()
wn.onkeypress(paddlea_moveup, "w")
wn.onkeypress(paddlea_movedown, "s")
wn.onkeypress(paddleb_moveup, "Up")
wn.onkeypress(paddleb_movedown, "Down")

#pontos
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


#loop do jogo principal
while True:
    wn.update()

    #move a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Borda
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >= 390: 
        ball.goto(0, 0)
        ball.dx *= -1
        apontos += 1
    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx *= -1
        bpontos += 1

    #colisão com as raquetes:
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleb.ycor() + 50 and ball.ycor() > paddleb.ycor() - 50):
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddlea.ycor() + 50 and ball.ycor() > paddleb.ycor() - 50):
        ball.dx *= -1
    pen.clear()
    pen.write(f"{apontos} x {bpontos}", align="center", font=("Courier", 24, "normal"))