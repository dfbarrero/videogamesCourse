class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        """ Initialize everything """

        # Initialize the parent class
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Create the sprites and set up the game """
        pass

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # TODO: Drawing code goes here
