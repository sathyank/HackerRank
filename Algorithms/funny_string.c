#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
char* reverse(char* s){
    

    
    int i=0,l=strlen(s),j=l-1;
	    char* str = (char *)malloc(l * sizeof(char));
    while (i < l) {
      str[i] = s[j];
	i++;
	j--;
      	
   }
	str[i] = '\0';
   printf("%s",str);
   return str;
}
char* funnyString(char* s){
    //char f[6] = "Funny";
    //char nf[12] = "Not Funny";
    int l = strlen(s),i;
    
     char* r=reverse(s);
    printf("%s",s);
    printf("%s",r);
    for(i=0;i<l;i++){
        if(abs(s[i+1]-s[i]) == abs(r[i+1]-r[i])){
	    printf("abs(s[i+1]-s[i])=%d,abs(r[i+1]-r[i]=%d",abs(s[i+1]-s[i]),abs(r[i+1]-r[i]));
            continue;
	}
        else
            return "Not Funny";
    }
    return "Funny";
}

int main() {
    int q; 
    scanf("%i", &q);
    for(int a0 = 0; a0 < q; a0++){
        char* s = (char *)malloc(512000 * sizeof(char));
        scanf("%s", s);
        int result_size;
        char* result = funnyString(s);
        printf("%s\n", result);
    }
    return 0;
}

