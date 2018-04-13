#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

 
void insertionSort(int ar_size, int *  ar) {

int i, key = ar[ar_size-1], j;
   for (i = ar_size-2; i >=0; i--)
   {
     
	
       if(key<ar[i]){
           ar[i+1] = ar[i];
       
 
       j=0;
       while (j<ar_size)
       {
           printf("%d ",ar[j]);
           j++;
       }
       printf("\n");
       }
	if(i==0 && (ar[0]==ar[1]))
{
ar[i] = key;
j=0;
        while (j<ar_size)
        {
               printf("%d ",ar[j]);
            j++;
        }
}
       else if(key>ar[i]){
           ar[i+1]=key;
           j=0;
        while (j<ar_size)
        {
               printf("%d ",ar[j]);
            j++;
        }
           break;
       }
   }
}
int main(void) {
    int _ar_size;
    scanf("%d", &_ar_size);
    int _ar[_ar_size], _ar_i;
    for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
        scanf("%d", &_ar[_ar_i]); 
    }

    insertionSort(_ar_size, _ar);
    return 0;
}

