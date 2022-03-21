from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")

driver = webdriver.Chrome(executable_path=Config.exe_path,
                          chrome_options=opt)
driver.get("https://web.whatsapp.com/")