public class CarFactory {
	public static Car buildCar(String model) {
		switch (model) {
			case "small":
				return new SmallCar();
 		 	case "sedan":
 		 		return new SedanCar();	
   		case "luxury":
   			return new LuxuryCar();
			}
		}
}
