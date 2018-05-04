package mySQL;

/** Imports. */
import java.sql.SQLException;
import java.util.Scanner;

/**
 * This class create the query to use the stored procedure.
 *
 * @author Johann and Samuel.
 */
public class PhysicalEntry {
	
	/**
	 * This method allow the user to input the name of the patient.
	 */
	public static void userInput() {
		System.out.println("Please, would you input the name of the patient.");
		Scanner scanner = new Scanner(System.in);
		String clientName = scanner.nextLine();
		runTheQuery(clientName);
		scanner.close();
	}
	
	//privates methods.
	
	/**
	 * This method run the query.
	 * @param clientName
	 * @exception ClassNotFoundException | {@link SQLException}.
	 */
	private static void runTheQuery(String clientName) {
		try {
			ExecuteQuery.pickFromDataBase(
					enterANewClient(clientName)
					);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	
	/**
	 * This method build the SQL query.
	 * @param clientName
	 */
	private static String enterANewClient(String clientName) {
		return 
				"call my_Hospital.physical_entry('" +  clientName + "');";
	}

}
