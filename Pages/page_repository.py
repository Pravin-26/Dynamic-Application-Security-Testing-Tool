class Homepage():

    def __init__(self,driver):
        self.driver= driver
        self.vulnerable_textbox_id = "query"               #locator for vulnerable field on demo.testfire.net
        self.google_textbox_name = 'q'
        self.sql_vulnerableapp_name = "name"
        self.sql_vulnerableapp_password = "password"
    
    def enter_payload(self, payload):                                                   # vulnerable field for xss - demo.testfire.net
        self.driver.find_element_by_id(self.vulnerable_textbox_id).clear()
        self.driver.find_element_by_id(self.vulnerable_textbox_id).send_keys(payload)
    
    def enter_payload_google_textbox(self, payload):                                    # vulnerable field for xss - google.com
        self.driver.find_element_by_name(self.google_textbox_name).clear()
        self.driver.find_element_by_name(self.google_textbox_name).send_keys(payload)
    
    def enter_sqlpayload_textbox_name(self, payload):                                    # SQL injection payload for username textbox
        self.driver.find_element_by_name(self.sql_vulnerableapp_name).clear()
        self.driver.find_element_by_name(self.sql_vulnerableapp_name).send_keys(payload)
    
    def enter_sqlpayload_textbox_password(self, payload):                                # SQL injection payload for password textbox
        self.driver.find_element_by_name(self.sql_vulnerableapp_password).clear()
        self.driver.find_element_by_name(self.sql_vulnerableapp_password).send_keys(payload)