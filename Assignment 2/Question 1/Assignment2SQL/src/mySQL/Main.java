package mySQL;

/**
 * This class contains the main method to make test and run the things we need.
 *
 * @author Johann and Samuel.
 */
public class Main {

	/**
	 * The main method.
	 * @param args
	 */
	public static void main(String[] args) {
		PatientList.userInput(); // Static method.
		ViewOfTheTenthPatients.runTheQuery(); //Static method.
		PhysicalEntry.userInput(); //Static method.
	}
}
