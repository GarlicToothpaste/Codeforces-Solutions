//http://codeforces.com/problemset/problem/112/A

import java.util.*;

public class PetyaStrings{
	public static void main (String args[]){
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		String input2 = sc.nextLine();

		input = input.toLowerCase();
		input2 = input2.toLowerCase();
		
		int res = input.compareTo(input2);
		if(res<0){
			res=-1;
		} 
		if(res>0){
			res=1;
		}
		System.out.println(res);
	}
}