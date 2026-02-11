from morse.mapping import MORSE

REVERSE_MORSE = {value: key for key, value in MORSE.items()}


def decode_word(morse_word):
    letters = morse_word.split()
    decoded_letters = []

    for letter in letters:
        if letter in REVERSE_MORSE:
            decoded_letters.append(REVERSE_MORSE[letter])

    return "".join(decoded_letters)


def decode(morse_code):
    words = morse_code.split("|")
    decoded_words = []

    for word in words:
        decoded_words.append(decode_word(word))

    return " ".join(decoded_words)
