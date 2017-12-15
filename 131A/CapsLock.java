//http://codeforces.com/problemset/problem/131/A
import java.util.*;

public class CapsLock{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		String firstLetter = input.substring(0,1);
		String sub = input.substring(1, input.length());
		String compare = sub.toUpperCase();
		String ans = "";

		if(sub.equals(compare)){
			if(Character.isUpperCase(firstLetter.charAt(0))){
				ans = input.toLowerCase();
				System.out.println(ans);
			}
			else{
				ans = input.substring(0,1).toUpperCase() + sub.toLowerCase();
				System.out.println(ans);
			}

		}
		else{
			System.out.println(input);
		}

	}
}