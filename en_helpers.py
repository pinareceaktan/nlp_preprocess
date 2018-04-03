from nltk.corpus import stopwords


def get_negativity_dict():
    return {'shouldn\'t': 'should not', 'shouldnt': 'should not', 'can\'t': 'can not', 'cant': 'can not',
            'couldn\'t': 'could not',
            'couldnt': 'could not', 'wouldn\'t': 'would not', 'wouldnt': 'would not', 'didn\'t': 'did not',
            'didnt': 'did not', 'haven\'t': 'have not', 'havent': 'have not', 'hasn\'t': 'has not',
            'hasnt': 'has not', 'don\'t': 'do not', 'dont': 'do not', 'doesn\'t': 'does not',
            'doesnt': 'does not', 'shan\'t': 'shall not', 'shant': 'shall not',
            'won\'t': 'will not', 'wont': 'will not', 'mayn\'t': 'may not', 'maynt': 'may not'}


def tag_negatives(tokens):
    """
        Tags not word in presence.
    """
    default_negatives = get_negativity_dict()
    for ind, token in enumerate(tokens):
        if token in default_negatives.keys():
            tokens[ind] = default_negatives[token]
    return tokens


def remove_stop_words(words):
    """
        Remove stop words in string.
        Uses NLTK.
    """
    stop_words = list(stopwords.words('english'))
    stop_words.remove('against')
    # I will not necessarily remove all variants of do not as don't.
    stop_words.remove('not')
    months = ['january', 'february', 'march', 'april',
              'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']
    days = ['monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'sunday', 'mon', 'tue',
            'wed', 'thu', 'fri', 'sat', 'sun']
    stop_words = stop_words + months + days

    words_filtered = []
    for w in words:
        if w not in stop_words:
            words_filtered.append(w)
    return words_filtered