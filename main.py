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

def purifyExtensions(i, j):
    if '.net' in newLinks[i][j]:
        newRefs.append(newLinks[i][j].split('.net'))
    elif '.io' in newLinks[i][j]:
        newRefs.append(newLinks[i][j].split('.io'))
    elif '.gov' in newLinks[i][j]:
        newRefs.append(newLinks[i][j].split('.gov'))
    elif '.org' in newLinks[i][j]:
        newRefs.append(newLinks[i][j].split('.org'))
    elif '.dev' in newLinks[i][j]:
        newRefs.append(newLinks[i][j].split('.dev'))
    else:
        newRefs.append(newLinks[i][j].split('.com'))

newLinks = []
newRefs = []

for i in range(3):
    links = driver.find_elements(By.CLASS_NAME,"yuRUbf")
    driver.implicitly_wait(3)
    for k in range(1):
        for j in range(9):
            newLinks.append(links[j].text.split('https://'))
    if i == 0:
        for j in range(1):
            for k in range(9):
                purifyExtensions(k,1)
                #newRefs.append(newLinks[k][1].split('.com'))
        driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]').click()
    elif i == 1:
        for j in range(1):
            for k in range(9):
                if k ==4:
                    purifyExtensions(k+9,0)
                    #newRefs.append(newLinks[k + 9][0].split('.com'))
                else:
                    purifyExtensions(k + 9, 1)
                    #newRefs.append(newLinks[k + 9][1].split('.com'))
        driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]').click()
    elif i == 2:
        for j in range(1):
            for k in range(9):
                purifyExtensions(k+18,1)
                #newRefs.append(newLinks[k+18][1].split('.com'))


driver.close()

workbook = xlsxwriter.Workbook('import_file.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', len(newLinks))
worksheet.set_column('B:B', len(newLinks))

text1 = 'A{n:.2f}'
text2 = 'B{n:.2f}'
for j in range(len(newLinks)):
    for k in range(1):
        stringLink = newLinks[j][k]
        stringRef = newRefs[j][k]
        worksheet.write(text1.format(n = j+1), stringLink)
        worksheet.write(text2.format(n = j+1), 'https://' + stringRef + '.com')

workbook.close()

