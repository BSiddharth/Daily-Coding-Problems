# Easy

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.


def encoder(string):
    count = 0
    currentRepetition = ''
    encodedWord = ''
    for alphabet in string:
        if alphabet == currentRepetition:
            count += 1
        else:
            if count != 0:
                encodedWord += str(count)+currentRepetition
            currentRepetition = alphabet
            count = 1
    encodedWord += str(count)+currentRepetition
    print(encodedWord)


encoder('AAAABBBCCDAA')
