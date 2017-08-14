#include<stdio.h>

void quickSort(int *a, int l, int r){
    if(l >= r){
        return;
    }
    int i = l;
    int j = r;
    int key = a[l];

    while(i < j){
        while(i < j && key <= a[j]){
            j--;
        }
        a[i] = a[j];
        
        while(i < j && key >= a[i]){
            i++;
        }
        a[j] = a[i];
    }

    a[i] = key;
    quickSort(a, l, i-1);
    quickSort(a, i+1, r);    
}

int main(){
    int i;
    int a[]={5, 6, 4, 1, 3};
    quickSort(a, 0, 4);
    for(i=0; i<=4; i++){
        printf("%d\n", a[i]);
    }
}
