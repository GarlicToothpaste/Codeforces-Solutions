//http://codeforces.com/contest/282/problem/A

#include <stdio.h>
#include <string.h>
int main()
{
    int input; 
    int x = 0;
    char input2[1000];
    scanf("%d", &input);
    for (input; input >0 ; input--)
    {
        scanf("%s", input2);
        if(strcmp(input2, "X++")== 0 )
        {
            x= x+1;
	    continue;
        }
        if(strcmp(input2, "++X")== 0 )
        {
            x= x+1 ;
	    continue;
        }
        if(strcmp(input2, "--X")== 0 )
        {
            x= x-1;
	    continue;
        }
        if(strcmp(input2, "X--")== 0 )
        {
            x= x-1;
	    continue;
        }
        
    }
	printf("%d", x);
}
