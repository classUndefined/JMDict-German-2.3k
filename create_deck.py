import json
import re
import codecs


core_deck = "Core2.3k Version 3.txt"

# dictionary with kanji entries
dict_file =  open('new_dict.json')
ger_dict = json.load(dict_file)


# dictionary with kana entries
dict_file_kana =  open('new_dict_kana.json')
ger_dict_kana = json.load(dict_file_kana)


# lines from new raw (txt, tab seperated) deck
deck_content = ""


lines = ''
with open(core_deck, 'r') as f:
    lines = f.readlines()

# regex if not notes txt file. 
#reg_str = "<div style='font-size: 25px;'>(.*?)</div>"

# go through the entire 2.3k deck and create a dictionary (python type)
# copies line of old deck and replaces 'Glossary Field' (from core 2.3k deck type) (3rd field)
# with all German translations found in the kana and kanji dictionary
for line in lines: 

  # get the jp word and the line as a list
  # then get all indices of tabs in the line
  split_list = re.split(r'\t+', line.rstrip('\t+'))
  indices = [i.start() for i in re.finditer('\t', line)]
  jp_word = split_list[0]

  not_found = False

  # search kanji dict
  dict_entry = ger_dict[jp_word]
  translations = []

  # is [] if not found in kanji dict. i.e. if kana word
  if dict_entry == []:
    # not in normal dic -> search in kana dict
    # there's prbably some better way to do this...
    try:
      kana_dict_entry = ger_dict_kana[jp_word]
      # only want the translations i.e. words
      # a single entry for a kana word is every possible meaning
      # for exmaple する can be 磨る、掏る、etc. ...
      for entry in kana_dict_entry:
        for word in entry[5]:
          translations.append(word)
    except:
       not_found = True
  else:
      translations = dict_entry[0][5]

  if not not_found:
    # replace English meaning/translation with found german translations
    split_list[2] = translations

    # insert between the 2nd and 3rd tab since Glossary field is the 3rd field.
    new_line = line[:indices[1] + 1] + ', '.join(map(str,translations)) + line[indices[2]:]
    deck_content += new_line
  else:
    print(f"{jp_word} not found" )




txt_file = open("Core2.3k Version 3 - V1.txt", "w")
txt_file.write(deck_content)
txt_file.close()
 