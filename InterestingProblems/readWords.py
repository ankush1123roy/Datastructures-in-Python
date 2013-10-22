def frequency(words_file):
    Words = read_words(words_file)
    dict = {}
    for i in range(len(Words)):
        if Words[i] not in dict:
            dict[Words[i]] = 0
        else:
            dict[Words[i]] = dict[Words[i]] + 1
    print dict, len(dict)

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

if __name__ == '__main__':
    frequency('corpus.txt')
