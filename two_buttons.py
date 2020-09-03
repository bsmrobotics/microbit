from microbit import *
pin15.set_analog_period(50)
pin16.set_analog_period(50)
low = 16
high = 48
mid = int((high + low) / 2)
state_a = 1 # 0: back, 1: off, 2: forward
display.set_pixel(0, state_a, 9)
state_b = 1 # 0: back, 1: off, 2: forward
display.set_pixel(4, state_b, 9)
while True:
  if(button_a.get_presses()):
    state_a += 1
    state_a = state_a % 4
    display.set_pixel(0, 0, 0)
    display.set_pixel(0, 1, 0)
    display.set_pixel(0, 2, 0)
    if(state_a % 2 == 1):
      light_a = 1
    else:
      light_a = state_a
    display.set_pixel(0, light_a, 9)
    angle_a = [low, mid, high, mid][state_a]
    pin15.write_analog(angle_a)
  if(button_b.get_presses()):
    state_b += 1
    state_b = state_b % 4
    display.set_pixel(4, 0, 0)
    display.set_pixel(4, 1, 0)
    display.set_pixel(4, 2, 0)
    if(state_b % 2 == 1):
        light_b = 1
    else:
        light_b = state_b
    display.set_pixel(4, light_b, 9)
    angle_b = [low, mid, high, mid][state_b]
    pin16.write_analog(angle_b)
