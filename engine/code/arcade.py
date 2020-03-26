import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Arcade")

	def setup(self):
		pass

	def on_draw(self):
		arcade.start_render()

	def on_update(self, delta_time):
		pass

def main():
	window = MyGame()
	window.setup()
	arcade.run()

main()
