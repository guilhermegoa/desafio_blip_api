from fastapi import HTTPException
from nltk import word_tokenize, pos_tag
from nltk.corpus import words as words_nltk



async def word_validation(sentence: str):
    if is_valid_word(sentence):
        raise HTTPException(status_code=400, detail="Invalid word")
    

def is_valid_word(sentence: str):
    words = word_tokenize(sentence)
    word_list = set(words_nltk.words())

    for word in words:
        if word.lower() not in word_list:
            return True
    
    return False


def is_valid_word_tag(sentence: str):
    words = word_tokenize(sentence)
    pos_tags = pos_tag(words)

    print(pos_tags)

    valid_pos_tags = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    for _, tag in pos_tags:
        if tag in valid_pos_tags:
            return False
    
    return True