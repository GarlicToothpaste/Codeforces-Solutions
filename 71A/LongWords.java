//http://codeforces.com/problemset/problem/71/A
import java.util.*;
public class LongWords{
	public static void main (String args[]){
		String word;
		ArrayList<String> result = new ArrayList<String>();

		Scanner sc = new Scanner(System.in);
		int count = sc.nextInt();
		for(int x =0 ; x<= count ; x++){
			word = sc.nextLine();
			int len = word.length();
			if(len> 10){
				String first= word.substring(0,1);
				String last = word.substring(len-1,len);
				System.out.println(first+ (len -2 ) + last);
			}
			else{
				System.out.println(word);
				// result.add(word);
			}
		}
		// for(int x = 0 ; x< result.size() ; x++){
		// 	System.out.println(result.get(x));
		// }
	}
}