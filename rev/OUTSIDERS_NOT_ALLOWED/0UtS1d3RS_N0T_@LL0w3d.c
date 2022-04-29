#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void printFlag()
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
  volatile int to_be_modded;
  char buffer[64];
  char *var;

  var = getenv("OUTSIDER");

  if(var == NULL) {
      errx(1, "Please set the 'OUTSIDER' ENV VARIABLE\n");
  }

  to_be_modded = 0;

  strcpy(buffer, var);

  if(to_be_modded == (int)0x84929076) {
      printFlag();
  } else {
      printf("Try again, you got 0x%08x\n", to_be_modded);
  }

}
