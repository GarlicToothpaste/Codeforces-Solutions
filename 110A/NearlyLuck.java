//http://codeforces.com/problemset/problem/110/A
import java.util.*;

public class NearlyLuck{
	public static void main (String args[]){
		Scanner sc = new Scanner (System.in);
		String input = sc.nextLine();
		int len = input.length();
		int trigger =0;
		int count = 0;
		for (int x = 0; x < len ; x++){
			char elem = input.charAt(x);
			String s = Character.toString(elem);
			int intElem = Integer.parseInt(s);
			if (intElem == 4 || intElem == 7){
				count++;
			}
			else{
				trigger=1;
			}

		}
		if ( count ==  4 || count  ==7){
			System.out.println("YES");
		}
		else{
			System.out.println("NO");
		}
	}
}