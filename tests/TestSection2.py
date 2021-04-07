import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.ArticlePage import article_page
from Methods.GenericActions import generic_actions


class test_article_page (unittest.TestCase, article_page):

    def test_setUp(self):
        wd = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        self.articlePage = article_page(wd)
        self.action = generic_actions(wd)
        self.action.load_page(self.articlePage.urlArticle)

    # finds disclaimer and check the link
    def test_disclaimer(self):
        # find the disclaimer.
        self.assertTrue(self.action.is_element_present(By.XPATH, self.articlePage.disclaimer))
        # verify link is valid.
        self.assertTrue(self.action.link_works(self.articlePage.disclaimerLink))

    # finds footer and check the text for match
    def test_footer(self):
        # find footer
        self.assertTrue(self.action.is_element_present(By.XPATH, self.articlePage.footer))
        # check text
        self.assertTrue(self.action.check_text(self.articlePage.footerText, self.articlePage.footer))

    # finds social links and check the link is accessible
    def test_socialLinks(self):
        # check social media links
        self.assertTrue(self.action.is_element_present(By.XPATH, self.articlePage.facebook))
        self.assertTrue(self.action.is_element_present(By.XPATH, self.articlePage.twitter))
        # test each one
        self.assertTrue(self.action.link_works(self.articlePage.facebook))
        self.assertTrue(self.action.link_works(self.articlePage.twitter))

    # finds "find my match section", tests the button
    def test_findMatch_form(self):
        # check for zipcode field exist
        self.assertTrue(self.action.is_element_present(By.XPATH, self.articlePage.zipcode))
        self.assertTrue(self.action.is_clickable(self.articlePage.matchbutton))
        # test button with no zipcode
        self.articlePage.driver.find_element_by_xpath(self.articlePage.matchbutton).click()
        self.assertFalse(self.action.is_dif_tab(self.articlePage.urlArticle))
        # write a valid zipcode
        self.action.write_zipcode(self.articlePage.zipNumber, self.articlePage.zipcode)
        # test button with zipcode
        self.articlePage.driver.find_element_by_xpath(self.articlePage.matchbutton).click()
        time.sleep(4)
        self.articlePage.driver.switch_to_window(self.articlePage.driver.window_handles[1])
        time.sleep(4)
        self.assertTrue(self.action.is_dif_tab(self.articlePage.urlArticle))

    # on related news section, checks first element
    def test_Latest_News_firstElem(self):
        # find first element on side
        self.assertTrue(self.action.is_element_present(By.XPATH, self.articlePage.latestNewsFirst))
        # test the link
        self.assertTrue(self.action.link_works(self.articlePage.latestNewsFirst))

    # on related news section, checks last element
    def test_Latest_News_lastElem(self):
        # find last element on side
        self.assertTrue(self.action.is_element_present(By.XPATH, self.articlePage.latestNewsLast))
        # test the link
        self.assertTrue(self.action.link_works(self.articlePage.latestNewsLast))

    def tearDown(self):
        self.articlePage.driver.close()

# this is the class to run
class MyTestSuite(unittest.TestCase):

    def test_suit_excecuter(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_article_page),
        ])
        runner1 = HtmlTestRunner.HTMLTestRunner(output="../Reports")
        runner1.run(smoke_test)



