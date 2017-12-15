//http://codeforces.com/problemset/problem/200/B
import java.util.*;

public class Drinks{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		double testCases = sc.nextDouble();
		double ans = 0;
		for (int x = 0 ; x < testCases ; x++){
			double currInput= sc.nextFloat();
			ans = ans + currInput;
		}		
		ans = ans/testCases;
		System.out.println(ans);
	}
}