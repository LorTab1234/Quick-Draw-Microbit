# Imports go at the top
from microbit import *
import radio
import music

radio.on()
radio.config(channel=7)
number = 0
message_receive = False
disabled = False
button_pressed = False

while True:
    receivedMsg = radio.receive()

    #amount of steps players need to take
    if receivedMsg == 'increase':
        number = number + 1
        display.show(number)

    if receivedMsg == 'decrease':
        number = number - 1
        display.show(number)

    if receivedMsg == 'finalSteps':
        display.show(number)
        sleep(1000)
        display.show(Image('00000:'
                           '00900:'
                           '00900:'
                           '09099:'
                           '90000'))
        sleep(1000)
        display.show(number)
        
    if button_a.was_pressed():
        number -= 1
        disabled = False
        display.show(number)
        music.play(['C5:1'])
        if number == 0:
            display.show(number)
            sleep(800)
            display.show(Image.TARGET)
            radio.send('takenSteps')
            sleep(100)
            
    if receivedMsg == 'shoot':
        number = 0
        message_receive = True
        display.show(Image('00000:'
                               '00000:'
                               '09990:'
                               '09000:'
                               '00000'))
        music.play(music.BA_DING)
        sleep(100)
        
        
    if button_b.is_pressed() and not button_pressed:
        if message_receive == True:
            radio.send('player1_shot')
            display.show(Image.TARGET)
            music.play(['C4:1', 'R:1', 'C5:1'], wait=True, loop=False)
            button_pressed = True
        elif not button_b.is_pressed():
            button_pressed = False
    
    if receivedMsg == 'winner1':
        display.show(Image.HAPPY)
        
    if receivedMsg == 'winner2':
        display.show(Image.SAD)
        
        