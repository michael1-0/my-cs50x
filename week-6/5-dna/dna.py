import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable

    with open(sys.argv[1], mode = 'r') as file:
        reader = csv.DictReader(file)
        database_file = [row for row in reader]


    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], mode = 'r') as file:
        sequence_file = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    str_count = {}
    for key in database_file[0].keys():
        if key == "name":
            continue
        str_count[key] = longest_match(sequence_file, key)

    # TODO: Check database for matching profiles
    for row in database_file:
        match = True
        for key in row.keys():
            if key == "name":
                continue
            if int(row[key]) != str_count[key]:
                match = False
                break
        if match:
            print(row["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
