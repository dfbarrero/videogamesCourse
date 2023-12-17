joysticks = arcade.get_joysticks()

if joysticks:
    self.joystick = joysticks[0]
    self.joystick.open()
else:
    print("There are no joysticks.")
    self.joystick = None
