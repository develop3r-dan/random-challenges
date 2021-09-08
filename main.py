######### PROBLEM 1 ###############
# import csv
# import json
#
#
# with open('A2_fitness.csv', "w") as csv_file:
#     headers = ['title', 'districts', 'districtl','latitude', 'longitude', 'length', 'mincal', 'maxcal']
#     csvwriter = csv.DictWriter(csv_file, fieldnames=headers)
#     csvwriter.writeheader()
#     with open('fitness.json', "r") as fitness_file:
#         data = json.load(fitness_file)
#         not_needed_keys = ['HowToAccess','MapURL','MapURL_tc', 'MapURL_sc']
#         for row in data:
#             for key in not_needed_keys:
#                 row.pop(key)
#             route_split = row['Route'].split(" ")
#             length = route_split[3]
#             calories = route_split[6].split('-')
#             mincal = calories[0]
#             maxcal = calories[1]
#             row['title'] = row.pop('Title')
#             row['districts'] = row.pop('DistrictS')
#             row['districtl'] = row.pop('DistrictL')
#             row['latitude'] = row.pop('Latitude')
#             row['longitude'] = row.pop('Longitude')
#             row['length'] = length
#             row['mincal'] = mincal
#             row['maxcal'] = maxcal
#             row.pop('Route')
#             csvwriter.writerow(row)

######### PROBLEM 1 ###############

######### PROBLEM 2 ###############
# import string
# import re
# import pandas as pd
# not_allowed_punctuation = string.punctuation
#
# with open('stop_words.txt', "r") as stop_words:
#     stop_word_list = []
#     for word in stop_words.readlines():
#         new_word = word.replace("\n", '')
#         stop_word_list.append(new_word)
#
#
# with open('policy.txt', 'rb') as policy_text:
#     headers = dict()
#     text = policy_text.readlines()
#     for line in text:
#         decoded = line.decode('utf-8', errors='replace')
#         decoded = decoded.replace(u'\ufffd', ' ')
#         for letter in not_allowed_punctuation:
#             decoded = decoded.replace(letter, " ")
#         for stop_word in stop_word_list:
#             decoded = re.sub(fr"\b{stop_word}\b"," ", decoded).strip()
#
#         for header_word in decoded.upper().split():
#             if header_word == " " or header_word == '':
#                 pass
#             elif header_word in headers:
#                 pass
#             else:
#                 headers[header_word] = 0
#
#         print(decoded.upper().split())
#         for word in decoded.upper().split():
#             headers[word] += 1
#
#
#     words = []
#     values = []
#     for key, value in headers.items():
#         words.append(key)
#         values.append(value)
#     df_dict = {'word':words, 'frequency':values}
#
#     df = pd.DataFrame(df_dict)
#     df.to_csv('A2_words.csv')

######### PROBLEM 2 ###############


######### PROBLEM 3 ###############

# import requests
# import re
#
# req = requests.get('https://www.imdb.com/chart/top')
# html = req.text
#
# print(html)
#
# pattern = re.compile(r'/title/tt')
#
# pattern_2 = re.compile(r'<strong title="')
# pattern_2_1=re.compile(r'</strong>')
#
# matches = pattern.finditer(html)
# urls =set()
# for match in matches:
#     begin = int(match.span()[0])
#     end = int(match.span()[1])
#     urls.add(html[begin:end+8])
#
# with open('A2_urls.txt', "w") as url_file:
#     url_file.writelines("%s\n" % l for l in urls)
#
# rating_matches = [match.span()[1] for match in list(pattern_2.finditer(html))]
#
# rating_matches_2 = [match.span()[0] for match in list(pattern_2_1.finditer(html))]
#
# index_dict = []
# for index in range(0, len(rating_matches)):
#     index_dict.append([rating_matches[index], rating_matches_2[index]])
#
#
# user_ratings = []
# for value in index_dict:
#     user_ratings.append(html[value[0]:value[1]])

######### PROBLEM 3 ###############

######### PROBLEM 5 ###############
from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent': 'Mozilla/5.0'}

req = requests.get(url="https://www.amazon.com/Best-Sellers-Kindle-Store/zgbs/digital-text", headers=headers)
html = req.text


soup = BeautifulSoup(html, 'html.parser')

big_soup = soup.select('#zg-ordered-list .zg-item-immersion')

results = []

def check_if_has_brackets(name):
    if '(' in name:
        return True
    else:
        return False

print(float(big_soup[0].select('span div .zg-item .a-row .a-link-normal span span')[0].text.replace('$',"")))

for index in range(0,len(big_soup)):
    title = big_soup[index].select('div .p13n-sc-line-clamp-1')[0].text.strip()
    ratings = float(big_soup[index].select('span div span .a-icon-row a i span')[0].text.strip()[0:3])
    try:
        authors = big_soup[index].select('span div .zg-item .a-row .a-size-small')[0].text.strip()
    except IndexError:
        authors = None
    try:
        price = float(float(big_soup[index].select('span div .zg-item .a-row .a-link-normal span span')[0].text.replace('$',"")))
    except IndexError:
        price = None

    if check_if_has_brackets(title):
        index_of_bracket = title.find(' (')
        title = title[0:index_of_bracket]

    book_object = {'rank':index+1,
                    'title':title,
                   'ratings':ratings,
                   'author':authors,
                   'price':price
                   }
    results.append(book_object)

print(results)
with open('A2_books.csv', "w") as csv_file:
    headers = ['rank','title', 'ratings', 'author','price']
    csvwriter = csv.DictWriter(csv_file, fieldnames=headers)
    csvwriter.writeheader()
    for row in results:
        csvwriter.writerow(row)

######### PROBLEM 5 ###############
