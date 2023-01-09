input.onButtonPressed(Button.A, function () {
    pins.servoWritePin(AnalogPin.P0, 120)
    basic.pause(700)
    pins.servoWritePin(AnalogPin.P0, 0)
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Happy)
    for (let index = 0; index < 4; index++) {
        strip.showRainbow(1, 360)
        basic.pause(200)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        basic.pause(200)
    }
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 2; index++) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        basic.pause(200)
        strip.showColor(neopixel.colors(NeoPixelColors.White))
        basic.pause(200)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        basic.clearScreen()
    }
})
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P1, 12, NeoPixelMode.RGB)
strip.setBrightness(50)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
pins.servoWritePin(AnalogPin.P0, 0)
