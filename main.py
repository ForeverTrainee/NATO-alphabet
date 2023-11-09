import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def generate_phonetic():
    word = input("Provide a name: ").upper()
    try:
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please provide only alphabet letters")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()




