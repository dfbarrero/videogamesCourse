def on_mouse_press(self, x, y, button, modifiers):
    """ Called when the user presses a mouse button. """

    if button == arcade.MOUSE_BUTTON_LEFT:
        print("Left mouse button pressed at", x, y)
    elif button == arcade.MOUSE_BUTTON_RIGHT:
        print("Right mouse button pressed at", x, y)
