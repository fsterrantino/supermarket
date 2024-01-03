from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from extract_aux_scripts.initiate_driver import initiate_driver

driver, wait = initiate_driver()

def safe_find_element(search_term, method):
    try:
        match method:
            case 'id':
                element = wait.until(EC.presence_of_element_located((By.ID, search_term)))
            case 'xpath':
                element = wait.until(EC.presence_of_element_located((By.XPATH, search_term)))
            case 'tagname':
                element = wait.until(EC.presence_of_element_located((By.TAG_NAME, search_term)))
    except Exception as e:
        print(f"Error: {e}")
        return None
    return element