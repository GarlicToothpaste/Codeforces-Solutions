//http://codeforces.com/problemset/problem/59/A
import java.util.*;

public class Word{
	public static void main (String args[]){
		int upperCase = 0;
		int lowerCase = 0;

		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		int len = input.length();

		for (int x = 0; x < len; x++){
			if(Character.isUpperCase(input.charAt(x))){
				upperCase++;
			}
			if(Character.isLowerCase(input.charAt(x))){
				lowerCase++;
			}
		}
		if(upperCase>lowerCase){
			input = input.toUpperCase();
		}
		else{
			input = input.toLowerCase();
		}
		System.out.println(input);
	}
}