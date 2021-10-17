class Homepage():

    def __init__(self,driver):
        self.driver= driver
        self.vulnerable_textbox_id = "query"
        self.button_xpath = "submit"
        self.google_textbox_xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    
    def enter_payload(self, payload):
        self.driver.find_element_by_id(self.vulnerable_textbox_id).clear()
        self.driver.find_element_by_id(self.vulnerable_textbox_id).send_keys(payload)
    
    def enter_payload_google_textbox(self, payload):
        self.driver.find_element_by_xpath(self.google_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.google_textbox_xpath).send_keys(payload)