def get_stop_words():
    numbers= ['bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz', 'on', 'milyar',
              'milyon', 'on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan',
              'yüz', 'trilyon']
    months = ['ocak', 'şubat', 'mart', 'nisan', 'mayıs', 'haziran', 'temmuz',
              'ağustos', 'eylül', 'ekim', 'kasım', 'aralık']
    other = ['acaba', 'ama', 'ancak', 'arada', 'artık', 'asla', 'aslında', 'ayrıca', 'az'
             'bazen', 'bazı', 'bazıları', 'belki', 'bilhassa', 'beri', 'birçok', 'birçoğu',
             'biri', 'birisi', 'birkaç', 'birşey', 'bir şey', 'şey', 'böyle', 'böylece',
             'bu', 'buna', 'bunda', 'bundan', 'bunlar', 'bunları', 'bunların', 'bunun',
             'burada', 'bütün', 'çoğu', 'çoğunu', 'çok', 'çünkü', 'da', 'de', 'daha', 'dahi',
             'defa', 'değil', 'diğer', 'diğeri', 'diğeri', 'diğerleri', 'diye', 'dolayısıyla',
             'eden', 'elbette', 'eğer', 'en', 'falan', 'fakat', 'filan', 'gene', 'gereği', 'gibi',
             'göre', 'hala', 'halde', 'halen', 'hangi', 'hani', 'hatta', 'hem', 'henüz', 'hep',
             'hepsi', 'her', 'herkes', 'herkez', 'herhangi', 'her hangi', 'hiç', 'hiçbir', 'hiç biri',
             'hiç bir', 'için', 'içinde', 'ile', 'ilgili', 'işte', 'itibaren', 'itibariyle', 'kaç',
             'kadar', 'karşın', 'kendi', 'kendilerine', 'kendine', 'kendini', 'kendisi', 'kendisine',
             'kendisini', 'kez', 'ki', 'kim', 'kime', 'kimi', 'kimisi', 'kimse', 'madem', 'mi', 'mı',
             'mu', 'mü', 'nasıl', 'ne', 'neden', 'nerde', 'nereye', 'neyse', 'niçin', 'niye',
             'öbür', 'olan', 'olarak', 'oldu', 'olduğu', 'olmadı', 'olsa', 'olsun', 'olduklarını',
             'olmaz', 'olsa', 'olsun', 'ötürü', 'öyle', 'oysa', 'pek', 'rağmen', 'sanki', 'şayet',
             'şekilde', 'şey', 'şeyler,', 'şimdi', 'sonra', 'şöyle', 'şunu', 'tabii', 'tabi', 'tam',
             'tarafından', 'tüm', 'tümü', 've', 'var', 'üzere', 'zaten', 'zira', 'yine']
    adverbs = ['sen', 'ben', 'o', 'biz', 'siz', 'onlar', 'bana', 'beni', 'sana', 'seni', 'sana',
               'o', 'biz', 'bizi', 'bize', 'size', 'bize', 'onlar', 'onları', 'onlardan']
    pointers = ['şu', 'bu', 'şurda', 'burda', 'şurası', 'burası', 'şura', 'bura']
    questions = ['mi', 'mu', 'mü', 'mı']
    conjuctions = ['de', 'da']
    stop_words = numbers + months + pointers + other + adverbs + questions + conjuctions
    return stop_words


def remove_stop_words(words):
    """
        Remove stop words in string.
        Uses NLTK.
    """
    stop_words = get_stop_words()

    words_filtered = []
    for w in words:
        if w not in stop_words:
            words_filtered.append(w)
    return words_filtered