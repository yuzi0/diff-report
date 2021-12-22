#include <stdio.h>

void hello()
{
    printf("Hello, world!\n");
}

void bye()
{
    printf("Bye!\n");
    printf("Have a nice day!\n");
}

void doNothing()
{
    //doNothing
}

int main()
{
    hello();
	bye();
	doNothing();

    return 0;
}