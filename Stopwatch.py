#Impoting
import tkinter as tk
import time

#Declairing Global variables
Absolute = int(0)

#Declairing the app 
window = tk.Tk()
window.title("StopWatch")
window.geometry("400x400")

#User Info Text
tittle = tk.Label(text = "Hello and welcome to the Stopwatch application")
tittle.grid()

#how long in seconds text
tittle2 = tk.Label(text = "How Long in Seconds? ")
tittle2.grid(column = 0, row = 1 )

#function
def UserInputTime():
    UserIntTime = int(EntryBox.get())

    return UserIntTime
    
def UserOutputTime():
    UserOutTime = int(UserInputTime())

    outdisplay = tk.Text(master = window, height = 10, width = 30)
    outdisplay.grid(column = 0, row = 3)

    outdisplay.insert(tk.END, UserOutTime)

    #while Statemunt
    while UserOutTime > 0:
        UserOutTime -= 1
        outdisplay.insert(tk.END, UserOutTime )
        time.sleep(1)
        window.update()
    print ("Finished")
    outdisplay.insert(tk.END, "Finished" )
   

#EntryBox
EntryBox = tk.Entry()
EntryBox.grid(column = 0, row = 2)

#Button to start
StartButton = tk.Button(text = "Start", command = UserOutputTime)
StartButton.grid(column = 1, row = 2)

#Button to stop
StopButton = tk.Button(text = "Stop")
StopButton.grid(column = 2, row = 2)

#Button to Reset
ResetButton = tk.Button(text = "Reset")
ResetButton.grid(column = 3, row = 2)






#window.mainloop runs the program 
window.mainloop()
