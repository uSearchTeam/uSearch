from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
import requests
from linkedin_api import Linkedin
from get_urls import getEasyApplyURL

email = input("Please enter LinkedIn email: ")
password = input("Please enter LinkedIn password: ")




def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.linkedin.com/")
    page.get_by_role("link", name="Sign in", exact=True).click()
    page.get_by_label("Email or phone").click()
    page.get_by_label("Email or phone").fill(email)
    page.get_by_label("Password", exact=True).click()
    page.get_by_label("Password", exact=True).fill(password)
    page.get_by_label("Password").press("Enter")
    page.goto("https://www.linkedin.com/jobs/view/3934584670/")
    page.get_by_label("Easy Apply to Senior Full stack Developer (Node.js, Java or Ruby on Rails, Angular/React/View) at Ad Analytica", exact=True).click()
    page.get_by_label("Mobile phone number").click()
    page.get_by_label("Mobile phone number").fill("1237342384")
    page.get_by_label("Mobile phone number").press("Enter")
    page.get_by_label("Continue to next step").click()
    page.get_by_role("button", name="Upload resume").click()
    page.get_by_label("Upload resume button. Only,").set_input_files("Document1.docx")
    page.get_by_label("Continue to next step").click()
    input_fields = page.query_selector_all('input')
    return input_fields

        




def main():
    with sync_playwright() as playwright:
        run(playwright)



if __name__ == "__main__":
    main()

