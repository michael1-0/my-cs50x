#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = (int)((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0 + .5);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int ogRED = image[i][j].rgbtRed;
            int ogGREEN = image[i][j].rgbtGreen;
            int ogBLUE = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = fmin(255, (int)(.393 * ogRED + .769 * ogGREEN + .189 * ogBLUE + .5));
            image[i][j].rgbtGreen = fmin(255, (int)(.349 * ogRED + .686 * ogGREEN + .168 * ogBLUE + .5));
            image[i][j].rgbtBlue = fmin(255, (int)(.272 * ogRED + .534 * ogGREEN + .131 * ogBLUE + .5));
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 -j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
