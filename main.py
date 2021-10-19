import pytest
from appium import webdriver
caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=Calculator_v7.8 (271241277)_apkpure.com.apk"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True

class TestSemanaMobile():

    def setup_method(self):
        self.driver = webdriver.Remote(
            "Sua Url", caps)


    def teardown_method(self):
        self.driver.quit()


    def testar_somar_dois_numeros(self):
        resultado_esperado = '13'
        botao8 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_8")
        botao8.click()
        mais = self.driver.find_element_by_id("com.google.android.calculator:id/op_add")
        mais.click()
        botao5 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_5")
        botao5.click()
        igual = self.driver.find_element_by_id("com.google.android.calculator:id/eq")
        igual.click()
        resultado = self.driver.find_element_by_id("com.google.android.calculator:id/result_final")
        assert resultado.text == resultado_esperado

    def testar_subtrair_dois_numeros(self):
        resultado_esperado = '5'
        botao1 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_1")
        botao1.click()
        botao0 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_0")
        botao0.click()
        menos = self.driver.find_element_by_id("com.google.android.calculator:id/op_sub")
        menos.click()
        botao5 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_5")
        botao5.click()
        igual = self.driver.find_element_by_id("com.google.android.calculator:id/eq")
        igual.click()
        resultado = self.driver.find_element_by_id("com.google.android.calculator:id/result_final")
        assert resultado.text == resultado_esperado


    def testar_multiplicar_dois_numeros(self):
        resultado_esperado = '125'
        botao2 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_2")
        botao2.click()
        botao5 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_5")
        botao5.click()
        mult = self.driver.find_element_by_id("com.google.android.calculator:id/op_mul")
        mult.click()
        botao5 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_5")
        botao5.click()
        igual = self.driver.find_element_by_id("com.google.android.calculator:id/eq")
        igual.click()
        resultado = self.driver.find_element_by_id("com.google.android.calculator:id/result_final")
        assert resultado.text == resultado_esperado


    def testar_dividir_dois_numeros(self):
        resultado_esperado = '2'
        botao8 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_8")
        botao8.click()
        mais = self.driver.find_element_by_id("com.google.android.calculator:id/op_div")
        mais.click()
        botao4 = self.driver.find_element_by_id("com.google.android.calculator:id/digit_4")
        botao4.click()
        igual = self.driver.find_element_by_id("com.google.android.calculator:id/eq")
        igual.click()
        resultado = self.driver.find_element_by_id("com.google.android.calculator:id/result_final")
        assert resultado.text == resultado_esperado
