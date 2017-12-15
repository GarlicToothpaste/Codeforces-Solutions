//http://codeforces.com/problemset/problem/577/A
import java.util.*;

public class MultTable{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		int count = 0;
		for(int a = 1 ; a <= x ; a++){
				if((y%a == 0) &&  (y/a)<=x) { // need (y/a)<= x because it counts the whole table of 1 if not
					count++;
				}
		}
		System.out.println(count);
	}
}