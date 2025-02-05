import joblib
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
# import numpy as np


class Model:
    def __init__(self):
        self.locator_model = joblib.load("/home/sun/procit/QA/model/random_forest_model.pkl")
        self.element_dict = joblib.load("/home/sun/procit/QA/model/element_dict.pkl")
        self.label_to_xpath = {
            "Login": "//*[@id='login-button']",
            "Email": "//input[@id='email']",
            "Password": "//input[@id='password']",
            # Add more mappings here for other elements
        }

    def InvokeSelfHealing(self, exception, driver, locator):
        features = self.extract_features(driver, locator)
        df = pd.DataFrame([features], columns=['tag', 'id', 'type', 'class', 'name', 'aria-autocomplete',
                                                'title', 'href', 'text', 'value', 'aria-label'])
        df = df.fillna('None')
        df_encoded = pd.get_dummies(df)

        model_features = joblib.load("/home/sun/procit/QA/model/train_features.pkl")
        df_encoded = df_encoded.reindex(columns=model_features, fill_value=0)

        predicted_label = self.locator_model.predict(df_encoded)[0]
        print(f"Predicted label: {predicted_label}")
        print(f"Element dict keys: {list(self.element_dict.keys())}")
        print(f"Label to XPath keys: {list(self.label_to_xpath.keys())}")

        if predicted_label in self.label_to_xpath:
            predicted_locator = self.label_to_xpath[predicted_label]
        else:
            print(f"Label '{predicted_label}' not found in label_to_xpath.Using original locator.")
            predicted_locator = locator

        print(f"Final XPath: {predicted_locator}")

        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, predicted_locator))
            )
            print(f"Self-healing successful! Using new locator: {predicted_locator}")
            return element
        except NoSuchElementException:
            print(f"Self-healing failed. Falling back to original locator: {locator}")
            return driver.find_element(By.XPATH, locator)

    @staticmethod
    def extract_features(driver, locator):
        features = []
        try:
            element = driver.find_element(By.XPATH, locator)
            print(f"Element found at locator: {locator}")

            tag = element.tag_name
            element_id = element.get_attribute('id') or 'None'
            element_type = element.get_attribute('type') or 'None'
            element_class = element.get_attribute('class') or 'None'
            name = element.get_attribute('name') or 'None'
            aria_auto = element.get_attribute('aria-autocomplete') or 'None'
            title = element.get_attribute('title') or 'None'
            href = element.get_attribute('href') or 'None'
            text = element.text.strip() or 'None'  # Clean whitespace
            value = element.get_attribute('value') or 'None'
            aria_label = element.get_attribute('aria-label') or 'None'

            features = [tag, element_id, element_type, element_class, name, 
                        aria_auto, title, href, text, value, aria_label]
            print("Extracted Features:")
            print(features)

        except NoSuchElementException:
            print(f"Element NOT found at locator: {locator}")
            features = ['None'] * 11  

        return features

