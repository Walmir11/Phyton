import calendar
import chardet
import holidays
import os
import psutil
import selenium.common
import shutil
import traceback
import undetected_chromedriver as uc
from anticaptchaofficial.imagecaptcha import *
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def start_chrome_driver(path=None,
                        incognito=False,
                        undetected_driver=False,
                        camouflage=False,
                        logs=False,
                        user=None,
                        headless=False,
                        no_images=False):
    if undetected_driver:
        chrome_options = uc.ChromeOptions()
    else:
        chrome_options = webdriver.ChromeOptions()

    chrome_options_list = [
        '--disable-dev-shm-usage',
        '--no-sandbox',
        '--delete-data-on-exit',
        '--disable-default-apps',
        '--site-per-process',
        '--disable-cache',
        '--disable-extensions',
        '--disable-password-saving',
        '--disable-hang-monitor',
        '--sec-ch-ua-platform="Windows"',
        '--sec-gpc=1',
        "--sec-ch-ua-mobile=?0?",
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/126.0.0.0 Safari/537.36',
        "--start-maximized",
        "--disable-infobars",
    ]

    [chrome_options.add_argument(option) for option in chrome_options_list]

    if headless:
        chrome_options.add_argument('--headless')
    if incognito:
        chrome_options.add_argument("--incognito")
    elif user:
        chrome_options.add_argument(f'--user-data-dir={user}')
    if no_images:
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    if logs:
        chrome_options.set_capability('pageLoadStrategy', 'none')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--v=1')

    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    if path is not None:
        prefs = {
            "download.default_directory": path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        }
        chrome_options.add_experimental_option("prefs", prefs)

    if undetected_driver:
        driver = uc.Chrome(options=chrome_options)
    else:
        driver = webdriver.Chrome(options=chrome_options)

    if camouflage:
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride',
                               {
                                   "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                'Chrome/126.0.0.0 Safari/537.36'
                               })
    return driver


def element_css(driver, css):
    return WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, css))
    )


def element_xpath(driver, xpath, timeout=30):
    return WebDriverWait(driver, timeout).until(
        ec.presence_of_element_located((By.XPATH, xpath))
    )


def element_text(driver, text, timer=30):
    return WebDriverWait(driver, timer).until(
        ec.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
    )


def elements_xpath(driver, xpath, timeout=30):
    try:
        return WebDriverWait(driver, timeout).until(
            ec.presence_of_all_elements_located((By.XPATH, xpath))
        )
    except selenium.common.exceptions.TimeoutException:
        return []


def rename_file(old_name, new_name, path):
    # nome do arquivo antigo
    file_name = old_name
    new_file_name = new_name
    way = path
    os.rename(rf'{way}/{file_name}', rf'{way}/{new_file_name}')


def click_mouse_css(driver, css):
    driver.implicitly_wait(10)
    click = element_css(driver, css)
    action = ActionChains(driver)
    action.move_to_element(click).click().perform()
    driver.implicitly_wait(10)


def click_mouse_xpath(driver, xpath, wait=10):
    driver.implicitly_wait(wait)
    click = element_xpath(driver, xpath)
    action = ActionChains(driver)
    action.move_to_element(click).click().perform()
    driver.implicitly_wait(wait)


def double_click_mouse_xpath(driver, xpath):
    driver.implicitly_wait(10)
    click = element_xpath(driver, xpath)
    action = ActionChains(driver)
    action.move_to_element(click).double_click().perform()
    driver.implicitly_wait(10)


def double_click_mouse_css(driver, css):
    driver.implicitly_wait(10)
    click = element_css(driver, css)
    action = ActionChains(driver)
    action.move_to_element(click).double_click().perform()
    driver.implicitly_wait(10)


def click_mouse_class(driver, class_name):
    driver.implicitly_wait(10)
    click = driver.find_element(By.CLASS_NAME, class_name)
    action = ActionChains(driver)
    action.move_to_element(click).click().perform()
    driver.implicitly_wait(10)


