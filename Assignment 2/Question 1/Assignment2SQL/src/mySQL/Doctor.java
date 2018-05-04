package mySQL;

/**
 * This class represent a doctor.
 * For now, the only thing needed is the id of the doctor, and his name.
 * 
 * @author Johann and samuel.
 */
public class Doctor {

	/** The id */
	private int id; //primary key (non null).
	private String firstName, 
				   lastName;

	/**
	 * Constructor.
	 * @param id
	 * @param firstName
	 * @param lastName
	 */
	public Doctor(int id, String firstName, String lastName) {
		this.id = id;
		this.firstName = firstName;
		this.lastName = lastName;
	}

	/**
	 * Constructor.
	 * @param id
	 */
	public Doctor(int id) {
		this.id = id;
		this.firstName = "unknown";
		this.lastName = "unknown";
	}
	
	/**
	 * Get id.
	 * @return id.
	 */
	public int getId() {
		return id;
	}

	/**
	 * Get fistName.
	 * @return fistName.
	 */
	public String getFirstName() {
		return firstName;
	}

	/**
	 * Get lastName.
	 * @return lastName.
	 */
	public String getLastName() {
		return lastName;
	}	
}
