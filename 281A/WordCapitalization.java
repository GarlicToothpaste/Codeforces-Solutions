//http://codeforces.com/problemset/problem/281/A
import java.util.*;

public class WordCapitalization{
	public static void main (String args[]){
		Scanner sc = new Scanner(System.in);
		String word = sc.nextLine();

		String sub = word.substring(0,1).toUpperCase();
		String ans = sub + word.substring(1);
		System.out.println(ans);	
	}
}