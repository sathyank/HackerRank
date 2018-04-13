#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char* timeConversion(char* s) {
    int l = strlen(s);
    char hr[2];
    hr[0] = s[0];
    hr[1] = s[1];
    hr[2] = '\0';
    int hour = atoi(hr);
    if(s[l-2] == 'P'){
        if(hour == 12){
            s[0] = '1';
            s[1] = '2';
        }
        else
        {    
            hour = hour + 12;
            sprintf(hr,"%d",hour);
            s[0] = hr[0];
            s[1] = hr[1];
        }   
    }
    if(s[l-2] == 'A'){
        if(hour == 12){
            s[0] = '0';
            s[1] = '0';
        }   
    }
    s[l-2] = '\0';
    return s;    
}

int main() {
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
        int result_size;
char* result = timeConversion(s);
    printf("%s\n", result);
    return 0;
}
