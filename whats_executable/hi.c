/*
 * hi.c
 */

#include <stdio.h>
#include <unistd.h>

void say_hi(void) {
    char name[8];
    int bytes;

    printf("Enter your name: ");
    fflush(stdout);
    bytes = read(0, name, 80);
    name[bytes-1] = '\0';
    printf("Hello %s!\n", name);
}

int main(int argc, char *argv[])
{
    say_hi();
}


