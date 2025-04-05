from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
url = "https://www.careerindia.com/cbse-schools-in-punjab-s30.html?page=1"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
school_name=[]
school_medium=[]
school_address=[]
school_city=[]
school_state=[]
school_pincode=[]
school_contact=[]
school_email=[]
school_website=[]

def extract_details():
    schools_list = driver.find_elements(By.CLASS_NAME,"edu-school-detlist-container")
    for school in schools_list:
        school_topblock=school.find_element(By.CLASS_NAME,"edu-school-det-topblock")
        school_name.append(school_topblock.find_element(By.CLASS_NAME,"edu-school-det-heading").text)

        school_medium.append(school_topblock.find_element(By.CLASS_NAME,"edu-school-det-subhead").text[8:])
        school_bottomblock=school.find_element(By.CLASS_NAME,"edu-school-det-bottomblock")
        school_details=school_bottomblock.find_elements(By.CLASS_NAME,"edu-school-det-text")
        try:
            school_address.append(school_details[0].text)
        except IndexError:
            school_address.append("N/A")
        
        try:
            school_state.append(school_details[1].text)
        except IndexError:
            school_state.append("N/A")
        
        try:
            school_city.append(school_details[2].text)
        except IndexError:
            school_city.append("N/A")
        
        try:
            school_pincode.append(school_details[3].text)
        except IndexError:
            school_pincode.append("N/A")
        
        try:
            school_contact.append(school_details[4].text)
        except IndexError:
            school_contact.append("N/A")
        
        try:
            school_email.append(school_details[5].text)
        except IndexError:
            school_email.append("N/A")
        
        try:
            school_website.append(school_details[6].text)
        except IndexError:
            school_website.append("N/A")
def change_pages():
    try:
        while True:
            try:
                extract_details()
            except Exception as e:
                 print(f"Error in extracting details: {e}")
            next_page_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "edu-clg-pag-next"))
                )
            next_page_button.click()
            WebDriverWait(driver, 10).until(
                EC.staleness_of(next_page_button)
            )
    except Exception as e:
        print(f"Error navigating to next page: {e}")
def state_change():
    print("State extracting now")
    try:
        state_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "cbse_state_id"))
            )
        for k in range (1,3):
            try:
                    state_dropdown = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, "cbse_state_id"))
                )
                    select=Select(state_dropdown)
                    state_name=(select.options)[k]
                    print(state_name.text)
                    select.select_by_value(str(k))
                    time.sleep(2)
                    change_pages()
            except Exception as e:
                    print(f"Error selecting option: {e}")
    except Exception as e:
        print(f"Error locating dropdown element: {e}")
        
state_change()
data = {
 "school_name": school_name,
 "school_medium":school_medium,
 "School State:":school_state,
 "School City:":school_city,
 "School Address:":school_address,
 "School Pincode:":school_pincode,
 "School Contact:":school_contact,
 "School Email:":school_email,
 "School Website:":school_website

}
df = pd.DataFrame(data)
# Write the data to an Excel file
df.to_excel("school_data_all_india.xlsx", index=False)
# Close the WebDriver
driver.quit()
# comment the line below if not needed
print(school_name)

