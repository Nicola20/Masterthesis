#!/usr/bin/env python3

"""
@Authors: Nicola Lea Libera (117073)
@Description: This script generates a password out of letters that was generated using
            the Gutenberg online library.
"""
import argparse
import codecs
import nltk
import nltk.data
import random

nltk.download('punkt')


def read_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length')   # length of the generated password
    args = parser.parse_args()
    return args.length


def load_data():
    f = codecs.open("data/faust.txt", "r", "utf-8")
    data = f.read()
    return data


def prepare_data(data):
    data = data.replace('\n', '').replace('\r', '')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    split_data = tokenizer.tokenize(data)
    number_of_sentences = len(split_data)
    return split_data, number_of_sentences


def generate_password(data, data_length, psw_length):
    start_sentence = random.randint(0, data_length - 1)
    tmp_psw_length = 0
    generated_psw = ""
    used_sentences = []

    while tmp_psw_length <= psw_length:
        generated_psw, used_sentences = password_construction(start_sentence, generated_psw,
                                                              data, psw_length, used_sentences)
        tmp_psw_length = len(generated_psw)
        start_sentence = start_sentence + 1

    return generated_psw, used_sentences


def password_construction(index, password, data, psw_length, used_sentences):
    tmp_sentence = data[index]
    used_sentences.append(tmp_sentence)
    tmp_words = nltk.tokenize.word_tokenize(tmp_sentence)
    for word in tmp_words:
        if len(password) <= psw_length:
            password = password + word[0]
        else:
            break

    return password, used_sentences


def main():
    psw_length = int(read_input())
    text_data = load_data()
    split_data, num_of_sentences = prepare_data(text_data)
    password, sentences = generate_password(split_data, num_of_sentences, psw_length)
    print("This is your generated password with the chosen length of " + str(psw_length) + ": " + password)
    print("Used text phrases: " + str(sentences))
    return 0


if __name__ == "__main__":
    main()
