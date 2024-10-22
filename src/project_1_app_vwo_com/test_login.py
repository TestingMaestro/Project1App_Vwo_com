import os
import time

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


@allure.title("Verify using invalid email id and invalid password")
@allure.description("Verify using invalid credentials, user stays on login page with proper error message")
def test_vwo_using_invalid_login_tc1(browser_options, launch_chrome):
    load_dotenv()
    user_name = launch_chrome.find_element(By.XPATH, "//input[@id='login-username']")
    user_name.send_keys(os.getenv("INVALID_MAIL_ID"))

    password = launch_chrome.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys(os.getenv("INVALID_PASSWORD"))

    sign_in_btn = launch_chrome.find_element(By.ID, "js-login-btn")
    sign_in_btn.click()
    time.sleep(5)

    error_message = launch_chrome.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message.text)
    assert error_message.text == "Your email, password, IP address or location did not match"

    time.sleep(6)
    user_name.clear()
    password.clear()


@allure.title("Verify using invalid email id and valid password")
@allure.description("Verify using invalid credentials, user stays on login page with proper error message")
def test_vwo_using_invalid_login_tc2(browser_options, launch_chrome):
    load_dotenv()
    user_name = launch_chrome.find_element(By.XPATH, "//input[@id='login-username']")
    user_name.send_keys(os.getenv("EMAIL"))

    password = launch_chrome.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys(os.getenv("INVALID_PASSWORD"))

    sign_in_btn = launch_chrome.find_element(By.ID, "js-login-btn")
    sign_in_btn.click()
    time.sleep(5)

    error_message = launch_chrome.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message.text)
    assert error_message.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
