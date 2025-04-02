%{
# include<stdio.h>
%}

%%

charusat  {printf("university");}

%%
int yywrap()
{
return 1;
}

void main()
{
yylex();
}
