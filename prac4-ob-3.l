%{
#include <stdio.h>
#include <stdlib.h>

int char_count = 0, word_count = 0, line_count = 0;
%}

%%
\n        { line_count++; char_count++; }
[^\n\t ]+ { word_count++; char_count += yyleng; }
.         { char_count++; }

%%

int main() {
    yylex();  // Process input

    // If input is non-empty, count the last line if it didn't end with \n
    if (char_count > 0 && line_count == 0) {
        line_count = 1;  
    }

    printf("Characters: %d\n", char_count);
    printf("Words: %d\n", word_count);
    printf("Lines: %d\n", line_count);
    
    return 0;
}

int yywrap() {
    return 1;
}
