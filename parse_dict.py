import json
import re
import codecs


dict_file =  open('ger_dict.json','r')
ger_dict = {}
ger_dict = json.loads(dict_file.read())

lines = ''
with open('Core2.3k Version 3._notestxt.txt', 'r') as f:
    lines = f.readlines()
new_dict = {}


for line in lines:
  found = False
  found_entries = []

  split_list = re.split(r'\t+', line.rstrip('\t+'))
  indices = [i.start() for i in re.finditer('\t', line)]
  jp_word = split_list[0]

  for entry in ger_dict:
   # print(entry[1])
    if str(jp_word) == str(entry[1]):
      found = True
      found_entries.append(entry)
    
    if found and jp_word is not entry[0]:

      try:
        new_dict[jp_word] = found_entries
      except:
        print(found_entries)
  


with open('new_dict_kana.json', 'w', encoding='utf-8') as f:
    # this would place the entire output on one line
    # use json.dump(lista_items, f, indent=4) to "pretty-print" with four spaces per indent
    json.dump(new_dict, f, ensure_ascii=False)