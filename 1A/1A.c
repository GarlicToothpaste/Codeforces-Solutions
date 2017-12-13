#include <stdio.h>
int main()
{
	int length;
	int width;
	int side;
	int area1;
	int area2;
	int ans;
	scanf("%d" , &length);
	scanf("%d", &width);
	scanf("%d", &side);

	area1 = length*width;
	area2 = side*side;
	ans = area1%area2;
	ans = ans/area2;
	printf("%d", ans);

	
}

