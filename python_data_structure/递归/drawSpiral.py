import turtle

myTurtle = turtle.Turtle()

mywin = turtle.Screen()


def drawSpiral(myTurtle,lineten):
    if lineten>0:
        myTurtle.forward(lineten)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineten-5)

def tree(branchLen,t):
    if branchLen>5:
        t.forward(branchLen)
        t.right(20)
        print(branchLen)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)


if __name__ == '__main__':
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(100)
    myTurtle.down()
    myTurtle.color('green')
    tree(75,myTurtle)
    mywin.exitonclick()