def double_click_mouse_class(driver, class_name):
    driver.implicitly_wait(10)
    click = driver.find_element(By.CLASS_NAME, class_name)
    action = ActionChains(driver)
    action.move_to_element(click).double_click().perform()
    driver.implicitly_wait(10)


def click_mouse_text(driver, text):
    driver.implicitly_wait(30)
    click = element_xpath(driver, f"//*[contains(text(), '{text}')]")
    action = ActionChains(driver)
    action.move_to_element(click).click().perform()
    driver.implicitly_wait(10)


def double_click_mouse_text(driver, text):
    driver.implicitly_wait(10)
    click = element_xpath(driver, f"//*[contains(text(), '{text}')]")
    action = ActionChains(driver)
    action.move_to_element(click).double_click().perform()
    driver.implicitly_wait(10)


def open_new_tab(driver, url):
    driver.execute_script(f"window.open('{url}', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])


def clean_folder(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Cound't delete {file}.\nError: {traceback.format_exc()}")


def select_visible_css(driver, css, visible_text):
    select = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, css)))
    select_element = Select(select)
    select_element.select_by_visible_text(visible_text)
    driver.implicitly_wait(10)


def select_visible_xpath(driver, xpath, visible_text):
    select = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, xpath)))
    select_element = Select(select)
    select_element.select_by_visible_text(visible_text)


def move_cursor(driver, css):
    action = ActionChains(driver)
    elem = WebDriverWait(driver, 100).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, css)))
    action.move_to_element(elem)
    action.perform()


def move_cursor_text(driver, text):
    action = ActionChains(driver)
    elem = WebDriverWait(driver, 100).until(
        ec.presence_of_element_located((By.XPATH, f'//*[contains(text(), "{text}")]')))
    action.move_to_element(elem)
    action.perform()


def sign_in(driver, login, password, login_css, password_css):
    try:
        elem = element_css(driver, css=login_css)
        elem.send_keys(login)
        elem = element_css(driver, css=password_css)
        elem.send_keys(password, Keys.RETURN)
        driver.implicitly_wait(10)
    except selenium.common.exceptions.TimeoutException as e:
        raise 'Element not found' from e
    except selenium.common.exceptions.ElementNotInteractableException as e:
        raise "Element can't be interacted with" from e
    except Exception as e:
        raise 'Erro desconhecido' from e


def sign_in_css(driver, login, password, login_css, password_css):
    try:
        elem = element_css(driver, css=login_css)
        elem.send_keys(login)
        elem = element_css(driver, css=password_css)
        elem.send_keys(password, Keys.RETURN)
        driver.implicitly_wait(10)
    except selenium.common.exceptions.TimeoutException as e:
        raise 'Element not found' from e
    except selenium.common.exceptions.ElementNotInteractableException as e:
        raise "Element can't be interacted with" from e
    except Exception as e:
        raise 'Erro desconhecido' from e


def sign_in_xpath(driver, login, password, login_xpath, password_xpath):
    try:
        elem = element_xpath(driver, xpath=login_xpath)
        elem.send_keys(login)
        elem = element_xpath(driver, xpath=password_xpath)
        elem.send_keys(password, Keys.RETURN)
        driver.implicitly_wait(10)
    except selenium.common.exceptions.TimeoutException as e:
        raise 'Element not found' from e
    except selenium.common.exceptions.ElementNotInteractableException as e:
        raise "Element can't be interacted with" from e
    except Exception as e:
        raise 'Erro desconhecido' from e


def move_cursor_text(driver, text):
    action = ActionChains(driver)
    elem = WebDriverWait(driver, 100).until(
        ec.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]")))
    action.move_to_element(elem)
    action.perform()


