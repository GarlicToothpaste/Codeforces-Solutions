import java.util.*;

public class LocalExtrema{
	public static void main (String args[]){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int count=0;
		int [] arr;

		arr = new int [n];

		for(int x =0 ; x<= arr.length-1; x++){
			int input = sc.nextInt();

			arr[x] = input;
		}

		for(int x=1; x<= arr.length-1 ; x++){
			int temp = arr[x];
			
			if(x>0 && x<n-1){

				if( temp>arr[x-1] && temp>arr[x+1]){
					count++;
				}
				else if( temp<arr[x-1] && temp<arr[x+1]){
					count++;
				}

			}
			if (x==n){
				break;
			}
		}
		System.out.println(count);
	}
}