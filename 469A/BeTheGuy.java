//http://codeforces.com/problemset/problem/469/A
import java.util.*;

public class BeTheGuy{
	public static void main (String args[]){
		Scanner sc = new Scanner(System.in);
		int level = sc.nextInt();
		int [] allLevels = new int [level]; 
		int [] ezLevels = new int[level];
		for (int x = 0; x < level ; x++){
			allLevels[x] = x+1;
		}

		int player1 = sc.nextInt();
		for (int x = 0; x < player1 ; x++){
			int p1Levels = sc.nextInt();
			ezLevels[p1Levels-1] = p1Levels;
		}

		int player2 = sc.nextInt();
		for (int x = 0; x < player2 ; x++){
			int p2Levels = sc.nextInt();
			ezLevels[p2Levels-1] = p2Levels;
		}

		boolean equal = Arrays.equals(allLevels, ezLevels);
		if(equal == true){
			System.out.println("I become the guy.");
		}
		else{
			System.out.println("Oh, my keyboard!");
		}
	}
}