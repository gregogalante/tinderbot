from time import sleep
from selenium import webdriver

class Tinderbot:
  def __init__(self):
    self.driver = webdriver.Chrome()
    self.driver.get('https://tinder.com/')

  def login(self):
    # apro modale per accesso
    modal_login_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
    modal_login_button.click()
    sleep(1)
    # eseguo click pulsante login facebook
    fb_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
    fb_button.click()
    sleep(1)
    # eseguo switch a tab di login facebook
    base_window = self.driver.window_handles[0]
    fb_window = self.driver.window_handles[1]
    popup = self.driver.switch_to_window(fb_window)
    # eseguo login facebook
    email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
    password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
    login_button = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
    email_input.send_keys('CAMBIAMI')
    password_input.send_keys('CAMBIAMI')
    login_button.click()
    sleep(1)
    # eseguo switch a tab base
    popup = self.driver.switch_to_window(base_window)
    sleep(1)

  def initDashboard(self):
    # attivo geolocalizzazione
    position_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    position_button.click()
    sleep(1)
    # disattivo notifiche
    notif_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
    notif_button.click()
    sleep(1)
    # disattivo check indirizzo email se compare
    try:
      check_email_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/button[2]')
      check_email_button.click()
      sleep(1)
    except Exception:
      True

  def play(self):
    while True:
      sleep(0.5)
      try:
        self.like()
      except Exception:
        try:
          # provo ad eliminare eventuale popup di invito a utilizzo app
          popup_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
          popup_button.click
        except Exception:
          True

  def like(self):
    like_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
    like_button.click()

  def dislike(self):
    dislike_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
    dislike_button.click()

bot = Tinderbot()
bot.login()
bot.initDashboard()
bot.play()

