//http://codeforces.com/problemset/problem/118/A
import java.util.*;

public class StringTask{
	public static void main (String args[]){
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();

		input = input.toLowerCase().replaceAll("[aeiouy]", "").replaceAll("(.)", ".$1");
		System.out.println(input);
	}
}