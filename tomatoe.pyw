import time 
import datetime as dt 

import tkinter
from tkinter import messagebox 
import winsound

# Main Script 
t_now = dt.datetime.now()               # Current Time [datetime object]
t_pom = 25*60                           # Pomodoro Time [int, seconds]
t_delta = dt.timedelta(0,t_pom)         # Pomodoro time [datetime object]
t_fut = t_now + t_delta                 # Future time, ending pomodoro [datetime object]
delta_sec = 5*60                        # Break time after pomodoro [int, seconds]
t_fin = t_now + dt.timedelta(0,t_pom+delta_sec) # Final time (w/ 5 mins break) [datetime object]


# GUI set pomodoro in motion! 

# hide tkinter's main window. We only need the alert message box 
root = tkinter.Tk()
root.withdraw()
# Show alert message - Started 
messagebox.showinfo("Pomodoro Started!", "\n It is now "+t_now.strftime("%H:%M") + " hrs. \nTimer set for 25 mins. ")

# Initialize pomodoro counter 
total_pomodoros = 0 
breaks = 0 

while True: 
    # Pomodoro time! 
    if t_now < t_fut:
        print('pomodoro')
    ## it is now past working pomodoro, within the break.
    elif t_fut <= t_now <= t_fin:
        print('in break')
        if breaks == 0:
            print('if break')
            # Annoy! 
            for i in range(5):
                winsound.Beep((i+100), 700)
                print('Break time!')
                breaks += 1 
    #Pomodoro and break finished. Check if ready for another pomodoro! 
    else: 
        print('Finished!')
        # Pomodoro finished. Reset breaks 
        breaks = 0 
        # Annoy! -> Let user known that break is over :'(
        for i in range(10):
            windsound.Beep((i+100), 500)
        # Ask if user wants to start again. 

        usr_ans = messagebox.askyesno("Pomodoro Finished!","Would you like to start another pomodoro?")
        total_pomodoros += 1 
        if usr_ans == True: 
            #user wants another pomodoro! Update values to indicate new timeset. 
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0,t_pom)
            t_fin = t_now + dt.timedelta(0,t_pom+delta_sec)
            continue
        elif usr_ans == False:
            # User is done, display achievements for now.
            messagebox.showinfo("Pomodoro Finished!", "\nYou completed "+str(total_pomodoros)+" pomodoros today." )
            break
        # check every 20 seconds and update current time 
        print('sleeping')
        time.sleep(20)
        t_now = dt.datetime.now()
        timenow = t_now.strftime("%H:%M")