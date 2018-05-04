package mySQL;

/** Imports. */
import java.sql.SQLException;
import java.util.Scanner;

/**
 * This class read the data from mySQL database and print the data.
 *
 * @author Johann and Samuel.
 */
public class PatientList {

	/**
	 * This method allow the user to input the id of the doctor.
	 */
	public static void userInput() {
		System.out.println("Please, would you input the id of the doctor.");
		@SuppressWarnings("resource") //Eclipse do not understand when the scanner is closed.
		Scanner scanner = new Scanner(System.in);
		int doctorID = scanner.nextInt();
		runTheQuery(doctorID);
	}

	//privates methods.

	/**
	 * This method build the SQL query.
	 * @param doctor
	 */
	private static String displayTheDoctorsData(Doctor doctor) {
		return 
				"SELECT P.pastient_name, QR.queue_time " + 
				"FROM " + 
				"my_Hospital.Patients AS P " + 
				"INNER JOIN " + 
				"my_Hospital.Queue_Reserved AS QR " + 
				"ON " + 
				"P.pastient_id = QR.pastient_id " + 
				"AND " + 
				"QR.doctor_id = " + doctor.getId() + 
				" ORDER BY(QR.Queue_time);";
	}

	/**
	 * This method run the query.
	 * @param doctorID
	 * @exception ClassNotFoundException | {@link SQLException}.
	 */
	private static void runTheQuery(int doctorID) {
		try {
			ExecuteQuery.pickFromDataBase(
					displayTheDoctorsData(
							new Doctor(
									doctorID
									)
							)
					);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
