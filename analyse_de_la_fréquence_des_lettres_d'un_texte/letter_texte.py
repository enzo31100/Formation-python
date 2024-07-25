from typing import List, Tuple, Any

from unidecode import unidecode

def input_sentence():
    saisie: str = input("Entrez un élément : ")
    return saisie


def normalize_sentence(saisie):
    return unidecode(saisie).lower()



def calc_letters_freq_sentence(saisie,num=20):
    res = dict()
    li = saisie.split('-')
    for k, v in enumerate(saisie[:num]):
        li = list(range(len(saisie)))
    print(li)


if __name__ == '__main__':
    sentence = input_sentence()
    sentence = normalize_sentence(sentence)
    frequency_letters = calc_letters_freq_sentence(sentence)
