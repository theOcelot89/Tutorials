import java.util.Scanner;
import javax.swing.JOptionPane;


public class Main {

	public static void main(String[] args) {

//		System.out.print("I love pizza");
//		// This is a comment
//		System.out.println();
//		
//		int x; // declaration
//		x = 128543;  // assignment
//		int y = 124; // initialization
//		System.out.println("x equals: " + x);
//		
//		long z = 238475334; // longer number
//		float f = 123.3124f; // float number
//		String name = "Angel";
//		System.out.print(name);
//		
//		
//		// User Input
//		Scanner scanner = new Scanner(System.in);
//		System.out.println("What is your name?");
//		String name1 = scanner.nextLine();
//		System.out.println("Hello " + name1);		
 
		// GUI 		
//		String name = JOptionPane.showInputDialog("Enter your name");
//		JOptionPane.showMessageDialog(null,"Hello " + name);
		
		Garage garage = new Garage();
		Car car = new Car("Ford");
		
//		System.out.println(car.name);
		garage.park(car);
	}

}
