def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P0, 120)
    basic.pause(700)
    pins.servo_write_pin(AnalogPin.P0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.HAPPY)
    for index in range(4):
        strip.show_rainbow(1, 360)
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index2 in range(2):
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P1, 12, NeoPixelMode.RGB)
strip.set_brightness(50)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
pins.servo_write_pin(AnalogPin.P0, 0)