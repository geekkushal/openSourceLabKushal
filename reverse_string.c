#include<stdio.h>
int main(){
    printf("Code by KUSHAL AJWANI\n");
    printf("C Code for reversing the given string \n");
    printf("\n\nEnter length of string: ");
    int n;
    scanf("%d",&n);
    printf("\n\nEnter string: \n");

    while(getchar()!='\n');

    char s[n+1];
    for(int i=0;i<n;i++){
        scanf("%c",s+i);
    }
    s[n] = '\0';

    int i = 0;
    int j = n - 1;

    while(i<=j){
        char k = s[i];
        s[i] = s[j];
        s[j] = k;
        i++;
        j--;
    }

    printf("\n\nThe reversed string is %s\n\n",s);
    return 0;
}
