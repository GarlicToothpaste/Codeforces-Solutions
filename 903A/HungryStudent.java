//http://codeforces.com/problemset/problem/903/A
import java.util.*;

public class HungryStudent{
	public static void main (String args[]){
		Scanner sc = new Scanner(System.in); 
		int count = sc.nextInt();
		for (int x = 0; x<count; x++){
			int num = sc.nextInt();
			if(num == 1 || num == 2 || num ==4 || num ==5 || num == 8 || num == 11){
				System.out.println("NO");
			}
			else{
				System.out.println("YES");
			}

		}
	}
}