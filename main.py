from threading import Timer

DELAY = 30
idle = False


def set_brightness(level):
    print("brightness set to", level)
    with open("/sys/class/backlight/intel_backlight/brightness", "w") as f:
        f.write(str(level))


def go_idle():
    global idle
    if idle: return
    idle = True
    print("idle")
    set_brightness(0)


with open( "/dev/input/event3", "rb" ) as f:

    # Init timer
    t = Timer(DELAY, go_idle)
    t.start()

    print("ttysaver started")
    while 1:
        data = f.read(24)
        
        # User performed an action
        if idle == True:
            # It was idle before
            set_brightness(100)
            idle = False
            print("active")
        

        # reset timer
        t.cancel()
        t = Timer(DELAY, go_idle)
        t.start()
