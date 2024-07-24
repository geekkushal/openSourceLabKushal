#include<stdio.h>
int main(){
    printf("Code by KUSHAL AJWANI\n");
    printf("C Code for printing average of numbers by taking n integers as input \n");
    printf("\n\nEnter n: ");
    int n;
    scanf("%d",&n);
    printf("\n\nEnter values: \n");

    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",arr+i);
    }

    int sum = 0;
    for(int i=0;i<n;i++){
        sum += arr[i];
    }

    float avg = (sum / (n*1.0));

    printf("\n\nThe average of the given %d numbers is %f\n\n",n,avg);
    return 0;
}
