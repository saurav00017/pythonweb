import turtle
import pyautogui
import time
import random
def Snake_game():
    def quit():
        global running
        running = False
    try:
        delay = 0.1
        color_list = ['Red', 'Blue', 'pink', 'violet', 'purple','orange','yellow','brown']
        shape_ = ['circle','square','turtle']
        #scores
        score = 0
        high_score = 0

        #set up screen
        wn = turtle.Screen()
        wn.getshapes()
        wn.title("Snake Game")
        wn.bgcolor('Black')
        wn.setup(width=600, height=600)
        wn.tracer(0)

        #snake head
        head = turtle.Turtle()

        # head.speed(2)
        head.shape('square')
        head.color("#83e700")
        head.penup()
        head.goto(0,0)
        head.direction = "stop"
        if score <= 20:
            head.speed(1)
        elif score >20 and score <= 50:
            head.speed(3)
        elif score >50 and score <= 100:
            head.speed(6)
        elif score >100 :
            head.speed(0)


        #snake food
        food= turtle.Turtle()
        food.speed(0)
        # for i in range(0,400):
        food.shape(random.choice(shape_))
        food.color(random.choice(color_list))
        food.penup()
        food.goto(0,100)

        segments = []

        #scoreboards
        sc = turtle.Turtle()
        sc.speed(0)
        sc.shape("square")
        sc.color("White")
        sc.penup()
        sc.hideturtle()
        sc.goto(0,260)
        sc.write("score: 0  High score: 0", align = "center", font=("ds-digital", 24, "normal"))

        #Functions
        def go_up():
            if head.direction != "down":
                head.direction = "up"
        def go_down():
            if head.direction != "up":
                head.direction = "down"
        def go_left():
            if head.direction != "right":
                head.direction = "left"
        def go_right():
            if head.direction != "left":
                head.direction = "right"
        def move():
            if head.direction == "up":
                y = head.ycor()
                head.sety(y+20)
            if head.direction == "down":
                y = head.ycor()
                head.sety(y-20)
            if head.direction == "left":
                x = head.xcor()
                head.setx(x-20)
            if head.direction == "right":
                x = head.xcor()
                head.setx(x+20)

        #keyboard bindings
        wn.listen()
        wn.onkeypress(go_up, "Up")
        wn.onkeypress(go_down, "Down")
        wn.onkeypress(go_left, "Left")
        wn.onkeypress(go_right, "Right")

        #MainLoop
        running = True
        while running:
            wn.update()

            #check collision with border area
            if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
                result = pyautogui.confirm(text='Wanna Play again ??',title='Game Over',buttons=['cancel','ok'])

                if result == 'ok':
                    print("New game started")
                else:
                    break
                    # quit()



                #hide the segments of body
                for segment in segments:
                    segment.goto(1000,1000) #out of range
                #clear the segments
                segments.clear()

                #reset score
                score = 0

                #reset delay
                delay = 0.1

                sc.clear()
                sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

            #check collision with food
            if head.distance(food) <20:
                food.shape(random.choice(shape_))
                food.color(random.choice(color_list))
                # move the food to random place
                x = random.randint(-280,280)
                y = random.randint(-280,280)
                food.goto(x,y)

                #add a new segment to the head
                new_segment = turtle.Turtle()
                if score <= 20:
                    new_segment.speed(1)
                elif score >20 and score <= 50:
                    new_segment.speed(3)
                elif score >50 and score <= 100:
                    new_segment.speed(6)
                elif score >100 :
                    new_segment.speed(0)
                # new_segment.speed()
                new_segment.shape("square")
                new_segment.color("#83e700")
                new_segment.penup()
                segments.append(new_segment)

                #shorten the delay
                delay -= 0.001
                #increase the score
                score += 10

                if score > high_score:
                    high_score = score
                sc.clear()
                sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))

            #move the segments in reverse order
            for index in range(len(segments)-1,0,-1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x,y)
            #move segment 0 to head
            if len(segments)>0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x,y)

            move()

            #check for collision with body
            for segment in segments:
                if segment.distance(head)<20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "stop"
                    result = pyautogui.confirm(text='Wanna Play again ??',title='Game Over',buttons=['cancel','ok'])

                    if result == 'ok':
                        print("New game started")
                    else:
                        break
                        # quit()

                    #hide segments
                    for segment in segments:
                        segment.goto(1000,1000)
                    segments.clear()
                    score = 0
                    delay = 0.1

                    #update the score
                    sc.clear()
                    sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
            time.sleep(delay)
        # wn.mainloop()
        wn.bye()
    except Exception:
        print(Exception)
