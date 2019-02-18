//スキルチェック練習問題「文字列収集」より

#include <stdio.h>
#include <string.h>
int main(void){
    int n,m;
    int i,j;
    
    scanf("%d %d\n",&n,&m);
    
    char s[n][100];
    int p[n];
    
    for(i=0;i<n;i++){
        scanf("%s %d\n",s[i],&p[i]);
    }
    
    char q[100];
    int total;

    for(i=0;i<m;i++){
        scanf("%s\n",q);
        total = 0;
        for(j=0;j<n;j++){
            if(strncmp(q,s[j],strlen(q))==0){
                total += p[j];
            }
        }
        printf("%d\n",total);
    }
    
    return 0;
}
