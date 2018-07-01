"""
This Simon Says game is modified to suit the use of the Pi-top's Inventor's Kit.
Each Inventor's Kit only has 2 buttons and 3 colors of LEDs. Hence, this game
will generate Simon's steps in sequence of "left" or "right", with left button
controlling the left side red LED, while the right button controlling the right
side green LED.

You can turn off the printing of Simon's steps by commenting out line 49:
print("Simon's steps:", simon_steps)
"""

from gpiozero import LED, Buzzer, Button
from random import choice
from time import sleep

led_r = LED(4)
led_g = LED(5)
bn_left = Button(27)
bn_right = Button(13)
bz = Buzzer(17)
options = ['l', 'r']
simon_steps = []
player_steps = []
player_guessed_correctly = False
player_curr_step = -1 #Step 0 is the first step

def error_bz():
    for i in range(2):
        bz.on()
        sleep(0.5)
        bz.off()
        sleep(0.1)

#error_bz()

def correct_bz():
    bz.on()
    sleep(0.5)
    bz.off()
    '''
    sleep(0.05)
    bz.on()
    sleep(0.2)
    bz.off()
    '''
#correct_bz()

def show_simon_steps():
    print("Simon's steps:", simon_steps) #comment to hide Simon steps
    for step in simon_steps:
        if step == 'l':
            led_r.on()
            sleep(0.5)
            led_r.off()
            sleep(0.2)
        elif step == 'r':
            led_g.on()
            sleep(0.5)
            led_g.off()
            sleep(0.2)
    #ending beep
    bz.on()
    sleep(0.5)
    bz.off()

def bn_left_pressed():
    led_r.on()

def bn_right_pressed():
    led_g.on()

def bn_left_released():
    led_r.off()
    player_steps.append('l')
    global player_curr_step
    player_curr_step += 1
    check_ans()

def bn_right_released():
    led_g.off()
    player_steps.append('r')
    global player_curr_step
    player_curr_step += 1
    check_ans()

def check_ans():
    global player_steps, simon_steps, player_curr_step
    print("Player's steps:", player_steps)
    #print("Simon's steps:", simon_steps)
    if len(player_steps) <= len(simon_steps):
        if player_steps[player_curr_step] != simon_steps[player_curr_step]:
            print("INCORRECT!")
            error_bz()
            player_steps = []
            player_curr_step = -1 #reset player input step number
            show_simon_steps()
    if player_curr_step + 1 == len(simon_steps) and player_steps[-1] == simon_steps[-1]:
        print("=== Correct and completed stage", (player_curr_step + 1), "! ===\n")
        correct_bz()
        player_steps = []
        player_curr_step = -1 #reset player input step number
        simon_steps.append(choice(options))
        show_simon_steps()
    

bn_left.when_pressed = bn_left_pressed
bn_left.when_released = bn_left_released
bn_right.when_pressed = bn_right_pressed
bn_right.when_released = bn_right_released

simon_steps.append(choice(options))
show_simon_steps()
