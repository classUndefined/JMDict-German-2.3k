from xml.dom import minidom
from xml.dom.minidom import Node
import xml.etree.ElementTree as ET
import json
import xmltodict


def xml_file_to_json():
  with open("wadoku-xml-20220109/test.xml") as xml_file:
      data_dict = xmltodict.parse(xml_file.read())

  xml_file.close()


  json_data = json.dumps(data_dict,  ensure_ascii=False)

  with open("wadoku-xml-20220109/test_wadoku.json", "w") as json_file:
    json_file.write(json_data)


# recursively get defintions
# not getting defintions half of the time...
def get_values(dictionary):
  defintions = ""
  try:
    if isinstance(dictionary, list):
      for key in dictionary[0].keys():
        defintions += get_values(dictionary[0][key])
    else:
      for key in dictionary.keys():
        defintions += get_values(dictionary[key])
  except:
    # still sometimes not getting defintions
    defintions += str(dictionary) + " "
    #print("no keys " + str(dictionary))
  
  return defintions

def remap_json():
  json_file = open("wadoku-xml-20220109/wadoku.json")
  json_data = json.load(json_file)

  #print(json.dumps(json_data, ensure_ascii=False, indent=2))

  entries = json_data['entries']['entry']
  new_dictionary = []
  for entry in entries:
    #print(json.dumps(entry['form'], ensure_ascii=False, indent=2))
    #print(json.dumps(entry['sense'], ensure_ascii=False, indent=2))

    defintions = ""

    for definitions in entry['sense']:
      defintions += get_values(definitions) + " "

    new_entry = []
    new_entry.append(entry['form']['orth'])  # Kanji/word
    new_entry.append(entry['form']['reading']['hira']) # reading
    new_entry.append("")
    new_entry.append("")
    try:
      new_entry.append(entry['form']['reading']['accent']) # pitch? dunno
    except:
      new_entry.append("")

    #new_entry.append(entry['sense']) # meaning. make this better
    new_entry.append(defintions) # meaning. make this better
    new_entry.append(entry['@id'])
    new_entry.append("")

    # add to new dictionary which is a list
    new_dictionary.append(new_entry)
  new_dictionary = str(new_dictionary)


  with open("wadoku-xml-20220109/new_wadoku.json", "w") as file:
    file.write(new_dictionary)







remap_json()




# parse an xml file by name

# create element tree object
#tree = ET.parse("wadoku-xml-20220109/test.xml")

# get root element
#root = tree.getroot()

# create empty list for news items


""" 

def get_content(node, dict_arg, word):

  dict = dict_arg
  
  tag = node.tag.split("}",1)[1]

  result = str(node.tag) + " " + str(node.text)
  child_dict = {}

  for child in node:
    child_dict = {}
    text, child_dict, word = get_content(child, child_dict, word)
    result += "\n" + text
    c_tag = child.tag.split("}",1)[1]

    if child.text != None:
      child_dict[c_tag] = [child.text]
      
    #print(child.text)
    if child_dict != {}:
      if c_tag in child_dict:
        # SOMETHING HERE DOENST WORK
        # WHY DOES IT NOT APPEND THE DEFINTIONS IF
        # TAG IS token OR text ETC??
        if c_tag in dict:
          dict[c_tag].append(child_dict[c_tag])
        else:
          dict[c_tag] = child_dict[c_tag]
      else:
        dict[c_tag] = child_dict

  if node.tag == "orth":
    word = node.text

  return result, dict, word


dict_json = ''

# iterate news items
for item in root.findall('.'):

  # empty news dictionary
  news = {}

  # iterate child elements of item
  for entries in item:

    dict_entry = {}
    print("\n---new entry---")
    word = ""
    text, dict_entry, word = get_content(entries, dict_entry, word)
    dict_json += json.dumps(dict_entry, indent=2, ensure_ascii=False)

    print(word) 
#print(dict_json)


with open('wadoku_v1.json', 'w', encoding='utf-8') as f:
    # this would place the entire output on one line
    # use json.dump(lista_items, f, indent=4) to "pretty-print" with four spaces per indent
    json.dump(dict_json, f, ensure_ascii=False)


 """