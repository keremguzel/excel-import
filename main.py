from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import xlsxwriter

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(chrome_options=opts)


driver.get("https://google.com")
driver.maximize_window()

searchBox = driver.find_element(By.CLASS_NAME,"gLFyf")


searchBox.send_keys("IBTECH")
searchBox.send_keys(Keys.ENTER)

links = driver.find_elements(By.CLASS_NAME,"yuRUbf")

link1 = links[0].text.split('https://')
link2 = links[1].text.split('https://')
link3 = links[2].text.split('https://')

ref1 = link1[1].split('.com')
ref2 = link2[1].split('.com')
ref3 = link3[1].split('.com')


driver.close()

workbook = xlsxwriter.Workbook('import_file.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)

worksheet.write('A1', link1[0])
worksheet.write('B1', 'https://' + ref1[0] + '.com')

worksheet.write('A2', link2[0])
worksheet.write('B2', 'https://' + ref2[0] + '.com')

worksheet.write('A3', link3[0])
worksheet.write('B3', 'https://' + ref3[0] + '.com')


workbook.close()







