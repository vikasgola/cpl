#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
void smashSix()
{
    FILE * f = fopen("flag.txt","r");
    if(f == NULL)
    {
        perror("No flag file present");
        exit(EXIT_FAILURE);
    }
    char c;
    while(c!=EOF)
    {
        printf("%c", c);
        c = fgetc(f);
    }
    fclose(f);
}

int main(int argc, char **argv)
{
  volatile int six;
  char buffer[64];

  six = 0;
  gets(buffer);

  if(six != 0) {
      smashSix();
  } else {
      printf("Smashing Stack is not some Child's play!!");
  }
}
