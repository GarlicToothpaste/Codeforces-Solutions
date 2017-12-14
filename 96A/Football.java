//http://codeforces.com/problemset/problem/96/A

import java.util.*;

public class Football{
	public static void main (String args[]){
		int countOne = 0;
		int countZero = 0;
		int trigger = 0;

		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		int len = input.length();
		for(int x = 0; x< len; x++){
			if(Character.toString(input.charAt(x)).equals("0")){
				countZero++;
				countOne=0;;
			}
			if(Character.toString(input.charAt(x)).equals("1")){
				countZero=0;
				countOne++;
			}
			if(countOne>=7 || countZero>=7){
				trigger=1;
			}
		}
		if(trigger==1){
			System.out.println("YES");
		}
		else{
			System.out.println("NO");
		}
	}
}