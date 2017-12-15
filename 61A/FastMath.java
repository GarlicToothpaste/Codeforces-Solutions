//http://codeforces.com/problemset/problem/61/A
import java.util.*;

public class FastMath{
	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		String input1 = sc.nextLine();
		String input2 = sc.nextLine();

		String ans = "";

		for (int x = 0 ; x<input1.length(); x++){
			String temp;
			if(input1.charAt(x)==input2.charAt(x)){
				temp = "0";
			}
			else{
				temp = "1";
			}

			ans = ans + temp;
		}
		System.out.println(ans);
	}
}