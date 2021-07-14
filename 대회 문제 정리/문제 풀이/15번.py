#include <stdio.h>

int main(){
    int num[7];
    int my_num[6];
    int i;
    for(i=0;i<7;i++) scanf("%d ", &num[i]);
    for(i=0;i<6;i++) scanf("%d ", &my_num[i]);
    
    int check=0;
    int bonus=0;
    
    for(i=0;i<6;i++){
        if(my_num[i]==num[0]||my_num[i]==num[1]) check++;
        if(my_num[i]==num[2]||my_num[i]==num[3]) check++;
        if(my_num[i]==num[4]||my_num[i]==num[5]) check++;
        if(my_num[i]==num[6]) bonus++;
    }
    
    if(check==6) printf("1");
    else if(check==5&&bonus==1) printf("2");
    else if(check==5) printf("3");
    else if(check==4) printf("4");
    else if(check==3) printf("5");
    else printf("0");
}

#c로 작성
#32:15