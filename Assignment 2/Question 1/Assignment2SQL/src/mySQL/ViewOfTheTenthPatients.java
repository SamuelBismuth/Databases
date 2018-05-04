package mySQL;

/** Import. */
import java.sql.SQLException;

public class ViewOfTheTenthPatients {

	/**
	 * This method run the query.
	 * @param doctorID
	 * @exception ClassNotFoundException | {@link SQLException}.
	 */
	public static void runTheQuery() {
		try {
			ExecuteQuery.pickFromDataBase(
					displayTheView()
					);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	//private method.
	
	/**
	 * This method build the SQL query.
	 * @param doctor
	 */
	private static String displayTheView() {
		return 
				"SELECT * FROM my_Hospital.`new_view`;";
	}
	
}
