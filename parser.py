import re


def clean(line):
    """ Removes punctuation and spaces, lowers words."""
    tmp = line.lower().strip()
    tmp = re.sub('-{1,3}', ' ', tmp)
    tmp = re.sub("[^a-z0-9 ]+", '', tmp)
    return tmp


def parse():
    f = open('example.txt')
    lines = f.readlines()

    sentences = list(map(clean, lines))
    sentences = list(filter(lambda x: x != '', sentences))

    total_chars = list(map(lambda x: len(x), sentences))
    total_chars = sum(total_chars)
    total_sentences = len(sentences)

    data = {
        'sentences': sentences,
        'stats': {
            'total_sentences': total_sentences,
            'total_chars': total_chars,
        },
    }

    return data
