%option noyywrap

%{

#include<stdio.h>
#include<string.h>
#include<ctype.h>	
 
void check_password(char *yytext)
{
int has_digit = 0,has_lower=0,has_upper=0,has_special=0;
int length = strlen(yytext);

if (length<9 || length>15)
{
printf("Invalid Password");
}

for (int i=0; i<length; i++)
{
if (isupper(yytext[i])) has_upper=1;
else if (islower(yytext[i])) has_lower=1;
else if (isdigit(yytext[i])) has_digit=1;
else if (strchr(";*#$@",yytext[i])) has_special=1;
}

if (has_upper && has_lower && has_digit && has_special)
{
printf("Valid String");
}
else
{
printf("Invalid String");
}
}

%}	

%%

[a-zA-Z0-9*#$@;]{9,15}     {check_password(yytext);}

%%

int main(){
yylex();
return 0;
}
