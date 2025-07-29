#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: copy inputfile outputfile\n");
        return 1;
    }
    // Open input file for reading
    // TODO #2
    char *input = argv[1];
    FILE *in = fopen(input, "rb");
    if (in == NULL)
    {
        printf("Could not open %s.\n", input);
        return 1;
    }
    // Read header
    // TODO #3
    WAVHEADER header;
    fread (&header, sizeof(WAVHEADER), 1, in);
    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) == 0)
    {
        printf("Not a WAV file\n");
        return 1;
    }

    if (header.audioFormat != 1)
    {
        printf("Not a WAV file\n");
        return 1;
    }
    // Open output file for writing
    // TODO #5
    char *output = argv[2];
    FILE *out = fopen(output, "wb");
    if (out == NULL)
    {
        printf("Could not open %s.\n", output);
        return 1;
    }
    // Write header to file
    // TODO #6
    fwrite (&header, sizeof(WAVHEADER), 1, out);
    // Use get_block_size to calculate size of block
    // TODO #7
    int size = get_block_size(header);
    // Write reversed audio to file
    // TODO #8
    if (fseek(in, size, SEEK_END))
    {
        return 1;
    }
    BYTE buffer[size];
    while (ftell(in) - size > sizeof(header))
    {
        if (fseek(in, - 2 * size, SEEK_CUR))
        {
            return 1;
        }s
        fread(buffer, size, 1, in);
        fwrite(buffer, size, 1, out);
    }


    fclose(out);
    fclose(in);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int size = header.numChannels * header.bitsPerSample / 8;
    return size;
}