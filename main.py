import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstagramBot():
    def __init__(self, email, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en, en_US'})
        self.browser = webdriver.Chrome("/Users/alexandermartinez/Downloads/chromedriver",
                                        chrome_options=self.browserProfile)
        self.email = email
        self.password = password
        self.hashtags = []

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        try:
            emailInput.send_keys(self.email)
            passwordInput.send_keys(self.password)
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(2)
            login = True

        except:
            login = False

        return login

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')

        try:
            if (followButton.text != 'Following'):
                followButton.click()
                assert followButton.text == 'Following'
            else:
                print("User already followed!")
            followed = True

        except:
            followed = False

        return followed

    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')

        try:
            if (followButton.text == "Following"):
                followButton.click()
                time.sleep(2)
                confirmButton = self.browser.find_element_by_xpath('//button[text() == "Unfollow"]')
                confirmButton.click()
                assert followButton.text != 'Following'
            else:
                print("User is not being followed.")
            unfollowed = True

        except:
            unfollowed = False


        return unfollowed

    def getUserFollowers(self, username, max_num):
        self.browser.get("https://www.instagram.com/" + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)

        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        followersList.click()
        time.sleep(2)
        actionChain = webdriver.ActionChains(self.browser)

        while (numberOfFollowersInList < max_num):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)

        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector("a").get_attribute('href')
            print(userLink)
            followers.append(userLink)

            if (len(followers) == max_num):
                break

        return followers


    def closeBrowser(self):
        try:
            self.browser.close()
            browser_closed = True
        except:
            browser_closed = False
        return browser_closed

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closeBrowser()
