from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for r in range(math.floor(REPS / 2)):
            marks += "✓"
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=20, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 70, "bold"), bg=YELLOW)
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)
check_mark = Label(text="", fg=GREEN, bg=YELLOW)

timer_label.grid(column=1, row=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_mark.grid(column=1, row=3)

window.mainloop()
