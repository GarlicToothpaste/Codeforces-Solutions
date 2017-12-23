import java.util.*;
//http://codeforces.com/problemset/problem/58/A
public class Chatroom{

	public static void main (String args[]){
		Scanner sc = new Scanner (System.in);
		String input = sc.nextLine().toLowerCase();
		String ideal = "hello";
		String output = "NO";
		int i = 0;
		for(int x = 0; x< input.length(); x++){
			//System.out.println(input.charAt(x));
			
			if(input.charAt(x) == ideal.charAt(i)){
				//System.out.println("SAME");
				//System.out.println(input.charAt(x));
				//System.out.println(i);
				i++;
				
			}
			if(i == 5){
				output = "YES";
				break;
			}

		}
		System.out.println(output);
	}
}
