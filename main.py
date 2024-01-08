from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import os

# Aplikasi Update SK PPNPN Otomatis
# By Husni

FILE_NAME = 'ppnpn_test.csv'

def install_webdriver():
    service = Chromeservice(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.quit()

def update_sk(username, password):
    browser_options = webdriver.ChromeOptions()
    browser_options.add_experimental_option('detach', True)
    
    try:
        with open(FILE_NAME, 'r') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=';')
            next(csv_data)
            
            for datas in csv_data:
                driver = webdriver.Chrome(options=browser_options)
                driver.get(os.getenv('URL'))
                time.sleep(4)
                
                # input username
                input_user = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div/form[1]/div[2]/input[5]')
                for i in range(len(username)):
                    input_user.send_keys(username[i])
                time.sleep(0.7)
                
                # input password
                input_pass = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div/form[1]/div[3]/div[1]/input')
                for i in range(len(password)):
                    input_pass.send_keys(password[i])
                time.sleep(0.7)
                
                # button login
                btn_login = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div/form[1]/div[4]/button')
                btn_login.click()
                time.sleep(10)
                
                # menu input data
                menu_input = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[2]/ul/li[2]/a/span')
                menu_input.click()
                time.sleep(0.7)
                
                # Menu RUH
                menu_ruh = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[2]/ul/li[2]/div/div[3]/ul[1]/li[1]/a')
                menu_ruh.click()
                time.sleep(0.7)
                
                # search NIK
                nik_data = datas[0]
                search_nik = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[1]/div/div/div/div[2]/div[1]/div[1]/div/input')
                search_nik.send_keys(nik_data)
                print('Menginput NIK : '+nik_data)
                time.sleep(2)
                
                # button detail
                btn_detail = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[1]/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/button')
                btn_detail.click()
                time.sleep(0.7)
                
                # button kontrak
                btn_kontrak = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[1]/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/div/a[1]')
                btn_kontrak.click()
                time.sleep(1.5)
                
                # button rekam
                btn_rekam = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[4]/div/div/div/div[3]/div/div/button[1]')
                btn_rekam.click()
                time.sleep(0.7)
                
                # input no. sk
                input_no_sk = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[5]/div/div/div/div/div/div[3]/div/input')
                input_no_sk.send_keys('Nomor 800')
                time.sleep(0.7)
                
                # clear tgl & input tgl sk
                input_tgl_sk = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[5]/div/div/div/div/div/div[4]/div/div/input')
                input_tgl_sk.clear()
                time.sleep(0.5)
                input_tgl_sk.send_keys('2023-11-28')
                time.sleep(0.7)
                
                # input keterangan
                input_ket = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[5]/div/div/div/div/div/div[5]/div/textarea')
                input_ket.send_keys('Pengangkatan Kembali PPNPN (Perpanjangan SK PPNPN Sampai 31 Desember)')
                time.sleep(0.7)
                
                # clear tgl mulai & input tanggal mulai
                input_tgl_mulai = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[5]/div/div/div/div/div/div[6]/div/div/input')
                input_tgl_mulai.clear()
                time.sleep(0.5)
                input_tgl_mulai.send_keys('2023-11-28')
                time.sleep(0.7)
                
                # clear tgl selesai & input tanggal selesai
                input_tgl_selesai = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[5]/div/div/div/div/div/div[7]/div/div/input')
                input_tgl_selesai.clear()
                time.sleep(0.5)
                input_tgl_selesai.send_keys('2023-12-31')
                time.sleep(0.7)
                
                # input penghasilan
                penghasilan_data = datas[1]
                input_penghasilan = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[5]/div/div/div/div/div/div[8]/div/input')
                input_penghasilan.clear()
                time.sleep(0.5)
                input_penghasilan.send_keys(penghasilan_data)
                time.sleep(0.7)
                
                # input default
                input_default = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[5]/div/div/div/div/div/div[10]/div/input')
                input_default.send_keys('1')
                time.sleep(0.7)
                
                # button simpan
                btn_simpan = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[5]/div/div/div/div/div/div[11]/button')
                btn_simpan.click()
                print('Berhasil Simpan NIK : '+nik_data)
                time.sleep(2)
                
                # button tutup
                btn_tutup = driver.find_element(By.XPATH, '/html/body/app-root/main/app-menusatker/div[1]/div[1]/div[3]/div[2]/div[2]/app-datappnpn/div[4]/div/div/div/div[3]/div/div/button[2]')
                btn_tutup.click()
                time.sleep(3)
                driver.quit()
            print('SELESAI UPDATE SK....')
            time.sleep(20)
    except:
        print('Error Input SK Perpanjangan : '+nik_data)

def main():
    print(' MENU '.center(50,'='))
    print('1. Update SK Dengan User Default')
    print('2. Update SK Dengan User Baru')
    print(' MENU '.center(50,'='))
    menu_main = input('Pilih Menu [1/2/3] : ')
    if menu_main == '1':
        update_sk(os.getenv('MY_USERNAME'), os.getenv('MY_PASSWORD'))

    elif menu_main == '2':
        new_user = input('Username : ')
        new_pass = input('Password : ')
        update_sk(new_user,new_pass)

    elif menu_main == '3':
        return menu_main

    else:
        print('menu nomor {} tidak ada'.format(menu_main))
    
if __name__ == '__main__':
    #install_webdriver()
    main()
