import base_helpers
import en_helpers
import tr_helpers

""" Preprocess function supported for EN and TR,
    Language is not necessary, function still works.
    But there wont be any language specific pre-process.    
"""


def main():
    input_text = ['say something', 'bu da ikinci text']
    output_str = []
    for text in input_text:
        text = base_helpers.tweet_preprocessor(text)
        lang = base_helpers.find_language(text)

        # Tag emoticons
        str1 = base_helpers.tag_emoticons(text)
        # Remove digits in text
        str2 = base_helpers.remove_digits(str1)
        # Make all words lower
        str3 = base_helpers.make_all_lower(str2)
        # Tokenize
        list1 = base_helpers.get_words(str3)

        if lang == 'tr':
            final_list = tr_helpers.remove_stop_words(list1)
        elif lang == 'en':
            list2 = en_helpers.tag_negatives(list1)
            final_list = en_helpers.remove_stop_words(list2)
        else:
            final_list = [base_helpers.tag_emoticons(text)]

        list3 = base_helpers.remove_punctuations(final_list)
        list4 = base_helpers.remove_single_lettereds(list3)

        if len(list4) != 0:
            output_str.append(list4)
        else:
            output_str.append([''])


if __name__ == '__main__':
    main()