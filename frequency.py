# russian (high), polish (moderately high), latvian (average), norwegian (moderetaly low), english (low)

# russian
alphabet_rus = 'ёйцукенгшщзхъфывапролджэячсмить'
list_vowels_rus = 'ёуеыаэяию'
list_consonants_rus = 'йцкнгшщзхъфвпрлджэчсмтьб'
vowels_rus, consonants_rus = 0, 0
russian = open('russian.txt')
draft_rus = ''
text_rus = ''
for s in russian:
     draft_rus += s
russian.close()
for symbol in draft_rus:
    if symbol.lower() in alphabet_rus and len(text_rus) < 300000:
        text_rus += symbol
for letter in text_rus:
    if letter in list_vowels_rus:
        vowels_rus += 1
    else:
        consonants_rus += 1
print(consonants_rus / vowels_rus)

# polish
alphabet_pol = 'AaĄąEeĘęIiOoÓóUuYyBbCcĆćDdFfGgHhJjKkLlŁłMmNnŃńPpQqRrSsŚśTtVvWwXxZzŹźŻż'
list_vowels_pol = 'AaĄąEeĘęIiOoÓóUuYy'
list_consonants_pol = 'BbCcĆćDdFfGgHhJjKkLlŁłMmNnŃńPpQqRrSsŚśTtVvWwXxZzŹźŻż'
vowels_pol, consonants_pol = 0, 0
polish = open('polish.txt')
draft_pol = ''
text_pol = ''
for s in polish:
     draft_pol += s
polish.close()
for symbol in draft_pol:
    if symbol in alphabet_pol and len(text_pol) < 300000:
        text_pol += symbol
for letter in text_pol:
    if letter in list_vowels_pol:
        vowels_pol += 1
    else:
        consonants_pol += 1
print(consonants_pol / vowels_pol)

# latvian
alphabet_latv = 'AaĀāEeĒēIiĪīOoUuŪūBbCcČčDdFfGgĢģHhJjKkĶķLlĻļMmNnŅņPpRrSsŠšTtVvZzŽž'
list_vowels_latv = 'AaĀāEeĒēIiĪīOoUuŪū'
list_consonants_latv = 'BbCcČčDdFfGgĢģHhJjKkĶķLlĻļMmNnŅņPpRrSsŠšTtVvZzŽž'
vowels_latv, consonants_latv = 0, 0
latvian = open('latvian.txt')
draft_latv = ''
text_latv = ''
for s in latvian:
     draft_latv += s
latvian.close()
for symbol in draft_latv:
    if symbol in alphabet_latv and len(text_latv) < 300000:
        text_latv += symbol
for letter in text_latv:
    if letter in list_vowels_latv:
        vowels_latv += 1
    else:
        consonants_latv += 1
print(consonants_latv / vowels_latv)

# norwegian
alphabet_norw = 'AaEeIiOoUuYyÆæØøÅåBbCcDdFfGgHhJjKkLlMmNnPpRrSsTtVvWwXxZz'
list_vowels_norw = 'AaEeIiOoUuYyÆæØøÅå'
list_consonants_norw = 'BbCcDdFfGgHhJjKkLlMmNnPpRrSsTtVvWwXxZz'
vowels_norw, consonants_norw = 0, 0
norwegian = open('norwegian.txt')
draft_norw = ''
text_norw = ''
for s in norwegian:
     draft_norw += s
norwegian.close()
for symbol in draft_norw:
    if symbol in alphabet_norw and len(text_norw) < 300000:
        text_norw += symbol
for letter in text_norw:
    if letter in list_vowels_norw:
        vowels_norw += 1
    else:
        consonants_norw += 1
print(consonants_norw / vowels_norw)

# english
alphabet_eng = 'AaEeIiOoUuYyBbCcDdFfGgHhJjKkLlMmNnPpRrSsTtVvWwXxZz'
list_vowels_eng = 'AaEeIiOoUuYy'
list_consonants_eng = 'BbCcDdFfGgHhJjKkLlMmNnPpRrSsTtVvWwXxZz'
vowels_eng, consonants_eng = 0, 0
english = open('english.txt')
draft_eng = ''
text_eng = ''
for s in english:
     draft_eng += s
english.close()
for symbol in draft_eng:
    if symbol in alphabet_eng and len(text_eng) < 300000:
        text_eng += symbol
for letter in text_eng:
    if letter in list_vowels_eng:
        vowels_eng += 1
    else:
        consonants_eng += 1
print(consonants_eng / vowels_eng)