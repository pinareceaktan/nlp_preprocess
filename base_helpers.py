from googletrans import Translator
import re


def get_emoticons():
    """
    @Todo: Extend the list sometime.
    :return: emoticons
    """
    emoticons = {
        ':)': 'HAPPYFACE',
        ':]': 'HAPPYFACE',
        '.)': 'HAPPYFACE',
        '=)': 'HAPPYFACE',
        '(:': 'HAPPYFACE',
        ':‑)': 'HAPPYFACE',
        ':D': 'LAUGHINGFACE',
        '=D': 'LAUGHINGFACE',
        ':d': 'LAUGHINGFACE',
        '=d': 'LAUGHINGFACE',
        '.d': 'LAUGHINGFACE',
        ':-D': 'LAUGHINGFACE',
        ':(': 'UNHAPPYFACE',
        '=(': 'UNHAPPYFACE',
        ':[': 'UNHAPPYFACE',
        '.(': 'UNHAPPYFACE',
        '):': 'UNHAPPYFACE',
        ':-(': 'UNHAPPYFACE',
        ':\'(': 'CRYINGFACE',
        '=\'(': 'CRYINGFACE',
        ':\'[': 'CRYINGFACE',
        ':\'-(': 'CRYINGFACE',
        ':@': 'ANGRYFACE',
        '=@': 'ANGRYFACE',
        ':O': 'SHOCKEDFACE',
        ':o': 'SHOCKEDFACE',
        'o.o': 'SHOCKEDFACE',
        'O.o': 'SHOCKEDFACE',
        'o_O': 'SHOCKEDFACE',
        'O_o': 'SHOCKEDFACE',
        ':s': 'EMBRASEDFACE',
        ':S': 'EMBRASEDFACE',
        ' :$': 'EMBRASEDFACE',
        '=$': 'EMBRASEDFACE',
        ':/': 'CONFUSEDFACE',
        ':- *': 'KISSINGFACE',
        ': *': 'KISSINGFACE',
        ':×': 'KISSINGFACE',
        '#‑)': 'DRUNKFACE'
    }
    return emoticons


def tag_emoticons(any_string):
    """
        Tag emoticons in string.
        :param any_string: any string.
        :returns tagged strings.
    """
    search_list = get_emoticons().keys()
    emo_dict = get_emoticons()

    for emo in search_list:
        pattern = "(" + emo.replace("(", "\\(").replace(")", "\\)") \
            .replace("|", "\\|").replace("[", "\\[").replace("]", "\\]") + ")"
        m = re.findall(pattern, any_string)
        if emo in m:
            any_string = any_string.replace(emo, " "+ emo_dict[emo]+ " ")
    return any_string


def query_text(any_string):
    """
        Do not use pipe, search for each character in a text one by one.
        lil bit dummy but rgx pipe is much dummier.
        @Todo: Make this replace stuff a separate function
    """
    search_list = get_emoticons().keys()
    emo_dict = get_emoticons()
    emoticons_in_txt = []
    for emo in search_list:
        pattern = "(" + emo.replace("(", "\\(").replace(")", "\\)")\
            .replace("|", "\\|").replace("[", "\\[").replace("]", "\\]") + ")"
        m = re.findall(pattern, any_string)
        if emo in m:
            emoticons_in_txt.append(emo_dict[emo])
    return emoticons_in_txt


def is_include_emoticon(any_string):
    """
    Check emoticon presence
    :param any_string:
    :return: True or False
    """
    emoticons_in_string = query_text(any_string)
    if len(emoticons_in_string) > 0:
        return True
    else:
        return False


def find_language(any_string):
    """
    Check language of text.
    Uses googletrans's detector
    :param any_string:
    :param language:
    :return:
    """
    # Check if tweet has only one emoticon but nothing else,
    # if presence tag the emoticon.
    if is_include_emoticon(any_string):
        if tag_emoticons(any_string) in get_emoticons().values():
            any_string = tag_emoticons(any_string)

    translator = Translator()
    detected_language = translator.detect(any_string)

    return detected_language.lang


def is_that_empty(any_string):
    """
        It tags the emoticons in presence than it
        checks if the string or list of strings is empty
        :param any_string: String or list of strings

    """
    array = re.findall(r"[\w']+", any_string)
    emoticons = is_include_emoticon(any_string)
    if len(array) > 0:
        return False
    else:
        if emoticons:
            return False
        else:
            return True


def clean_tweet(tweet, process):
    """
        Remove urls, hash-tags, rt, at, mentions
        :param tweet in list
        :return cleaned tweets in list
    """
    result = []
    pattern = {
        'hash-tag': '(?:\#+[\w_]+[\w\'_\-]*[\w_]+)',
        'mention': '(?:\@+[\w_]+[\w\'_\-]*[\w_]+)',
        'url':  '(https?:\/\/(?:www\.|http:|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+'
                '[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.'
                '[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})',
        'rt': '^RT :',
        'at': '(?:^|\W)at'
    }
    cleaned_tweet = ' '.join(re.sub(pattern[process], " ", tweet[0]).split())

    if is_that_empty(cleaned_tweet):
        result.append('')
    else:
        result.append(cleaned_tweet)
    return result


def has_digit(any_string):
    """
        Checks if the string has digit
        :param any_string: any string
        :return: True or False
    """
    if any(re.findall(r"[\d]+", any_string)):
        return True
    else:
        return False


def remove_digits(any_string):
    """
        If the word includes digits, remove them from text.
        :param any_string: the word to check in string.
        :return: List of refined words.
    """
    chars = list(any_string)
    ind = 0
    while ind < len(chars):
        if has_digit(chars[ind]):
            chars.remove(chars[ind])
        else:
            ind = ind + 1
    return ''.join(chars)


def make_all_lower(sentence):
    return sentence.lower()


def is_including(any_string, punctuation):
    """
        Checks if any any_string includes punctuation.
        :param any_string: String to check.
        :param punctuation: Punc. to search for.
        :return: True, False.
    """
    if punctuation in any_string:
        return True
    else:
        return False


def get_words(any_string):
    """
        Get the words.
        :param any_string:
        :return: Words of strings.
    """
    #   Check for the apostrophe and remove it
    if not is_including(any_string, '\''):
        return re.findall(r"[\w']+", any_string)
    else:
        return get_words(''.join(any_string.split("'")))


def remove_punctuations(any_string):
    """
        Removes punctuation in string
    """
    if not isinstance(any_string, str):
        any_string = ' '.join(any_string)
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''

    # remove punctuation from the string
    no_punct = ""
    for char in any_string:
        if char not in punctuations:
            no_punct += char
        else:
            no_punct += " "
    return get_words(no_punct)


def remove_single_lettereds(words):
    """
        If the word includes short words, remove them.
        :param words: The list of words to check.
        :return: List of refined words.
    """
    ind = 0
    while ind < len(words):
        if len(words[ind]) < 2:
            words.remove(words[ind])
        else:
            ind = ind + 1
    return words


def tweet_preprocessor(text):
    """
    Removes hash-tags, mentions, urls, rts and ats
    :param string_arr:
    :return:
    """
    # Remove hash-tags
    no_hash_tag = clean_tweet([text], 'hash-tag')
    # Remove mention
    no_mention = clean_tweet(no_hash_tag, 'mention')
    # Remove URLs
    no_url = clean_tweet(no_mention, 'url')
    # Remove rt
    no_rt = clean_tweet(no_url, 'rt')
    # Remove at
    no_at = clean_tweet(no_rt, 'at')
    return no_at[0]


