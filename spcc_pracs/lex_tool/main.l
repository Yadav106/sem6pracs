%{
  #define Header 3
  #define Number 1
  #define Key 2
  #define ID 7
  #define NewLine 4
  #define Punc 6
  #define Comment 5
  #define Literal 8
%}

%%
[0-9]+|[0-9]+\.[0-9]+ {return Number;}
main|int|char|int|void {return Key;}
[a-zA-z]+[a-zA-Z0-9]* {return ID;}
\[\n]*\  {return NewLine;}
\<[a-z]\.h\> {return Header;}
[!@#$^&*(){}:;,./<>?+=-] {return Punc;}
\/\/|\/\*+[a-zA-z]+[a-zA-Z0-9]* {return Comment;}
["][a-zA-Z]*["] {return Literal;}
%%

#include<stdio.h>
int main(int arg,char *argv[]) {
  int val;
  while(val=yylex()) {
    switch(val) {
      case 1:
        printf("\n%s - Number",yytext);
        break;
      case 2:
        printf("\n%s - Keyword",yytext);
        break;
      case 3:
        printf("\n%s - Header File",yytext);
        break;
      case 4:
        printf("\nNew Line");
        break;
      case 5:
        printf("\n%s - Comment",yytext);
        break;
      case 6:
        printf("\n%s - Symbol",yytext);
        break;
      case 7:
        printf("\n%s - Identifier",yytext);
        break;
      case 8:
        printf("\n%s - Literal",yytext);
        break;
      default:
        printf("Invalid choice");
        break;
    }
  }
}
