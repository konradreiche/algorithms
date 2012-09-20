#include <stdio.h>
#include <string.h>

/*
 * Question
 *
 *      Implement a function void reverse(char* str) in C which reverses a
 *      null-terminated string.
 *
 * Solution 1
 *
 *      The string is simply reversed by iterating the string and using a
 *      temporary variable. It is important to consider the null character
 *      and handle the case when NULL is passed to the function.
 *      
 *      Time Complexity O(n)
 *      Space Complexity O(n)
 *
 */
void reverse(char* str)
{
        if (str == NULL)
                return;

        int len = strlen(str);
        int tmp, i, j;
        for (i = 0, j = len - 1; i < j; i++, j--)
        {
                tmp = str[i];
                str[i] = str[j];
                str[j] = tmp;
        }
        str[len] = '\0';
}

/*
 * Solution 2
 *
 *      If is not allowed to use the string library and/or to avoid writing a
 *      strlen(str) function the problem can also be solved with pointer
 *      operations.
 *
 *      Time Complexity O(n)
 *      Space Complexity O(n)
 *
 */
void reverse2(char* str)
{
        if (str == NULL)
                return;

        char* end = str;
        char tmp;
        while (*end != '\0') {
                ++end;
        }
        --end;

        while (str < end) {
                tmp = *str;
                *str = *end;
                *end = tmp;
                ++str;
                --end;
        }
}

int main(int argc, char** argv)
{
        char* str1 = "Hello Berlin";
        char* str2 = NULL;

        reverse(str1);
        reverse(str2);

        printf("%s\n", str1);

        reverse2(str1);
        reverse2(str2);
        
        printf("%s\n", str1);

        return 0;
}
