/**
 * April 2018
 */
/**
 * by C Lyman
 */
input.onButtonPressed(Button.A, function () {
    letter = abcs.charAt(index)
    basic.showString(letter)
    basic.pause(100)
    index += 1
    if (index == abcs.length) {
        index = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showString(word)
    radio.sendString(word)
})
input.onButtonPressed(Button.B, function () {
    word = "" + word + letter
    index = 0
    basic.showString(word)
})
radio.onReceivedStringDeprecated(function (receivedString) {
    basic.showString("" + (receivedString))
})
let index = 0
let word = ""
let letter = ""
let abcs = ""
basic.showString("ABCs")
abcs = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = "a"
word = "b"
