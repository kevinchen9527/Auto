import turtle

import time

BC = 'DodgerBlue4'

def draw_moon():

    turtle.pencolor(BC)

    turtle.fillcolor( 'Gold')

    turtle.penup()

    turtle.goto( -150, 0)

    turtle.pendown()

    turtle.begin_fill()

    turtle.circle(110)

    turtle.end_fill()

def draw_words():

    turtle.penup()

    turtle.pencolor('Yellow1')

    turtle.goto(400, -150)

    turtle.write("明\n月\n出\n天\n山\n", align= "center", font=("STXingkai", 50, "bold")) 
    time.sleep(1)

    turtle.goto(300, -150)

    turtle.write("苍\n茫\n云\n海\n间\n", align= "center", font=("STXingkai", 50, "bold")) 
    time.sleep(1)

    turtle.goto(200, -150)

    turtle.write("长\n风\n几\n万\n里\n", align= "center", font=("STXingkai", 50, "bold")) 
    time.sleep(1)

    turtle.goto(100, -150)

    turtle.write("吹\n度\n玉\n门\n关\n", align= "center", font=("STXingkai", 50, "bold"))

def draw_mountain():

    turtle.fillcolor('grey21')

    turtle.pencolor('grey31')

    turtle.pensize(4)

    turtle.penup()

    turtle.goto(-500, -250)

    turtle.begin_fill()

    turtle.pendown()

    turtle.left(15)

    turtle.forward(400)

    turtle.right(30)

    turtle.forward(200)

    turtle.left(40)

    turtle.forward(300)

    turtle.right(50)

    turtle.forward(300)

    turtle.goto(500, -300)

    turtle.goto(-500, -300)

    turtle.end_fill()

def draw_cloud():
    step = 1.5 # 画弧时的步长

    angle = 3 # 每次改变的角度

    disize = 0.6 # 每次增加或减少的线宽 
    psize = 5 # 初始线宽 
    turtle.pencolor('WhiteSmoke') 
    turtle.pencolor('Gainsboro') 
    turtle.pensize(psize) 
    turtle.penup()

    turtle.goto(-500, 200) 
    turtle.pendown() 
    turtle.forward(250)
    
    for i in range(30):

        psize += disize

        turtle.pensize(psize)

        turtle.right(angle)

        turtle.forward(step)

    for i in range(30):

        psize -= disize

        turtle.pensize(psize)

        turtle.right(angle)

        turtle.forward(step)

    turtle.forward(100)

    for i in range(30):

        psize += disize

        turtle.pensize(psize)

        turtle.left(angle)

        turtle.forward(step)

    for i in range(30):

        psize -= disize

        turtle.pensize(psize)

        turtle.left(angle)

        turtle.forward(step)

    turtle.forward(600)

def draw_init():
    turtle.setup(1000, 600) 
    turtle.bgcolor(BC) 
    turtle.speed(8) # 设置画笔速度为8

def main():

    draw_init()

    draw_moon()

    draw_cloud()

    draw_mountain()

    draw_words()

    turtle.exitonclick() #点击才关闭画画窗口

if __name__ == '__main__':
    main()