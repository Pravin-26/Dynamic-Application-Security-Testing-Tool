# Automated Security Testing_Web_Scanner_Software
In recent years, web-applications have become an essential part of our daily life. Web-applications provide digital services like social networking, e-governance, payment of utility bills, online banking, e-commerce etc. The two way-data transfers between web-applications and web-browser makes web-applications attractive to web criminals or hackers for stealing information & committing crimes on internet. Thus, finding vulnerabilities in web-applications becomes crucial part for Application Security team.
There are manual and automated tools methods to perform vulnerability assessment of a web-application. 

In this Project,I have developed automated security testing framework to perform vulnerability assessment and penetration testing in web-applications. The framework includes Python Unit Tests and Selenium IDE for cross-browser testing of web-applications. 
Page Object Model is implemented with Page file will contain constructors for corressponding web elements & then the constructors are used for test cases in Python Unit Test.
Two test cases are included - (1) One test case for Vulnerable website & (2) One test case for secure website - to show accuracy of the software.
In test case for Vulnerable website, a XSS-payload is injected & then alert is captured. A detailed HTML report is generated that will capture alert message & inform necessary remediation steps for protecting the website from XSS.
In test case for Secure website (let's say google), a XSS-payload is injected & then no alert will be genrated because website is protected with CSP. Thus, a detailed HTML report is generated that will inform website is protected from XSS.
Sofwate goes through SDLC which is given below: -

Sofwatare Development Lifycyle (SDLC): - \n
 1.Requirement gathering & Analysis Phase: - Analyzed & gathered information on Selenium architecture, Working of Selenium that will help us to design & implement automated software for detecting vulnerabilities requirements in Web-application!
 2. Sofware Design Phase : - 	Designed software standard Page Object Model framework for software. Defined Page Object Repository & Test File
 3. Coding Phase: - Create Page Object Repository, Create Test file for test script, Implemented Selenium.
 4. Testing Phase: - Implemented Python Unit framework with 3 phases: - Arrange, Act, Assert.
 5. Deployment & Maintenance: - -	After successful testing, deployed script for Cross-Site Scripting attack with continuous maintenance
 
