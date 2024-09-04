from tkinter import *
import math

# --------------- CONSTANTS -------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
counter = " "


# --------------- TIMER RESET -------------#


def rest_timer():
    global check_marks, reps
    window.after_cancel(counter)
    timer.config(text="Timer", fg="blue")
    canvas.itemconfig(timer_text, text="00.00")
    check_marks.config(text="")
    reps = 0


# --------------- TIMER MECHANISM -------------#


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_sec)
        timer.config(text="Break4", fg="red")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text=f"Break{int(reps / 2)}", fg="pink")
    else:
        count_down(work_sec)
        timer.config(text="Work", fg="green")


# --------------- COUNTDOWN MECHANISM -------------#


def count_down(count):
    global reps, counter
    count_min = int(math.floor(count / 60))
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        counter = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = " "
        work_sessions = int(math.floor(reps / 2))
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)
    if reps == 8:
        reps = 0


# --------------- UI SETUP -------------#
window = Tk()
window.title("POMODORO")
window.minsize(width=270, height=200)
# window.config(padx=100,pady=50)
window.config(bg="white")

# window.config(bg="yellow")

canvas = Canvas(width=206, height=238, bg="white", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(104, 120, image=tomato_img)  # 104,120
timer_text = canvas.create_text(105, 160, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.config(background="white")
canvas.grid(column=2, row=2)

# count_down(5)

timer = Label(text="Timer", fg="blue", bg="white", font=(FONT_NAME, 60, "bold"))
timer.grid(column=2, row=1)

start = Button(text="Start", fg="white", bg="black", highlightthickness=0, command=start_timer,
               font=(FONT_NAME, 20, "bold"))
start.grid(column=1, row=3)

reset = Button(text="Reset", fg="white", bg="black", highlightthickness=0, command=rest_timer,
               font=(FONT_NAME, 20, "bold"))
reset.grid(column=3, row=3)

check_marks = Label(bg="white")
check_marks.grid(column=2, row=5)

window.mainloop()
