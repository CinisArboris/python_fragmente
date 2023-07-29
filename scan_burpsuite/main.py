from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType

class WebTesting:
    def __init__(self, driver, proxy_address):
        self.driver = driver
        self.setup_proxy(proxy_address)

    def setup_proxy(self, proxy_address):
        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = proxy_address
        proxy.ssl_proxy = proxy_address

        capabilities = webdriver.DesiredCapabilities.FIREFOX
        proxy.add_to_capabilities(capabilities)

    def visit_links(self, base_url, links):
        for link in links:
            self.driver.get(f'{base_url}/{link}')

    def authenticate(self, url, username, password):
        self.driver.get(url)

        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'password')

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, 'login')
        login_button.click()

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    driver = webdriver.Firefox()
    tester = WebTesting(driver, "127.0.0.1:8080")
    
    links = ['estudiantes/default.php', 'docentes/default.php', 'administrativos/default.php']
    tester.visit_links('https://perfil.uagrm.edu.bo', links)

    tester.authenticate('https://perfil.uagrm.edu.bo/estudiantes/default.php', '213128780', 'Alicia777')

    tester.quit()
