#include<stdio.h>
void bin(unsigned n)
{
    unsigned i;
    for (i = 1 << 31; i > 0; i = i / 2)
        (n & i) ? printf("1") : printf("0");
}
 
int main(void)
{
	printf("7\n");
    bin(7);

    printf("\n\n");

	printf("4\n");
    bin(4);
}
