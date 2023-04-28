import pandas

phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_df.iterrows()}


def create_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        phonetic_code_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        create_phonetic()
    else:
        print(phonetic_code_list)


create_phonetic()
