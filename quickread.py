import turtle
import time

wn = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()

file_name = "Random_py_files/text.txt"
text = open(file_name, "r").read().split()

words_per_second = 10
wait_time = 1/words_per_second

for word in text:
    if ("." in word or "!" in word or "?" in word):
        t.clear()
        t.write(word, font=("Arial", 16, "normal"), align = "center")
        time.sleep(wait_time*1.5)
    else:
        t.clear()
        t.write(word, font=("Arial", 16, "normal"), align = "center")
        time.sleep(wait_time)


wn.exitonclick()