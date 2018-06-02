'''
Created on May 21, 2018

@author: HP
'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.vajor.com/customer/account/create")
driver.maximize_window()

# Test case 1
def sign_up_with_valid_credentials():
    driver.find_element_by_id("firstname").send_keys("Kshitiz")
    driver.find_element_by_name("lastname").send_keys("Agarwal")
    driver.find_element_by_name("email").send_keys("k.agarwal4@gmail.com")
    driver.find_element_by_name("mobilenumber").send_keys("9811908880")
    driver.find_element_by_id("password").send_keys("India@000")
    driver.find_element_by_id("password-confirmation").send_keys("India@000")
    driver.find_element_by_id("gender-option-2").click();
    driver.find_element_by_xpath("//button[@title='Sign Up']").click();
    return True


def sign_up_with_invalid_mobile_number():
    driver.find_element_by_id("firstname").send_keys("Kshitiz")
    driver.find_element_by_name("lastname").send_keys("Agarwal")
    driver.find_element_by_name("email").send_keys("k.agarwal4@gmail.com")
    driver.find_element_by_name("mobilenumber").send_keys("kshit")
    driver.find_element_by_id("password").send_keys("India@000")
    driver.find_element_by_id("password-confirmation").send_keys("India@000")
    driver.find_element_by_id("gender-option-2").click();
    driver.find_element_by_xpath("//button[@title='Sign Up']").click();
    message = driver.find_element_by_id("mobilenumber-error").text;
    if message == "Please enter a valid number in this field.":
      print True
    else:
      print False  

    return True

def signup_with_exiting_email_id():
    driver.find_element_by_id("firstname").send_keys("Kshitiz")
    driver.find_element_by_name("lastname").send_keys("Agarwal")
    driver.find_element_by_name("email").send_keys("k.agarwal4@gmail.com")
    driver.find_element_by_name("mobilenumber").send_keys("9811908880")
    driver.find_element_by_id("password").send_keys("India@000")
    driver.find_element_by_id("password-confirmation").send_keys("India@000")
    driver.find_element_by_id("gender-option-2").click();
    driver.find_element_by_xpath("//button[@title='Sign Up']").click();
    message = driver.find_element_by_xpath("//div[@data-bind='html: message.text']").text;
    if message == "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.":
      print True
    else:
      print False  
      
def signup_with_diffrent_password_in_password_confirmpassword_field():
    driver.find_element_by_id("firstname").send_keys("sdgjk")
    driver.find_element_by_name("lastname").send_keys("Agarwal")
    driver.find_element_by_name("email").send_keys("swati.gupta@payu.in")
    driver.find_element_by_name("mobilenumber").send_keys("9011111111")
    driver.find_element_by_id("password").send_keys("India@000")
    driver.find_element_by_id("password-confirmation").send_keys("India")
    driver.find_element_by_id("gender-option-1").click();
    driver.find_element_by_xpath("//button[@title='Sign Up']").click();
    message = driver.find_element_by_xpath("//div[@id='password-confirmation-error']").text;
    if message == "Please enter the same value again.":
      print True
    else:
      print False  
      

    return True

def signup_with_dob():
    driver.find_element_by_id("dob").click()
    time.sleep(2)
   # driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr['2']/td['2']/a")
    driver.find_elements_by_class_name("ui-state-default")[6].click()
     
signup_with_dob()
#sign_up_with_valid_credentials();
#sign_up_with_invalid_mobile_number();
#signup_with_exiting_email_id();
#signup_with_diffrent_password_in_password_confirmpassword_field();

