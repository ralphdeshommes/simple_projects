from time import sleep






#This fucntion will call the time function to see if its time for the certain task
task_hour = 0
task_minutes = 0
task_seconds = 25



def the_task():
    print("please put the time for when you want to stop the timer")
    hours = int(input("Hours:"))
    minutes = int(input("Minutes:"))
    seconds = int(input("Seconds"))
    return(hours,minutes,seconds)


# This is a timer
def time(seconds=0, minutes = 0, hour = 0):
    question = input("do you want a point to stop in the timer(Y/N)").upper()
    while True:
        if question == "Y":
            task = the_task()
            break
        if question == "N":
            task = None
            break
        print("incorrect input")
        question = input("please type correct input (Y/N)")
    while seconds >= 0:
        print(f"{hour:02}:{minutes:02}:{seconds:02}")
        sleep(1)
        
        if seconds == 0:
            if minutes > seconds:
                minutes -= 1
                seconds += 60
            elif hour > minutes:
                minutes += 60
                hour -= 1
        else:
            seconds -= 1
        if (hour,minutes,seconds) == task:
            print("your save point have arrived")
            to_continue = input("continue(y) or set another taks(t)").upper()
            if to_continue == "Y":
                continue
            elif to_continue == "T":
                task = the_task()
            else:
                break
        if  seconds + hour + minutes < 0:
            print("timer has completed")
            break
        

def main():
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    start_timer = input("To start the timer press Y\n").upper()

    while True:
        if start_timer == 'Y':
            time(seconds,minutes,hours)
            break
        else:
            print("incorrect input")
            sleep(3)
            start_timer = input("please press the correct letter(Y)").upper()
    
    

main()




        


