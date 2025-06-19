#include <stdio.h>
#include <stdlib.h>

int main(void);

int main(void) {
  int response;
  response = system("git rev-parse --is-inside-work-tree 1>/dev/null 2>/dev/null");
  if (response == 0) {
    printf("True");
  } else {
    printf("False");
  }
}
