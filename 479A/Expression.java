//http://codeforces.com/problemset/problem/479/A
import java.util.*;

public class Expression{
	public static void main (String args[]){
		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		int op1 = a+b+c;
		int op2 = a+b*c;
		int op3 = a*b+c;
		int op4 = (a+b)*c;
		int op5 = a*(b+c);
		int op6 = a*b*c;

		int ans;
		ans = op1;
		if(ans < op2){
			ans= op2;
		}
		if(ans < op3){
			ans = op3;
		}
		if(ans < op4){
			ans = op4;
		}
		if(ans < op5){
			ans = op5;
		}
		if(ans < op6){
			ans = op6;
		}

		System.out.println(ans);
	}
}