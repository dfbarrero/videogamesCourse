import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "Example of sound in Arcade")

music = arcade.load_sound(
        ":resources:/music/1918.mp3", 
        streaming=True)
# music = Sound(":resources:/music/1918.mp3", streaming=True) 
arcade.play_sound(music)
# music.play() # Object-oriented style

arcade.start_render()
arcade.draw_text("Enjoy!", 350, 300, arcade.color.WHITE)
arcade.finish_render()

arcade.run()
