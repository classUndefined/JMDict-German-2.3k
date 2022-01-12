import json
import re
import codecs

# json dict to load data from
dict_file =  open('ger_dict.json','r')
ger_dict = {}
ger_dict = json.loads(dict_file.read())

# use this as reference to create the new dictionary from
lines = ''
with open('Core2.3k Version 3.txt', 'r') as f:
    lines = f.readlines()
new_dict = {}


# go through the entire dictionary, take the word and the translation 
# and create a dictionary (python dict type) 
for line in lines:
  found = False
  found_entries = []

  split_list = re.split(r'\t+', line.rstrip('\t+'))
  indices = [i.start() for i in re.finditer('\t', line)]
  jp_word = split_list[0]

  for entry in ger_dict:
    # entry[1] for kana, entry[0] for creating a kanji
    if str(jp_word) == str(entry[1]):
      found = True
      found_entries.append(entry)
    
    if found and jp_word is not entry[0]:

      try:
        new_dict[jp_word] = found_entries
      except:
        print(found_entries)
  

# adjust this to create new dictionary
with open('new_dict_kana.json', 'w', encoding='utf-8') as f:
    # this would place the entire output on one line
    # use json.dump(lista_items, f, indent=4) to "pretty-print" with four spaces per indent
    json.dump(new_dict, f, ensure_ascii=False)