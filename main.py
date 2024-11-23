import vgamepad as vg
import time
import math

gamepad = vg.VX360Gamepad()
time.sleep(5)

while True:
    # Move the left joystick in a circular motion
    for angle in range(0, 360, 10):
        # Convert polar coordinates to Cartesian coordinates
        x = 0.9 * math.cos(math.radians(angle))
        y = 0.9 * math.sin(math.radians(angle))

        

        # Set the left joystick values
        gamepad.left_joystick_float(x_value_float=x, y_value_float=y)
        gamepad.left_right_float(x_value_float=x, y_value_float=y)
        gamepad.update()
        time.sleep(0.1)

        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()  # Update the gamepad to reflect the change
    print("A button pressed")

    # Hold the button for a short duration
    time.sleep(0.5)

    # Release the A button
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()  # Update the gamepad to reflect the change
    print("A button released")

    # Wait for a short duration before pressing again
    time.sleep(0.5)

    # Release the left joystick
    gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()
    time.sleep(0.5)

    # Reset gamepad to default state
    gamepad.reset()
    gamepad.update()
    time.sleep(1.0)
