from googletrans import Translator

translator = Translator()

print('''
-------------------------------------------
HERE IS A LIST OF LANGUAGES WITH THEIR
CORRESPONDING LANGUAGE CODES:
-------------------------------------------
Afrikaans: af
Albanian: sq
Amharic: am
Arabic: ar
Armenian: hy
Azerbaijani: az
Basque: eu
Belarusian: be
Bengali: bn
Bosnian: bs
Bulgarian: bg
Catalan: ca
Cebuano: ceb
Chinese (Simplified): zh-CN
Chinese (Traditional): zh-TW
Corsican: co
Croatian: hr
Czech: cs
Danish: da
Dutch: nl
English: en
Esperanto: eo
Estonian: et
Filipino: tl
Finnish: fi
French: fr
Frisian: fy
Galician: gl
Georgian: ka
German: de
Greek: el
Gujarati: gu
Haitian Creole: ht
Hausa: ha
Hawaiian: haw
Hebrew: iw
Hindi: hi
Hmong: hmn
Hungarian: hu
Icelandic: is
Igbo: ig
Indonesian: id
Irish: ga
Italian: it
Japanese: ja
Javanese: jw
Kannada: kn
Kazakh: kk
Khmer: km
Korean: ko
Kurdish: ku
Kyrgyz: ky
Lao: lo
Latin: la
Latvian: lv
Lithuanian: lt
Luxembourgish: lb
Macedonian: mk
Malagasy: mg
Malay: ms
Malayalam: ml
Maltese: mt
Maori: mi
Marathi: mr
Mongolian: mn
Myanmar (Burmese): my
Nepali: ne
Norwegian: no
Odia (Oriya): or
Pashto: ps
Persian: fa
Polish: pl
Portuguese: pt
Punjabi: pa
Romanian: ro
Russian: ru
Samoan: sm
Scots Gaelic: gd
Serbian: sr
Sesotho: st
Shona: sn
Sindhi: sd
Sinhala: si
Slovak: sk
Slovenian: sl
Somali: so
Spanish: es
Sudanese: su
Swahili: sw
Swedish: sv
Tajik: tg
Tamil: ta
Telugu: te
Thai: th
Turkish: tr
Ukrainian: uk
Urdu: ur
Uzbek: uz
Vietnamese: vi
Welsh: cy
Xhosa: xh
Yiddish: yi
Yoruba: yo
Zulu: zu
-------------------------------------------
''')

languages = ["af", "am", "ar", "az", "be", "bn", "bg", "bs", "ca", "ceb", "cs", "cy", "da", "de", "el", "en", "eo",
             "es", "et", "fa", "fi", "fr", "gd", "gl", "gu", "ha", "haw", "he", "hi", "hmn", "hr", "ht", "hu", "hy",
             "id", "ig", "is", "it", "ja", "jw", "ka", "kk", "km", "kn", "ko", "ku", "ky", "la", "lb", "lo", "lt", "lv",
             "mg", "mi", "mk", "ml", "mn", "mr", "ms", "mt", "my", "ne", "nl", "no", "ny", "pa", "pl", "pt", "ps", "ro",
             "ru", "si", "sk", "sl", "sm", "sn", "so", "sq", "sr", "st", "su", "sw", "ta", "te", "tg", "th", "tl", "tr",
             "uk", "ur", "uz", "vi", "xh", "yi", "yo", "zh-CN", "zh-TW", "zu"]

while True:
    source = input('What language do you want to translate?: ')
    if source not in languages:
        print('Language chosen either does not exist or is unsupported')
    else:
        break
print()
text = input('Text: ')
print()

while True:
    target = input('What language are you translating to?: ')
    if target not in languages:
        print('Language chosen either does not exist or is unsupported')
    else:
        break

translation = translator.translate(text, src=source, dest=target)
print('---------------------')
print(f"\nTranslated Text:\n{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
print('---------------------')


