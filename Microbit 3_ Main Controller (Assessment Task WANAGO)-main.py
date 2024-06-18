# Imports go at the top
from microbit import *
import radio
import music

radio.on()
radio.config(channel=7)
message_received = False
disabled = False
winner = None

def increase_function():
    if button_a.is_pressed():
        disabled = False
        radio.send('increase')
        display.show(Image('00000:'
                           '00900:'
                           '09990:'
                           '00900:'
                           '00000'))
        sleep(500)

def decrease_function():
    if button_b.is_pressed():
        disabled = False
        radio.send('decrease')
        display.show(Image('00000:'
                           '00000:'
                           '09990:'
                           '00000:'
                           '00000'))
        sleep(500)

def confirm_function():
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send('finalSteps')
        display.show(Image('00000:'
                           '00009:'
                           '09090:'
                           '00900:'
                           '00000'))
        sleep(500)

while True:
    receivedMsg = radio.receive()
    #for amount of steps players need to take

    increase_function()
    decrease_function()
    confirm_function()
        
        
    if receivedMsg == 'step':
        display.show(Image.ARROW_E)

    #when the player takes that much steps
    if receivedMsg == 'takenSteps':
        display.show(Image.TARGET)
        sleep(500)
        message_received = True
        disabled = True
        
        
    if button_a.is_pressed():
        if message_received == True:
            if disabled == True:
                radio.send('shoot')
                display.show(Image('00000:'
                                  '00000:'
                                  '09990:'
                                  '09000:'
                                  '00000'))
                music.play(music.BA_DING)
                music.stop()
                
    if receivedMsg == 'player1_shot':
        display.show('1')
        sleep(100)
        radio.send('winner1')
    
    if receivedMsg == 'player2_shot':
        display.show('2')
        sleep(100)
        radio.send('winner2')
            
            