def sign_in_virtaus(driver, login, password):
    driver.execute_script("captchaNeeded = false")

    elem = driver.find_element(By.CSS_SELECTOR, '#emailAddress')
    elem.send_keys("dev@tnpromotora.com.br")

    elem = driver.find_element(By.CSS_SELECTOR, '#password')
    elem.send_keys("Rhcp@1205", Keys.RETURN)


def element_exists(driver, css):
    try:
        driver.find_element(By.CSS_SELECTOR, css)
    except selenium.common.NoSuchElementException:
        return False
    return True


def element_exists_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except selenium.common.NoSuchElementException:
        return False
    return True


def element_exists_text(driver, text):
    try:
        driver.find_element(By.XPATH, f"//*[contains(., '{text}')]")
    except selenium.common.NoSuchElementException:
        return False
    return True


def close_current_tab(driver):
    driver.close()
    driver.switch_to.window(window_name=driver.window_handles[0])


def table_to_dataframe(driver, css):
    table_element = WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.CSS_SELECTOR, css)))
    return table_element.get_attribute('outerHTML')


###Deprecated. Kept for old code
def convert_to_float(string):
    return convert_to_numeric(string)


def break_captcha(driver, path, css):
    clean_folder(path)
    elem = driver.find_element(By.CSS_SELECTOR, css)
    screenshot = elem.screenshot_as_png

    with open(f"{path}/captcha.png", "wb") as file:
        file.write(screenshot)

    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("9215e0d20b6794b80ca07c0bc009f0b1")

    # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
    solver.set_soft_id(0)
    result = solver.solve_and_return_solution(f"{path}/captcha.png")

    if result != 0:
        return result
    else:
        raise Exception('Captcha error')


def break_captcha_xpath(driver, path, xpath):
    clean_folder(path)
    elem = element_xpath(driver, xpath)
    screenshot = elem.screenshot_as_png

    with open(f"{path}/captcha.png", "wb") as file:
        file.write(screenshot)

    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("9215e0d20b6794b80ca07c0bc009f0b1")

    # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
    solver.set_soft_id(0)
    result = solver.solve_and_return_solution(f"{path}/captcha.png")

    if result != 0:
        return result
    else:
        raise Exception('Captcha error')


def delete_xpath(driver, xpath, timeout=10):
    driver.execute_script("arguments[0].remove();", element_xpath(driver, xpath, timeout))


def remove_items(test_list, item):
    return list(filter(item.__ne__, test_list))


def move_cursor_xpath(driver, xpath):
    action = ActionChains(driver)
    elem = WebDriverWait(driver, 100).until(
        ec.presence_of_element_located((By.XPATH, xpath)))
    action.move_to_element(elem)
    action.perform()


def camouflaged_move_xpath(driver, xpath, interval=2000):
    action = ActionChains(driver)
    pointer_action = action.w3c_actions.pointer_action
    pointer_action._duration = interval
    elem = WebDriverWait(driver, 100).until(
        ec.presence_of_element_located((By.XPATH, xpath)))
    pointer_action.move_to(elem)


def accept_alerts(driver):
    while True:
        try:
            alert = WebDriverWait(driver, 5).until(ec.alert_is_present())
            alert.accept()
            sleep(1)
        except Exception:
            break


def accept_alerts(driver):
    while True:
        try:
            alert = WebDriverWait(driver, 5).until(ec.alert_is_present())
            alert.accept()
            sleep(1)
        except Exception:
            break


def n_dia_util(today: datetime, pais: str = "BR", ):
    if today.day < 1:
        raise ValueError("O valor de n deve ser >= 1")
    feriados = holidays.country_holidays(pais)
    _, n_dias_no_mes = calendar.monthrange(today.year, today.month)
    dias_uteis = []
    for dia in range(1, today.day):
        data = today.replace(day=dia)
        if (
                data.weekday() < 5 and  # data não é sábado/domingo
                data not in feriados  # e também não é feriado
        ):
            dias_uteis.append(data)
    try:
        return dias_uteis[-1]
    except IndexError:
        return None


