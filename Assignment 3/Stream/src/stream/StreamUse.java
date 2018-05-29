package stream;

import java.util.Arrays;

public class StreamUse {

	public static void main(String[] args) {
		Arrays.asList('a', 'b', 'c', 'g', 'H', 'i', 't', 'u', 'v')
		.stream()
		.forEach(
				(c) 
				-> 
				{
					if (c > 'g' && c < 'o')
						System.out.println((char) ('z' - c + 'a'));
					else if (c > 'G' && c < 'O')
						System.out.println((char) ('Z' - c + 'A'));
				}
				);
	}
}
