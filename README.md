# gpiozero_simon_says_2_buttons
Create a 2 buttons version of Simon Says game on your Raspberry Pi. Suitable for Pi-Top Inventor Kit which includes 2 buttons only.

## Why 2 buttons?
Pi-Top Inventor's Kit comes with 2 tactile button switches, 2 pieces for each of the 3 different colors of 10mm LEDs, and a few 
other components. Due to the limited tactile buttons, this project will only use 2 buttons instead of the usual 4.

Content inside the inventor's kit:
![Inventor's Kit content](https://pi-top.com/static/inventor-kit-alt-bg.e039d69d.jpg)
Find out more about the inventor's kit at: https://pi-top.com/products/pi-top/

## Wiring Diagram
![Wiring on Pi-Top proto+](https://github.com/fongkahchun86/gpiozero_simon_says_2_buttons/blob/master/Simon%20Says%202%20Buttons%20diagram.png)
**Note:** You can also create this project with your usual breadboard.

## Usage
To play this game, user can observe the sequence of the **red** and **green** blinking LEDs. This game will generate Simon's 
steps in sequence of "left" or "right", with left button controlling the left side red LED, while the right button controlling 
the right side green LED.

Simon's step will start off with 1 step, and increases in length whenever the user pressed the respective button correctly. User 
can press the corresponding button sequence after they hear a 0.5 sec beep at the end of the LED blinking steps.

Should the user pressed an incorrect sequence, double beeps will be produced, followed by the showing of Simon Steps again.

**Note:** You can turn off the printing of Simon's steps by commenting out line 49:
print("Simon's steps:", simon_steps)
