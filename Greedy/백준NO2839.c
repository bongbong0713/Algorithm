#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int n,num=0,tmp=0;

	scanf("%d", &n);
	tmp = n;
	while (tmp>0) {
		tmp -= 5;
		num++;
		if (tmp % 3 == 0 && tmp<=12) {
			num += tmp / 3;
			break;
		}
	}
	if (tmp < 0) {
		if (n % 3 == 0)
			num = n / 3;
		else
			num = -1;
	}
	printf("%d\n", num);
}
