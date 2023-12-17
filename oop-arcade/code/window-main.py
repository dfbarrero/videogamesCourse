def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game Title")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
