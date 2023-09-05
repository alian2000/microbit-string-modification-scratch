"""

April 2018

"""
"""

by C Lyman

"""

def on_button_pressed_a():
    global letter, index
    letter = abcs.char_at(index)
    basic.show_string(letter)
    basic.pause(100)
    index += 1
    if index == len(abcs):
        index = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string(word)
    radio.send_string(word)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global word, index
    word = "" + word + letter
    index = 0
    basic.show_string(word)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_string_deprecated(receivedString):
    basic.show_string("" + (receivedString))
radio.on_received_string_deprecated(on_received_string_deprecated)

index = 0
word = ""
letter = ""
abcs = ""
basic.show_string("ABCs")
abcs = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = "a"
word = "b"