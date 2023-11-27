from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from urllib.request import Request, urlopen

def bana():
    url = "https://www.banapresso.com/store"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    # 추출 과정
    name_list = []
    address_list = []
    img_list = []
    img_path_list = []
    for i in range(3):
        list_div_xpath = "/html/body/div/div/div/div/article/article/div/div[1]/div[2]"
        next_button_xpath = "/html/body/div/div/div/div/article/article/div/div[1]/div[3]/span[2]/a"
        if ( i == 2 ):
            for j in range(1, 4):
                section_xpath = f"/html/body/div/div/div/div/article/article/div/div[1]/div[3]/ul/li[{j}]/a"
                section = driver.find_element(By.XPATH, section_xpath).click()

                name_and_address_list_div = driver.find_element(By.XPATH, list_div_xpath).find_elements(By.CLASS_NAME, "store_name_map")
                for k in name_and_address_list_div:
                    name = k.text.split("\n")[1]
                    address = k.text.split("\n")[2]
                    name_list.append(name)
                    address_list.append(address)

                img_list_div = driver.find_element(By.XPATH, list_div_xpath).find_elements(By.CLASS_NAME, "store_photo")
                for k in img_list_div:
                    list_img = k.find_element(By.TAG_NAME, "img")
                    image_url = list_img.get_attribute("src")
                    img_list.append(image_url)

        else:
            for j in range(1, 6):
                section_xpath = f"/html/body/div/div/div/div/article/article/div/div[1]/div[3]/ul/li[{j}]/a"
                section = driver.find_element(By.XPATH, section_xpath).click()

                name_and_address_list_div = driver.find_element(By.XPATH, list_div_xpath).find_elements(By.CLASS_NAME, "store_name_map")
                for k in name_and_address_list_div:
                    name = k.text.split("\n")[1]
                    address = k.text.split("\n")[2]
                    name_list.append(name)
                    address_list.append(address)

                img_list_div = driver.find_element(By.XPATH, list_div_xpath).find_elements(By.CLASS_NAME, "store_photo")
                for k in img_list_div:
                    list_img = k.find_element(By.TAG_NAME, "img")
                    image_url = list_img.get_attribute("src")
                    img_list.append(image_url)
            next_button = driver.find_element(By.XPATH, next_button_xpath).click()
            time.sleep(1.5)

    # 이미지들 파일에 저장하기
    if not os.path.exists("C:/Hong/KDT/231124 바나프레소 과제/banapresso_img"):
        os.mkdir("C:/Hong/KDT/231124 바나프레소 과제/banapresso_img")

    for i in range(len(img_list)):
        img_url = img_list[i]
        ext = img_url.split(".")[-1]
        img_byte = Request(img_url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'})
        path = f"C:/Hong/KDT/231124 바나프레소 과제/banapresso_img/{i}_banapresso_{name_list[i]}.{ext}"
        img_path = f"./banapresso_img/{i}_banapresso_{name_list[i]}.{ext}"
        f = open(path, "wb")
        img_path_list.append(img_path)
        f.write(urlopen(img_byte).read())
        f.close()

    return name_list, address_list, img_path_list