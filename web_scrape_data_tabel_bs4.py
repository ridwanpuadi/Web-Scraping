# mengimport library
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'

# membuat objek page
page = requests.get(url)
page

# mengambil informasi website
soup = BeautifulSoup(page.text, 'lxml')
soup

# mengambil informasi tag table
tabel = soup.find('table', id='main_table_countries_today')
tabel

# mengambil semua nama kolom dengan tag <th>
headers = []
for i in tabel.find_all('th'):
    judul = i.text
    headers.append(judul)
    
headers[13] = 'Tests/1M pop'

# membuat dataframe tabel utama kita
dataku = pd.DataFrame(columns=headers)

# mengisi dataframe dataku
for j in tabel.find_all('tr')[1:]:  # <tr> untuk barisnya
    data_baris = j.find_all('td')   # <td> untuk per kolomnya
    baris = [tr.text for tr in data_baris]
    panjang = len(dataku)           # menghitung sampai di baris ke berapa
    dataku.loc[panjang] = baris
      
# menghilangkan dan merapikan baris
dataku.drop(dataku.index[0:7], inplace=True)
dataku.drop(dataku.index[232:240], inplace=True)

# mereset index agar mulai dari awal / 0
dataku.reset_index(inplace=True, drop=True)

# menghilangkan kolom #
dataku.drop('#', inplace=True, axis=1)

# menyimpan dalam bentuk csv
dataku.to_csv('data_covid.csv', index=False)

# membuka file yang sudah di simpan
buka = pd.read_csv('data_covid.csv')








