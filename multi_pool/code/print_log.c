#include <stdlib.h>
#include <time.h>


int main(void) {
    while(1) {
        sleep(2);
        system("cat /home/penper/pre.log");
    }
}