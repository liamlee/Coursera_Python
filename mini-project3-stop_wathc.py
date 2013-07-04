# template for "Stopwatch: The Game"
import simplegui
# define global variables
interval = 100
times = 0

nice_stop = 0
all_stop = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = 0
    while t > 600:
        minutes = minutes + 1
        t = t - 600
    ms = t % 10
    seconds = (t - ms) / 10 
    if seconds < 10:
        seconds = "0" + str(seconds)
    
    return str(minutes) + ":" + str(seconds) + "." + str(ms)


def format_score():
    return str(nice_stop) + "/" + str(all_stop)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
   
def Stop():
    global nice_stop,times,all_stop
    if timer.is_running():
        all_stop = all_stop + 1
        if times % 10 == 0:
            nice_stop = nice_stop + 1
    timer.stop()

def Reset():
    global nice_stop,times,all_stop
    if timer.is_running():
        timer.stop()
    times = 0
    nice_stop = 0
    all_stop = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global times 
    times = times + 1


# define draw handler
def draw_time(canvas):
    #Show the time
    canvas.draw_text(format(times),[50,95],38,"White")
    #Show the score
    canvas.draw_text(format_score(),[160,20],24,"green")
  
  
# create frame
frame = simplegui.create_frame("StopWatch",200,150)
frame.add_button("Start",Start,80)
frame.add_button("Stop",Stop,80)
frame.add_button("Reset",Reset,80)
timer = simplegui.create_timer(interval,tick)

# register event handlers
frame.set_draw_handler(draw_time)

# start frame
frame.start()

# Please remember to review the grading rubric
