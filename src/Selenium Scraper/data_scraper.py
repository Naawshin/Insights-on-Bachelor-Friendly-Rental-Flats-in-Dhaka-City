from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import re
import random

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #chrome_options.add_argument("--headless")
    
    service = Service(r"E:\Data Science\drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scroll_to_bottom(driver, max_scrolls=300):
    
    for i in range(max_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        
        property_count = len(driver.find_elements(By.CSS_SELECTOR, "div.card"))
        print(f"Scroll #{i+1}, Properties found: {property_count}")

def extract_gender(driver, property_url):
    original_window = driver.current_window_handle
    gender = "Not specified"
    
    try:
        # Open property page in new tab
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(property_url)
        time.sleep(2) 
        
        page_text = driver.find_element(By.TAG_NAME, "body").text.lower()
        
        if any(word in page_text for word in ['female']):
            gender = "Female"
        elif any(word in page_text for word in ['male']):
            gender = "Male"
        elif any(word in page_text for word in ['anyone']):
            gender = "Anyone"
            
    except Exception as e:
        print(f"Error extracting gender: {e}")
    finally:
        driver.close()
        driver.switch_to.window(original_window)
        return gender

def extract_property_info(card, driver):
    try:
        card_text = card.text
        lines = card_text.split('\n')
        
        if len(lines) < 2:
            return None
            
        title = lines[0]
        location = lines[1] if len(lines) > 1 else "Not specified"
        details = '\n'.join(lines[2:]) if len(lines) > 2 else ""
        
        # Get property URL
        link_element = card.find_element(By.TAG_NAME, "a")
        property_url = link_element.get_attribute("href")
        
        # Rent extraction
        rent_match = re.search(r'Rent[:\s]*([\d,]+)', details, re.IGNORECASE)
        rent = int(rent_match.group(1).replace(',', '')) if rent_match else None
        
        # Number of bedrooms
        bed_match = re.search(r'Bed[:\s]*(\d+)', details, re.IGNORECASE)
        bedrooms = int(bed_match.group(1)) if bed_match else None
        
        # Rental type
        text = (title + " " + details).lower()
        if 'seat' in text:
            rent_type = 'Seat'
        elif 'room' in text:
            rent_type = 'Room'
        elif 'apartment' in text or 'flat' in text:
            rent_type = 'Flat'
        elif 'bachelor' in text:
            rent_type = 'Bachelor'
        else:
            rent_type = 'Unknown'
            
        # Extract gender    
        gender = extract_gender(driver, property_url)
        
        return {
            'Title': title,
            'Location': location,
            'Rent': rent,
            'Bedrooms': bedrooms,
            'Rent_Type': rent_type,
            'Gender': gender,
            'Property_URL': property_url  # Added property URL
        }
        
    except Exception as e:
        print(f"Error extracting property info: {e}")
        return None

def main():
    url = "https://www.thetolet.com/bd/property-district/dhaka/dhaka?category=bachelor"
    
    driver = setup_driver()
    
    try:
        driver.get(url)
        time.sleep(3)
        
        # Scroll content
        scroll_to_bottom(driver, max_scrolls=300)
        
        # Extract property info
        property_cards = driver.find_elements(By.CSS_SELECTOR, "div.card")
        all_data = []
        
        print(f"Total properties found: {len(property_cards)}")
        
        for i, card in enumerate(property_cards):
            print(f"Processing property {i+1}/{len(property_cards)}")
            
            property_info = extract_property_info(card, driver)
            if property_info:
                all_data.append(property_info)
                # Print gender information for each entry
                print(f"  - Title: {property_info['Title'][:50]}...")
                print(f"  - Gender: {property_info['Gender']}")
                print(f"  - URL: {property_info['Property_URL']}")
                print("-" * 80)
            else:
                print(f"  - Failed to extract property info for card {i+1}")
                
            time.sleep(2)
        
        if all_data:
            df = pd.DataFrame(all_data)
            df.to_csv("thetolet_properties.csv", index=False, encoding='utf-8')
            print(f"Successfully scraped {len(all_data)} properties")
            
            # Print summary of genders
            gender_counts = df['Gender'].value_counts()
            for gender, count in gender_counts.items():
                print(f"{gender}: {count} properties")
                
        else:
            print("Scraping Failed - No data extracted")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()