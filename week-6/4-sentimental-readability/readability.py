import cs50

def main():
    user_text = cs50.get_string("Text: ")

    count_letter = letters(user_text)
    count_words = words(user_text)
    count_sentences = sentences(user_text)

    L = count_letter /  count_words * 100
    S = count_sentences / count_words * 100
    coleman = round(0.0588 * L - 0.296 * S - 15.8)

    if coleman < 1:
        print("Before Grade 1")
    elif coleman >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {coleman}")


def letters(ftext):
    letters = 0

    for i in ftext:
        if i.isalpha():
            letters += 1

    return letters


def words(ftext):
    words = 1

    for i in ftext:
        if i == " ":
            words += 1

    return words


def sentences(ftext):
    sentences = 0

    for i in ftext:
        if i == "!" or i == "." or i == "?":
            sentences += 1

    return sentences


if __name__ == "__main__":
    main()
