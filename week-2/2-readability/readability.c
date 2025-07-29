#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int letters(string text);
int words(string text);
int sentences(string text);

int main(void)
{
    string text = get_string("What's on your mind?\n");
    int count_letter = letters(text);
    int count_words = words(text);
    int count_sentences = sentences(text);

    float L = (float) count_letter / (float) count_words * 100;
    float S = (float) count_sentences / (float) count_words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    printf("Text: %s\n", text);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int letters(string text)
{
    int letters = 0;
    for (int i = 0, j = strlen(text); i < j; i++)
    {
        if (isspace(text[i]) || ispunct(text[i]) || isdigit(text[i]))
        {
            ;
        }

        else if (isupper(text[i]))
        {
            letters++;
        }

        else if (islower(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int words(string text)
{
    int words = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isspace(text[i]))
        {
            words++;
        }
    }
    return words;
}

int sentences(string text)
{
    int sentences = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text [i] == '!')
        {
            sentences++;
        }
    }
    return sentences;
}