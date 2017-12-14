//http://codeforces.com/problemset/problem/41/A
import java.util.*;

public class Translation{
	public static void main (String args[]){
		int trigger = 0;

		Scanner sc = new Scanner(System.in);
		String input1 = sc.nextLine();
		String input2 = sc.nextLine();
		
		String reverse = new StringBuffer(input2).reverse().toString();
		if(reverse.equals(input1)){
			System.out.println("YES");
		}
		else{
			System.out.println("NO");
		}
	}
}