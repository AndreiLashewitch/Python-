from random import randrange

def get_jokes ():
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    random_idx0 = randrange(len(nouns))
    random_idx1 = randrange(len(adverbs))
    random_idx2 = randrange(len(adjectives))

    bonus0 = nouns[random_idx0]
    bonus1 = adverbs[random_idx1]
    bonus2 = adjectives[random_idx2]
    return f"{bonus0} {bonus1} {bonus2}"
print(get_jokes())





