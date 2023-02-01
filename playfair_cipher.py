"""
A program that reads a plaintext and a key
and encrypts the plaintext using the
playfair cipher.

"""


def conv_text_to_diagraphs(plain_text: str) -> str:
    """Fills an X whenever two letters are
    repeated and creates a diagraph for
    the plain_text given.

    """

    # append X if two letters are being repeated

    for i in range(0, len(plain_text)+1, 2):

        if i < len(plain_text)-1:

            if plain_text[i] == plain_text[i+1]:
                plain_text = plain_text[:i+1]+'X'+plain_text[i+1:]

    # append X if the total letters are odd, to make plain_text even

    if len(plain_text) % 2 != 0:
        plain_text = plain_text[:]+'X'

    return plain_text


def gen_matrix(key: str) -> list[list[int]]:
    """
     generates a key array with the key from user
     with following below conditions:
     -> A character should not be repeated
     -> Replacing J with I (as per the rule of the playfair cipher)

    """
    mat: list[list[int]] = [[0 for _ in range(5)] for _ in range(5)]
    key_arr: list = []

    for char in key:
        if char not in key_arr:
            if char == 'J':
                key_arr.append('I')
            else:
                key_arr.append(char)

    # filling the remaining key array with rest of unused
    # letters from the English alphabet.

    is_i_exist: bool = "I" in key_arr

    # A-Z's ASCII Value lies between 65 to 90 but as range's
    # second parameter excludes that value we will use 65 to 91

    for i in range(65, 91):
        if chr(i) not in key_arr:
            # I = 73
            # J = 74
            # We want I in key_arr not J

            if i == 73 and not is_i_exist:

                key_arr.append("I")
                is_i_exist = True

            elif i == 73 or i == 74 and is_i_exist:
                pass

            else:
                key_arr.append(chr(i))

    index: int = 0

    for i in range(0, 5):
        for j in range(0, 5):

            mat[i][j] = key_arr[index]
            index += 1

    return mat


def index_locator(char: str, cipherkey_matrix: list) -> list[int]:
    """
    returns the index of the character in the cipherkey_matrix.

    """
    char_index = []

    # convert the character value from J to I
    if char == "J":
        char = "I"

    for i, j in enumerate(cipherkey_matrix):

        for key, value in enumerate(j):
            if char == value:

                char_index.append(i)
                # add 1st dimension of 5X5 matrix => i.e., char_index = [i]

                char_index.append(key)
                # add 2nd dimension of 5X5 matrix => i.e., char_index = [i,k]

            # Now with the help of char_index = [i,k]
            # we can pretty much locate every element,
            # inside our 5X5 matrix like this =>  cipherkey_matrix[i][k]

    return char_index


def encryption(plain_text: str, key: str) -> list[str]:
    """
    Encrypts the plain_text using the key
    and returns the cipher_text.
    """
    cipher_text: list = []

    # generate key matrix
    key_matrix: list[list[int]] = gen_matrix(key)

    integer: int = 0

    # encrypt according to rules of playfair cipher

    while integer < len(plain_text):
        # calculate two grouped characters indexes from key_matrix

        first_value = index_locator(plain_text[integer], key_matrix)
        second_value = index_locator(plain_text[integer+1], key_matrix)

        # if same column then look in below row so
        # format is [row,col]
        # now to see below row => increase the row in both item
        # (first_value[0]+1,first_value[1]) => (3+1,1) => (4,1)

        # (second_value[0]+1,second_value[1]) => (4+1,1) => (5,1)

        # but in our matrix we have 0 to 4 indexes only
        # so to make value bound under 0 to 4 we will do %5
        #
        #   (first_value[0]+1 % 5,first_value[1])
        #   (second_value[0]+1 % 5,second_value[1])

        if first_value[1] == second_value[1]:
            int_one = (first_value[0] + 1) % 5
            value_one = first_value[1]

            int_two = (second_value[0] + 1) % 5
            value_two = second_value[1]
            cipher_text.append(key_matrix[int_one][value_one])
            cipher_text.append(key_matrix[int_two][value_two])
            # cipher_text.append(", ")

        # same row
        elif first_value[0] == second_value[0]:
            int_one = first_value[0]
            value_one = (first_value[1] + 1) % 5

            int_two = second_value[0]
            value_two = (second_value[1] + 1) % 5
            cipher_text.append(key_matrix[int_one][value_one])
            cipher_text.append(key_matrix[int_two][value_two])
            # cipher_text.append(", ")

        # if making rectangle then
        # [4,3] [1,2] => [4,2] [3,1]
        # exchange columns of both value
        else:
            int_one = first_value[0]
            value_one = first_value[1]

            int_two = second_value[0]
            value_two = second_value[1]

            cipher_text.append(key_matrix[int_one][value_two])
            cipher_text.append(key_matrix[int_two][value_one])
            # cipher_text.append(", ")

        integer += 2

    return cipher_text


def main() -> None:
    """Main function"""

    while True:
        # will keep on getting user inputs until a user
        # fails to fill in a key or a text

        # -> A key to make the 5x5 char matrix
        key: str = input("Enter key: ").replace(" ", "").upper()
        if key == "":
            break

        # -> A plain text message that is to be encrypted
        plain_text: str = input("Plain Text: ").replace(" ", "").upper()
        if plain_text == "":
            break

        converted_plain_text: str = conv_text_to_diagraphs(plain_text)

        ciphertext: str = "".join(encryption(converted_plain_text, key))

        print(ciphertext)


if __name__ == "__main__":
    main()
