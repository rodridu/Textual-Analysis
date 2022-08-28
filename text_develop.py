
class text_develop:
    def text_del(text):
        """
        text:  string
        :return:
        """
        import string
        import re
        from nltk.corpus import stopwords
        import nltk


        # 小写
        text = text.lower()

        # 停用词
        punctuation_string = string.punctuation
        for i in punctuation_string:
            text = text.replace('\\', ' ')
            text = text.replace(i, '')

        BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
        STOPWORDS = set(stopwords.words('english'))

        text = BAD_SYMBOLS_RE.sub('', text)
        text = ' '.join(word for word in text.split() if word not in STOPWORDS)
        text = ''.join([i for i in text if not i.isdigit()])


        return text


# %%
aaa = '1  ,  4531,  a , taken, she, loves, A'
print(text_develop.text_del(aaa))

