servo1 = servoPWM.create_servo(AnalogPin.P0)
servo2 = servoPWM.create_servo(AnalogPin.P0)
servo3 = servoPWM.create_servo(AnalogPin.P0)
servo4 = servoPWM.create_servo(AnalogPin.P0)

def on_gesture_right():
    basic.show_icon(IconNames.HEART)
PlanetX_Gesture.on_gesture(PlanetX_Gesture.GestureType.RIGHT, on_gesture_right)

def on_gesture_left():
    basic.show_icon(IconNames.HAPPY)
PlanetX_Gesture.on_gesture(PlanetX_Gesture.GestureType.LEFT, on_gesture_left)

def on_gesture_up():
    basic.show_icon(IconNames.HAPPY)
PlanetX_Gesture.on_gesture(PlanetX_Gesture.GestureType.UP, on_gesture_up)

def on_gesture_down():
    basic.show_icon(IconNames.HAPPY)
PlanetX_Gesture.on_gesture(PlanetX_Gesture.GestureType.DOWN, on_gesture_down)
