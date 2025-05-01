def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return 'un' + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]

    return f' :: {prefix}'.join(vocab_words)


def remove_suffix_ness(word):

    no_sufix = word.replace('ness', '')

    if no_sufix[-1] == 'i':
        no_sufix = no_sufix.replace('i', 'y')

    return no_sufix

def adjective_to_verb(sentence, index):

    list_words = sentence.split()
    adjective = list_words[index]
    if adjective.endswith('.'):
        adjective = list_words[index].replace('.', 'en')
        return adjective
    return adjective + 'en'

print(adjective_to_verb("His expression went dark.", -1))