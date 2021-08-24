from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import json


userName = 'userName' #Vi du: userName = '20139098'
passWord = 'passWord'
namHoc = '2021-2022'
hocKy = 'Học kỳ 1'
tuanHoc = '1'



driver = webdriver.Edge(executable_path='.\Driver\msedgedriver.exe')
driver.get("https://online.hcmute.edu.vn")
driver.find_element_by_id("ctl00_lbtDangnhap").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ctl00_txtUserName").send_keys(userName)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ctl00_txtPassword").send_keys(passWord)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ctl00_btLogin").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ctl00_lnkThoiKhoaBieu").click()

selectNamHoc = Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ctl00_ctl00_ddlNamHoc"))
selectNamHoc.select_by_value(namHoc)
selectHocKy = Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ctl00_ctl00_ddlHocKy"))
selectHocKy.select_by_visible_text(hocKy)
selectTuanHoc = Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ctl00_ctl00_ddlTuan"))
selectTuanHoc.select_by_visible_text(tuanHoc)

soHang = len(driver.find_elements_by_xpath("/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr"))
soCot = len(driver.find_elements_by_xpath("/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td"))

thoiKhoaBieu = { 'THỨ 2': [], 'THỨ 3': [], 'THỨ 4': [], 'THỨ 5': [], 'THỨ 6': [], 'THỨ 7': []}

for cot in range(2, soCot + 1):
    for hang in range(2, soHang + 1):
        q = "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[" + str(hang) + "]/td[" + str(cot) + "]/b"
        if len(driver.find_elements_by_xpath(q)) > 0:
            THU = 'THỨ ' + str(cot)
            crawlXpath = "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[" + str(hang) + "]/td[" + str(cot) + "]"
            crawl = driver.find_element_by_xpath(crawlXpath).text
            crawlList = crawl.split("\n")
            phongHoc = "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[" + str(hang) + "]/td[1]"
            thongTinMonHoc = {'Tên môn': crawlList[0],
                              'Giờ học': crawlList[1],
                              'Tiết học': crawlList[2],
                              'Giáo viên': crawlList[3],
                              'Phòng học': driver.find_element_by_xpath(phongHoc).text}
            thoiKhoaBieu[THU].append(thongTinMonHoc)

driver.close()



def SaveFile(thoiKhoaBieu, isVietnamese=True):

    if isVietnamese:
        with open('ThoiKhoaBieu.json', 'w', encoding='utf-8') as jsonFile:
            json.dump(thoiKhoaBieu, jsonFile, indent=2, ensure_ascii=False)
    else:
        with open('ThoiKhoaBieu.json', 'w') as jsonFile:
            json.dump(thoiKhoaBieu, jsonFile, indent=2)
    return

SaveFile(thoiKhoaBieu, isVietnamese=True)




