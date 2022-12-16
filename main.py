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

newLinks = []
newRefs = []

for i in range(len(links)):
    newLinks.append(links[i].text.split('https://'))


for j in range(len(links)):
    if '.net' in newLinks[j][1]:
        newRefs.append(newLinks[j][1].split('.net'))
    elif '.io' in newLinks[j][1]:
        newRefs.append(newLinks[j][1].split('.io'))
    else:
        newRefs.append(newLinks[j][1].split('.com'))


driver.close()

workbook = xlsxwriter.Workbook('import_file.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', len(links))
worksheet.set_column('B:B', len(links))

text1 = 'A{n:.2f}'
text2 = 'B{n:.2f}'
for j in range(len(newLinks)):
    for k in range(1):
        stringLink = newLinks[j][k]
        stringRef = newRefs[j][k]
        worksheet.write(text1.format(n = j+1), stringLink)
        worksheet.write(text2.format(n = j+1), 'https://' + stringRef + '.com')

workbook.close()

