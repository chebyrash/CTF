#include <stdio.h>
#include <unistd.h>
#include <string.h>

// DEBUG ORIGINAL FLAG
// unsigned char flag[] = {0x43, 0x54, 0x46, 0x7B, 0x4D, 0x6F, 0x75, 0x73, 0x65, 0x5F, 0x52, 0x69, 0x67, 0x68, 0x74, 0x5F, 0x43, 0x6C, 0x69, 0x63, 0x6B, 0x5F, 0x74, 0x6F, 0x5F, 0x66, 0x6C, 0x61, 0x67, 0x7D};

unsigned char flag[] = {0x37, 0x26, 0x3F, 0x5B, 0x25, 0x0E, 0x07, 0x17, 0x11, 0x2D, 0x2B, 0x49, 0x0F, 0x09, 0x06, 0x3B, 0x37, 0x1E, 0x10, 0x43, 0x03, 0x3E, 0x06, 0x0B, 0x2B, 0x14, 0x15, 0x41, 0x0F, 0x1C};
unsigned char banner[] = {0x74, 0x72, 0x79, 0x20, 0x68, 0x61, 0x72, 0x64, 0x65, 0x72};

void donut(int spin) {
    if (spin == 0) {
        return;
    }

    printf("\nYou should've changed it :)\n");
    sleep(2);

             int k;double\
         sin(),cos();float A=
       0,B=0,i,j,z[1760];char b[
     1760];printf("\x1b[2J");for(;;
  ){memset(b,32,1760);memset(z,0,7040)
  ;for(j=0;6.28>j;j+=0.07)for(i=0;6.28
 >i;i+=0.02){float c=sin(i),d=cos(j),e=
 sin(A),f=sin(j),g=cos(A),h=d+2,D=1/(c*
 h*e+f*g+5),l=cos      (i),m=cos(B),n=s\
in(B),t=c*h*g-f*        e;int x=40+30*D*
(l*h*m-t*n),y=            12+15*D*(l*h*n
+t*m),o=x+80*y,          N=8*((f*e-c*d*g
 )*m-c*d*e-f*g-l        *d*n);if(22>y&&
 y>0&&x>0&&80>x&&D>z[o]){z[o]=D;;;b[o]=
 ".,-~:;=!*#$@"[N>0?N:0];}}/*#****!!-*/
  printf("\x1b[H");for(k=0;1761>k;k++)
   putchar(k%80?b[k]:10);A+=0.04;B+=
     0.02;usleep(25000);}/*****####*
       ~::==!!!**********!!!==::-
         .,~~;;;========;;;:~-.
             ..,--------,*/

}

void print_flag() {
    for (int x = 0; x < sizeof(flag); x++)
        printf("%c", flag[x] ^ banner[x % 8]);
    printf("\n");
}

// DEBUG TO OBFUSCATE FLAG
//void crypto() {
//    for (int x = 0; x < sizeof(flag); x++)
//        printf("0x%02X, ", flag[x] ^ banner[x % 8]);
//}

int main() {
    // DEBUG TO PRODUCE OBFUSCATED KEY
    // crypto();
    // return 0;

    setbuf(stdout, NULL);

    int spin = 1;

    printf("Welcome to Mineswee");

    for (int x = 0; x < 3; x++) {
        printf(".");
        usleep(750000);
    }

    printf("\nSegmentation fault\n");
    usleep(750000);

    donut(spin);

    print_flag();

    return 0;
}