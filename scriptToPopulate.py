from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import random

class InstaBot:
    def __init__(self, username, password, post_to_share, destinations_batch_size, alternative_messages, destinations):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)

        # Find the username text box and enters the username
        self.driver.find_element(by=By.XPATH, value="//input[@name=\"username\"]").send_keys(username)

        # Find the password text box and enters the password
        self.driver.find_element(by=By.XPATH, value="//input[@name=\"password\"]").send_keys(password)

        # Click on login button
        self.driver.find_element(by=By.XPATH, value="//button[@type=\"submit\"]").click()

        sleep(3)

        # Go to the page you want to share
        self.driver.get(post_to_share)

        sleep(2)

        # Click Share Post button
        svg = self.driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Share Post']")
        svg.find_element(by=By.XPATH, value="../..").click()

        destinations_counter = 0
        
        # Repeat the steps for each influencer
        for influencer in destinations:
            destinations_counter += 1
            sleep(2)
            
            # Types the influencer name
            self.driver.find_element(by=By.XPATH, value="//input[@placeholder='Search...']").send_keys(influencer)
            sleep(2)

            # Gets the exact match in the results and clicks it to be added to the list
            exact_match = self.driver.find_element(by=By.XPATH, value="//div[text()='" + influencer + "']")
            exact_match.find_element(by=By.XPATH, value="../..").click()

            sleep(2)

            if destinations_counter == destinations_batch_size:
                destinations_counter = 0
                
                # Type a random message in the share dialog from the list
                self.driver.find_element(by=By.XPATH, value="//input[@placeholder='Write a message...']").send_keys(random.choice(alternative_messages))
                
                # Sleep enough seconds to interact with the page before it sends the message
                sleep(10)

                # Click in the send button
                send_button = self.driver.find_element(by=By.XPATH, value="//button//*[contains(text(), 'Send')]")
                send_button.find_element(by=By.XPATH, value="..").click()

                sleep(4)

                # Click Share Post button again
                svg = self.driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Share Post']")
                svg.find_element(by=By.XPATH, value="../..").click()

                sleep(2)
 

with open("igbot-input.yaml", "r") as stream:
    try:
        loaded_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

InstaBot(
    loaded_data['username'], 
    loaded_data["password"],
    loaded_data["post_to_share"],
    loaded_data["destinations_batch_size"],
    loaded_data["alternative_messages"],
    loaded_data["destinations"])
