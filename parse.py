import json
import re
import codecs

"""
file = "Core2.3k Version 3.txt"
dict_file =  open('ger_dict.json','r')
ger_dict = {}
ger_dict = json.loads(dict_file.read())
"""
file = "Core2.3k Version 3._notestxt.txt"
dict_file =  open('new_dict.json')
ger_dict = json.load(dict_file)

dict_file_kana =  open('new_dict_kana.json')
ger_dict_kana = json.load(dict_file_kana)

deck_content = ""


lines = ''
with open(file, 'r') as f:
    lines = f.readlines()

# regex if not notes txt file. NOT NEEDED
#reg_str = "<div style='font-size: 25px;'>(.*?)</div>"

new_dict = {}

for line in lines: 

  split_list = re.split(r'\t+', line.rstrip('\t+'))
  indices = [i.start() for i in re.finditer('\t', line)]
  jp_word = split_list[0]

  not_found = False

  # list of lists
  dict_entry = ger_dict[jp_word]
  translations = []


  if dict_entry == []:
    # not in normal dic -> search in kana dict
    # there's prbably some better way to do this...
    try:
      kana_dict_entry = ger_dict_kana[jp_word]
      # only want the translations i.e. words
      for entry in kana_dict_entry:
        for word in entry[5]:
          translations.append(word)
    except:
       not_found = True
  else:
      translations = dict_entry[0][5]

  if not not_found:
    insert_string = translations
    split_list[2] = insert_string

    new_line = line[:indices[1] + 1] + ', '.join(map(str,translations)) + line[indices[2]:]
    deck_content += new_line
  else:
    print(f"{jp_word} not found" )




txt_file = open("Core2.3k Version 3 - V1.txt", "w")
txt_file.write(deck_content)
txt_file.close()
 