class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    def __init__(self, texture_list):
        super().__init__(texture_list[0])
        # How long the explosion has been around.
        self.time_elapsed = 0

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self, delta_time=1 / 60):
        self.time_elapsed += delta_time
        # Update to the next frame of the animation. 
        # If we are at the end of our frames, then delete this sprite.
        self.current_texture = int(self.time_elapsed * 60)
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        
        else:
            self.remove_from_sprite_lists()
