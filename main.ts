let servo1 = servoPWM.createServo(AnalogPin.P0)
let servo2 = servoPWM.createServo(AnalogPin.P0)
let servo3 = servoPWM.createServo(AnalogPin.P0)
let servo4 = servoPWM.createServo(AnalogPin.P0)
PlanetX_Gesture.onGesture(PlanetX_Gesture.GestureType.Right, function on_gesture_right() {
    basic.showIcon(IconNames.Heart)
})
PlanetX_Gesture.onGesture(PlanetX_Gesture.GestureType.Left, function on_gesture_left() {
    basic.showIcon(IconNames.Happy)
})
PlanetX_Gesture.onGesture(PlanetX_Gesture.GestureType.Up, function on_gesture_up() {
    basic.showIcon(IconNames.Happy)
})
PlanetX_Gesture.onGesture(PlanetX_Gesture.GestureType.Down, function on_gesture_down() {
    basic.showIcon(IconNames.Happy)
})
