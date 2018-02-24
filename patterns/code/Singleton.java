public class Singleton {
	private static Singleton INSTANCE = new Singleton();

	private Singleton() {}

	public static Singleton getInstance() { return INSTANCE; }
}
