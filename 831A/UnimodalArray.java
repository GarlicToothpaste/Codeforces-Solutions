//http://codeforces.com/problemset/problem/831/A
import java.util.ArrayList;
import java.util.Scanner;

public class UnimodalArray
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int[] al;
		int count = sc.nextInt();
		al = new int[count];
		for(int x = 0; x< count; x++){
			int num = sc.nextInt();
			al[x] = num;
		}
		System.out.println(unimodal(al));
	}
	public static String unimodal(int[] al){
		int state = 1;  // state == 1 if increasing
						//state == 2 if constant 
						//state == 3 if decreasing
		for (int x = 0; x< al.length-1 ; x++){
			if(state == 1){
				if (al[x] == al[x+1])
					state = 2;
				else {
					if (al[x] > al[x+1])
						state=3;
				} 
			}
			else if(state == 2){
				if(al[x]> al[x+1])
					state = 3;
				else{
					if(al[x]< al[x+1])
						return "NO";
				}
			}
			else if(state == 3){
				if(al[x] < al[x+1])
					return "NO";
				else{
					if (al[x] == al[x+1])
						return "NO";
				}
			}
		}
		return "YES";
	}
}
