from tkinter import *

FONT_NAME = "Courier"
check_list = ""

rep = 1

def add_in_checklist():
    global check_list
    check_list += "✔"
    check_marks["text"] = check_list


def start_timer():
    if(rep % 2 != 0):
        countdown(25*60)
    else:
        if(rep % 8 != 0):
            countdown(300)
        else:
            countdown(1200)

def reset_timer():
    global check_list, timer_id, rep
    if timer_id:  # If a timer is running, cancel it
        window.after_cancel(timer_id)
        timer_id = None  # Reset the timer ID
    check_list = ""
    check_marks["text"] = check_list
    canvas.itemconfig(timer_text, text="00:00")
    rep = 1

def countdown(count):
    global timer_id, rep
    y = str(count // 60)
    z = str(count % 60)
    if (count % 60) < 10:
        z = "0" + z
    if (count // 60) < 10:
        y = "0" + y
    a = y + ":" + z
    canvas.itemconfig(timer_text, text=a)
    
    if count == 0:
        if(rep % 2 != 0):
            add_in_checklist()
        rep += 1
        start_timer()
    if(count > 0):
        timer_id = window.after(1000, countdown, count - 1)  # Store the timer ID







window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg="#ffffff")

canvas = Canvas(width=400, height=450, bg="#ffffff",highlightthickness=0)
# Correctly loading the image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 200, image=tomato_img)
timer_text = canvas.create_text(200, 200, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)



timer = Label(text="Timer", bg="white", fg="black",font=(FONT_NAME,40,"bold"))
timer.grid(column=1, row=0)


start = Button(
    text="Start",
    highlightthickness=0,
    bg="#28a745",  # Green background
    fg="white",    # White text
    font=(FONT_NAME, 13, "bold"),
    padx=15,
    pady=10,
    relief="raised",
    command=start_timer
)
start.grid(column=0, row=2, padx=10, pady=10)

# Style the Reset button
reset = Button(
    text="Reset",
    highlightthickness=0,
    bg="#dc3545",  # Red background
    fg="white",    # White text
    font=(FONT_NAME, 13, "bold"),
    padx=15,
    pady=10,
    relief="raised",
    command=reset_timer
)
reset.grid(column=2, row=2, padx=10, pady=10)

check_marks = Label(text=check_list, fg="black", bg="white", font=(FONT_NAME, 13, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
