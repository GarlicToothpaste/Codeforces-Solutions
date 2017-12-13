//http://codeforces.com/problemset/problem/158/A

import java.util.*;

public class NextRound{
	public static void main (String args[]){

		Scanner sc = new Scanner(System.in);
		int numPart = sc.nextInt();
		int numPlace = sc.nextInt();
		int [] num = new int [numPart];
		int count = 0;
		int basis=0;
		int status = 0;
		for(int x = 0 ; x< numPart; x++){
			int score = sc.nextInt();
			num[x] = score;
			if(score>0){
				status = 1;
			}

		}

		for(int x = 0; x< numPart; x++){
			basis = num[numPlace-1];
			if(num[x]>= basis && status == 1 && num[x] > 0){
				count++;
			}
		}
		System.out.println(count);
	}
}