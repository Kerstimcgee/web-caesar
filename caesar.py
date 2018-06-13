<script src="https://gist.github.com/chrisbay/496880de24bba4f532ed03211eff7294.js"></script>
  
 Code  Revisions 1  Stars 1  Forks 1
For Web Caesar assignment
 caesar.py
def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_string_13(text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]

    return rotated

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]

def rotate_string(text, rot):

    rotated = ''

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated
 