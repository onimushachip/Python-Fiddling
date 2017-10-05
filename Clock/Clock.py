import turtle
import datetime
import time

secondHand = turtle.Turtle()
secondHand.speed(0)
secondHand.hideturtle()
secondHand.color("red")

minuteHand = turtle.Turtle()
minuteHand.speed(0)

hourHand = turtle.Turtle()
hourHand.speed(0)


clock = turtle.Turtle()
clock.speed(0)


def drawClock(currentSecond, currentMinute, currentHour):
    clock.penup()
    clock.goto(0, -180)
    clock.pendown()
    clock.color("blue")
    clock.circle(180)

    secondHand.penup()
    secondHand.goto(0, 0)
    secondHand.setheading(90)
    secondHand.right(currentSecond * 360 / 60)
    secondHand.pendown()
    secondHand.forward(150)

    minuteHand.penup()
    minuteHand.goto(0, 0)
    minuteHand.setheading(90)
    minuteHand.right(currentMinute * 360 / 60)
    minuteHand.pendown()
    minuteHand.forward(150)

    hourHand.penup()
    hourHand.goto(0, 0)
    hourHand.setheading(90)
    hourHand.right(currentHour * 360 / 12)
    hourHand.pendown()
    hourHand.forward(100)

def runSecondHand(currentSecond):
    secondHand.clear()
    secondHand.penup()
    secondHand.goto(0, 0)
    secondHand.setheading(90)
    secondHand.right(currentSecond * 360 / 60)
    secondHand.pendown()
    secondHand.forward(150)
    time.sleep(0.5)

def runMinuteHand(currentMinute):
    minuteHand.clear()
    minuteHand.penup()
    minuteHand.goto(0, 0)
    minuteHand.setheading(90)
    minuteHand.right(currentMinute * 360 / 60)
    minuteHand.pendown()
    minuteHand.forward(150)

def runHourHand(currentHour):
    hourHand.clear()
    hourHand.penup()
    hourHand.goto(0, 0)
    hourHand.setheading(90)
    hourHand.right(currentHour * 360 / 12)
    hourHand.pendown()
    hourHand.forward(100)


def runClock():
    currentSecond = datetime.datetime.now().second
    currentMinute = datetime.datetime.now().minute
    currentHour = datetime.datetime.now().hour
    drawClock(currentSecond, currentMinute, currentHour)

    while (True):
        currentSecond = datetime.datetime.now().second
        currentMinute = datetime.datetime.now().minute
        currentHour = datetime.datetime.now().hour
        runSecondHand(currentSecond)
        if currentSecond % 60 == 0:
            runMinuteHand(currentMinute)
        if currentMinute % 60 == 0:
            runHourHand(currentHour)

runClock()
