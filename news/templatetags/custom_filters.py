from django import template

register = template.Library()

BAD_WORDS = [
    'shit!',
    'crap!',
    'bullshit!'
]

@register.filter()
def censor_text(text):
    text1 = text.lower() #весь текст в нижний регистр
    text2 = text1.split() #список
    for word in text2:
        if word in BAD_WORDS:
            censor_word = f'{word[0]+"*"*(len(word)-1)}'
            text2 = " ".join(text2)
            text = (text2.replace(word, censor_word)).capitalize()

    return text
