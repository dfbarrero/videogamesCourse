public class Screen implements Observer {
	@Override
	public void update(Observable ob, Object arg) {
		// Do something
	}

	public static void main(String args[]) {
		Screen screen = new Screen();
		DataStore datastore = new DataStore();
		datastore.addObserver(screen);
	}
}
