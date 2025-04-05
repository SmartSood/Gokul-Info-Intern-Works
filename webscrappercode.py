from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
# URL of the website to scrape
url = "https://registration2022.pseb.ac.in/School/Schoollist#"

# Initialize the WebDriver (assuming you have chromedriver installed)
driver = webdriver.Chrome()

# Open the URL
driver.get(url)

# Wait for the table to be visible
wait = WebDriverWait(driver, 10)
table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table")))

# Get the page source after JavaScript execution
html = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Find the table containing the data
table = soup.find("table")

# Initialize lists to store data
school_names = []
school_codes = []
school_type = []
school_contacts=[]
principal_names = []
mobile_numbers = []
phone_numbers = []
email_ids = []
# Extract data from the table
def scrape_page(soup):
    for row in table.find_all("tr")[1:]:  # Skip the first row (header row)
        cells = row.find_all("td")
        print(cells)
        school_names.append(cells[1].text.strip()if len(cells) > 2 else None)
        school_codes.append(cells[0].text.strip() if len(cells) > 2 else None)
        school_type.append(cells[2].text.strip() if len(cells) > 2 else None)
        contact_cell = cells[3] if len(cells) > 3 else None
        if contact_cell:
                contact_link = contact_cell.find("a", class_="tip")
                if contact_link:
                    contact_details = contact_link["rel"]
                    school_contacts.append(contact_details)
                else:
                    school_contacts.append("No contact details available")
        else:
                school_contacts.append("No contact details available")
        if contact_cell:
            contact_link = contact_cell.find("a", class_="tip")
            if contact_link:
                contact_details = contact_link["rel"]
                # if isinstance(contact_details, list):
                #     contact_details = contact_details[0]  # Extract the string from the list
                
                # Split the contact details into individual words
                contact_details_list = contact_details

                # Extract information based on known positions
                try:
                    principal_index = contact_details_list.index('Principal') + 3
                    principal_index_finish=contact_details_list.index('Mobile')
                    principal_name =" "
                    for i in range(principal_index ,principal_index_finish):
                        principal_name = principal_name + contact_details_list[i] + " "
                    if principal_name==" ":
                        principal_name="No Principal Name"
                except:
                    principal_name = "No Principal Name"
                    
                try:
                    mobile_index = contact_details_list.index('Mobile') + 3
                    mobile_number = contact_details_list[mobile_index]
                    if(mobile_number=="Phone"):
                        mobile_number = "No Mobile Number"
                except:
                    mobile_number = "No Mobile Number"

                try:
                    phone_index = contact_details_list.index('Phone') + 3
                    phone_number = contact_details_list[phone_index]
                    if(phone_number=="Email"):
                        phone_number = "No Phone Number"
                except:
                    phone_number = "No Phone Number"

                try:
                    email_index = contact_details_list.index('Email') + 3
                    email_id = contact_details_list[email_index]
                except:
                    email_id = "No Email ID"
                
                principal_names.append(principal_name)
                mobile_numbers.append(mobile_number)
                phone_numbers.append(phone_number)
                email_ids.append(email_id)
            else:
                principal_names.append("No contact details available")
                mobile_numbers.append("No contact details available")
                phone_numbers.append("No contact details available")
                email_ids.append("No contact details available")
        else:
            principal_names.append("No contact details available")
            mobile_numbers.append("No contact details available")
            phone_numbers.append("No contact details available")
            email_ids.append("No contact details available")
time.sleep(5)
while True:
    # Get the page source after JavaScript execution
    html = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(html, "html.parser")

    # Scrape data from the current page
    scrape_page(soup)

    # Try multiple methods to find the "Next" button
    try:
        # Option 1: Using ID (preferred if unique)
        next_button = driver.find_element(By.ID, "btnNext")

    except (NoSuchElementException):
        try:
            # Option 2: Using XPath (fallback option)
            next_button = driver.find_element(By.XPATH, "//a[contains(@text(), 'Next')]")

        except (NoSuchElementException):
            try:
                # Option 3: Using Link Text (less specific)
                next_button = driver.find_element(By.LINK_TEXT, "Next")

            except (NoSuchElementException, StaleElementReferenceException):
                # No button found using any method, assume no more pages
                print("Next button not found or inaccessible. Assuming no more pages.")
                break

    # Check if the "Next" button is disabled
    if 'disabled' in next_button.get_attribute("class"):
        # If disabled, no more pages left
        break

    # Click the "Next" button
    next_button.click()

    time.sleep(5)
#uncomment if you want to see output 
# for name, code, typ, principal, mobile, phone, email,contactdetail in zip(school_names, school_codes, school_type, principal_names, mobile_numbers, phone_numbers, email_ids,school_contacts):
#     print(f"School Name: {name}, School Code: {code}, Type: {typ}, Principal: {principal}, Mobile: {mobile}, Phone: {phone}, Email: {email}")
#     print(f"Contact Details: {contactdetail}")
data = {
    "School Name": school_names,
    "School Code": school_codes,
    "School Type": school_type,
    "Principal Name": principal_names,
    "Mobile Number": mobile_numbers,
    "Phone Number": phone_numbers,
    "Email ID": email_ids,
    "Contact Details":school_contacts
}
df = pd.DataFrame(data)

# Write the data to an Excel file
df.to_excel("school_data2.xlsx", index=False)
# Close the WebDriver
driver.quit()