def kill_process_by_exename(exename):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == exename:
            proc.kill()
            return True
    return False


def kill_process_chrome():
    while True:
        a = kill_process_by_exename(exename='chrome.exe')

        b = kill_process_by_exename(exename='chromedriver.exe')

        if not a and not b:
            break
    sleep(5)


def send_date_xpath(driver, xpath, minus_days=0, bars=True, skip_escape=False):
    date = element_xpath(driver, xpath)
    date.send_keys(Keys.CONTROL + "a")
    date.send_keys(Keys.DELETE)
    date.send_keys(
        (datetime.today() - timedelta(days=minus_days)).strftime("%d/%m/%Y" if bars else "%d%m%Y"))
    if not skip_escape:
        element_xpath(driver, '/html/body').send_keys(Keys.ESCAPE)


def send_date_css(driver, css, minus_days=0, bars=True):
    date = element_css(driver, css)
    date.send_keys(Keys.CONTROL + "a")
    date.send_keys(Keys.DELETE)
    date.send_keys(
        (datetime.today() - timedelta(days=minus_days)).strftime("%d/%m/%Y" if bars else "%d%m%Y"))
    element_xpath(driver, '/html/body').send_keys(Keys.ESCAPE)


def right_click_css(driver, css):
    driver.implicitly_wait(2)
    action = ActionChains(driver)
    click = element_xpath(driver, css)
    action.context_click(click).perform()
    driver.implicitly_wait(10)


def right_click_text(driver, text):
    driver.implicitly_wait(2)
    action = ActionChains(driver)
    click = element_text(driver, text)
    action.context_click(click).perform()
    driver.implicitly_wait(10)


def right_click_xpath(driver, xpath):
    driver.implicitly_wait(2)
    action = ActionChains(driver)
    click = element_xpath(driver, xpath)
    action.context_click(click).perform()
    driver.implicitly_wait(2)


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = str(result['encoding'])
    print(f'The encoding of the file is: {encoding}')
    return encoding


def delete_file(path):
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass


def convert_to_numeric(number_string):
    if isinstance(number_string, float):
        return number_string
    elif isinstance(number_string, int):
        return float(number_string)

    if '.' in number_string and ',' in number_string:
        if number_string.find('.') < number_string.find(','):
            number_string = number_string.replace('.', '')
            number_string = number_string.replace(',', '.')
        else:
            number_string = number_string.replace(',', '')
    elif ',' in number_string:
        number_string = number_string.replace(',', '.')
    return float(number_string)


def post_proposal(solicitacao):
    response = requests.post("http://172.16.26.20:8000/approve",
                             headers={
                                 'Content-Type': 'application/json'
                             },
                             data=json.dumps({
                                 "solicitacao": solicitacao
                             }))
    print(response.text)


def check_existing_proposals(proposals, bank):
    payload = []
    for proposal in proposals:
        payload.append({
            "proposal": proposal,
            "banco": bank
        })

    response = requests.post("http://172.16.26.20:8000/check_existing",
                             headers={
                                 'Content-Type': 'application/json'
                             },
                             data=json.dumps(payload))

    return [proposal.get("proposal") for proposal in response.json()]


def post_proposal_not_mapped(bank_name: str, valor: float, proposal_id: str):
    response = requests.post("http://172.16.26.20:8000/not_mapped/approve",
                             headers={
                                 'Content-Type': 'application/json'
                             },
                             json={
                                 "bank_name": bank_name,
                                 "valor": valor,
                                 "proposal_id": str(proposal_id)
                             })
    print(response.text)


def post_portab(proposta, valor, banco):
    print(requests.post(url="http://172.16.26.20:8000/portab/approve", headers={"Content-Type": "application/json"},
                        json={
                            "bank_name": str(banco),
                            "value": convert_to_numeric(valor),
                            "proposal_id": str(proposta)
                        }))
    return
