from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.goat.com/sneakers'
requests.get(url)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup

postings = soup.find_all('div', class_='GridCellProductInfo__Price-sc-17lfnu8-6 gjSLBu')
postings

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Tentukan jalur ke chromedriver.exe
path_to_chromedriver = 'D:/Scrapping/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# Buat objek Service dengan jalur ke chromedriver.exe
service = Service(path_to_chromedriver)

# Inisialisasi Chrome WebDriver dengan objek Service
driver = webdriver.Chrome(service=service)

# Contoh penggunaan driver
driver.get(url)

# Belajar menggunakan XPath (ekspresi lokasi untuk menuju ke html/xml)
driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div[1]/a/div[1]/div[2]/div/div[1]/span').text
driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div[2]/a/div[1]/div[1]/div[1]').text

soup.find('div', class_='GridCellProductInfo__Name-sc-17lfnu8-3 fXLXkm').string

# Menggunakan full XPath
driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[2]/a/div[1]/div[1]/div[1]').text
# Merubah nomor id
driver.find_element(By.XPATH,'//*[@id="grid-body"]/div/div[1]/div[2]/a/div[1]/div[1]/div[1]').text
driver.find_element(By.XPATH,'//*[@id="grid-body"]/div/div[1]/div[4]/a/div[1]/div[1]/div[1]').text
driver.find_element(By.XPATH,'//*[@id="grid-body"]/div/div[1]/div[10]/a/div[1]/div[1]/div[1]').text

# Scraping dengan for loop
for i in range(1, 21):  # Indeks dimulai dari 1
    try:
        harga = driver.find_element(By.XPATH, f'//*[@id="grid-body"]/div/div[1]/div[{i}]/a/div[1]/div[2]/div/div[1]/span').text
        nama = driver.find_element(By.XPATH, f'//*[@id="grid-body"]/div/div[1]/div[{i}]/a/div[1]/div[1]/div[1]').text
        
        if i == 1:
            print('=' * 15, 'List Produk', '=' * 15)
        
        print(f'{nama} = {harga}')
    
    except NoSuchElementException:
        print(f'Produk ke-{i} tidak ditemukan.')
        continue  # Lanjutkan ke iterasi berikutnya jika elemen tidak ditemukan
    
    
url2 = 'https://www.google.com'
driver.get(url2)

# Belajar memasukkan input dan menggunakan keyboard
from selenium.webdriver.common.keys import Keys    
kotak = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')    
kotak.send_keys('wisata Indonesia')    
kotak.send_keys(Keys.ENTER)    

# Belajar menggunakan klik kiri
kotak = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')    
kotak.send_keys('masyarakat Indonesia')       
kotak.send_keys(Keys.ESCAPE) 
tombol = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
tombol.click()
# ambil gambar
driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div').click()


# Kembali ke Goat.com
driver.get(url)
# cookies
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

# mengambil screenshot
driver.save_screenshot('D:\\Scrapping\\all_product2.png')
# atau
driver.save_screenshot('D:/Scrapping/all_product3.png')

# mengambil satu gambar
driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div[39]/a/div[2]/div/img').screenshot('D:/Scrapping/satu_gambar.png')

# Belajar scrolling halaman
driver.execute_script('return document.body.scrollHeight') # mengukur berapa tinggi halaman
driver.execute_script('window.scrollTo(0,20000)')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight-3000)')

# infinite scrolling
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight-2000)')

# Belajar mengatur jeda waktu
driver.get(url2)
import time

kotak = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')    
kotak.send_keys('wisata Indonesia') 
time.sleep(5)   
kotak.send_keys(Keys.ENTER)   