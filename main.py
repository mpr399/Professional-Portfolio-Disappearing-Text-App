from tkinter import messagebox
import tkinter as tk

THREAD_COUNTER = ""
TIME = 10
TEXT = ""


def update_time_label(time_left):
    l_time['text'] = f"Time Left: {time_left}"


def check_text_change():
    global TEXT
    new_text = t_typing.get(1.0, tk.END)
    if TEXT != new_text:
        TEXT = new_text
        reset_timer()


def countdown(x):
    update_time_label(x)
    check_text_change()

    if x > 0:
        global THREAD_COUNTER
        THREAD_COUNTER = window.after(1000, countdown, x - 1)
    else:
        end_session()
        stop_countdown()


def stop_countdown():
    global THREAD_COUNTER
    window.after_cancel(THREAD_COUNTER)


def end_session():
    t_typing.delete('1.0', tk.END)
    messagebox.showinfo("TIME UP", f"You have lost your text, because you stopped typing :)")
    b_start.config(state=tk.NORMAL)


def reset_timer():
    try:
        stop_countdown()
    except:
        pass
    countdown(TIME)


def start():
    reset_timer()
    b_start.config(state=tk.DISABLED)


# GUI ####################################################################
window = tk.Tk()
window.title("Disappearing Text App")
window.config(padx=10, pady=10)

b_start = tk.Button(text="Start Disappearance Timer", command=start)
b_start.grid(row=0, column=0)

l_time = tk.Label(text="Time Left: ")
l_time.grid(row=0, column=1)

t_typing = tk.Text(wrap=tk.WORD)
t_typing.grid(row=1, column=0, columnspan=2)

window.mainloop()
