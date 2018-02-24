class SlickLoop extends BasicGame {
	@Override
	public void init(GameContainer container) throws SlickException {
		// Init game
	}

	@Override
	public void update(GameContainer container, int delta) throws SlickException {
		// Update world
	}

	@Override
    public void render(GameContainer container, Graphics g) throws SlickException {
		// Render world
    }

	public static void main(String arg[]) {
		// Launch game
		try {
	    	new SlickLoop();
		} catch (SlickException e) { }
}
