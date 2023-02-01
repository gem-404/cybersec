
"""
A program that decrypts a message encoded in the
caesars cypher.
"""

ENCRYPTED_MSG1 = """
vjg ugetgvu hqt dgkpi iqqf cv etarvqitcrja ku vq rtcvkeg cp kpetgfkdng
coqwpv qh jqwtu"""

ENCRYPTED_MSG2 = """vtblqj ghfubswlqj brxu rzq fbskhuwhaw zlwk udqgrp
qxpehuv dv nhbv. brx frxog xvh udqgrp nhb"""

ENCRYPTED_MSG3 = """bzizmvodji vgbjmdochn. oj wz xjindyzmzy vn v hvnozm,
v ojovg ja 10000 cjpmn dn mzlpdmzy.
"""


def str_decoder(word: str, char_num: int) -> str:
    """Takes a single word and decodes the word.
    Since the encoded words are most similar to
    what a caesar encryption would look like,
    the decryption will assume caesar encryption
    was used.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    char_len: int = len(alphabet)
    # max number that can be efficiently used in encryption

    new_word = ""

    if char_num > char_len:
        char_num %= char_len

    for char in word:
        if char in alphabet:  # only letters should be decoded.
            position = alphabet.index(char)
            new_position = position-char_num

            new_word += alphabet[new_position]
        else:
            new_word += char

    return new_word


def read_string(words: str, num: int) -> str:
    """Reads the whole string and decodes the
    string word by word. The decrypted words are then
    stored in a list which is then concatenated
    to a string again.
    """

    return "".join(str_decoder(word, num) for word in words)


def main():
    """Testing the functionality of the above functions."""

    msg1 = read_string(ENCRYPTED_MSG1, 28)
    msg2 = read_string(ENCRYPTED_MSG2, 3)
    msg3 = read_string(ENCRYPTED_MSG3, 99)

    print(f"{msg1} {msg2} {msg3}")


if __name__ == '__main__':
    main()
