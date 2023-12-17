class arcade.Sprite(
        filename: Optional[str] = None, 
        scale: float = 1, 
        image_x: float = 0, # offset within sprite sheet
        image_y: float = 0, # offset within sprite sheet
        image_width: float = 0, 
        image_height: float = 0, 
        center_x: float = 0, 
        center_y: float = 0, 
        repeat_count_x: int = 1, 
        repeat_count_y: int = 1, 
        flipped_horizontally: bool = False, 
        flipped_vertically: bool = False, 
        flipped_diagonally: bool = False, 
        hit_box_algorithm: Optional[str] = 'Simple', 
        angle: float = 0)
