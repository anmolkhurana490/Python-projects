from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Note: You have verify the captcha (just click the checkbox) manually. That's not automated!

class User:
    def __init__(self):
        self.driver=wb.Chrome()
    
    def login(self, username, password):
        # logging in to your profile
        self.driver.get("https://leetcode.com/accounts/login/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "login").send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="signin_btn"]').click()
        time.sleep(3)

    def get_leetcode_problems(self, page, status):
        # link of leetcode problemset
        if status=="solved":
            url=f"https://leetcode.com/problemset/?page={page}&status=AC"
        elif status=="attempted":
            url=f"https://leetcode.com/problemset/?page={page}&status=TRIED"
        self.driver.get(url)
        time.sleep(3)

        # as 3rd table contains our list of problems
        problems_table=self.driver.find_elements(By.XPATH, "//div[@role='table']")[2]
        table_rows=problems_table.find_elements(By.XPATH, ".//div[@role='row']")
        
        problems={
            "problem_no.": [],
            "title": [],
            "status": [],
            "difficulty": [],
            "problem_url": []
        }

        # excluding 1st row as it is table header
        if(page==1):
            problems_rows=table_rows[2:]
        else:
            problems_rows=table_rows[1:]
        
        # storing data of each solved problem
        for row in problems_rows:
            cells=row.find_elements(By.XPATH, ".//div[@role='cell']")
            problems["problem_no."].append(cells[1].text.split('.')[0])
            problems["title"].append(cells[1].text.split('.')[1].strip())
            problems["status"].append(status)
            problems["difficulty"].append(cells[4].text)
            problems["problem_url"].append(cells[1].find_element(By.TAG_NAME, "a").get_attribute("href"))
        
        return problems
    
    def collect_all_problems(self, pages, status):
        all_problems=pd.DataFrame(columns=["problem_no.", "title", "status", "difficulty", "problem_url"])

        # storing data of each page
        for page_no in range(pages):
            currPage_problems=self.get_leetcode_problems(page_no+1, status)
            all_problems=pd.concat([all_problems, pd.DataFrame(currPage_problems)])
        
        # saving data into csv file
        all_problems.to_csv("my_leetcode_problems.csv", index=False)
        
if __name__=="__main__":
    username=input("Enter your Leetcode Username: ")
    password=input("Enter your Leetcode Password: ")

    print("Opening Chrome Browser...")
    profile=User()

    print("Logging in to your Leetcode Account...")
    profile.login(username, password)

    print("Collecting your list of problems...")
    profile.collect_all_problems(4, "solved")
    print("Saved your problems into CSV file successfully!!!")