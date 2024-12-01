
# bring all jobs posted few days ago
# comment it and submit to Github.
from bs4 import BeautifulSoup
import requests
import time

# function to print jobs and company names
def find_jobs():
    # requesting html text from site 
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
    
    # parsing through html text
    soup = BeautifulSoup(html_text,"lxml")

    # jobs object pointing to all jobs which are contained in <li> tags with class mentioned below
    jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")

    # iterating through each job <li> tag
    for job in jobs:
        # getting the date when job was published
        published_date = job.find("span", class_ = "sim-posted").text.strip()

        # only need jobs published "few" days ago
        if "few" in published_date:

            # getiing company name
            company_name = job.find("h3", class_ =  "joblist-comp-name").text.strip()

            # getting skills required
            skills = [job.find("div", class_ = "srp-skills").text]

            # going into a tag and pulling out the href attribute to get link to job
            more_info = job.a["href"]
            cleaned_skills = [skill.strip()for skill in skills[0].replace("\n", "").replace("\t", "").split()]
            
            # writing all jobs to a text file
            with open("jobs/jobs.txt", "a") as  f:
                f.write(f"Company Name: {company_name}\n")
                f.write(f"Required Skills: {cleaned_skills}\n")
                f.write(f"More Info: {more_info}\n")
                f.write(" ")
            
            # also printing jobs to terminal
            print(f"Company Name: {company_name}")
            print(f"Required Skills: {cleaned_skills}")
            print(f"More Info: {more_info}")
            print(" ")

# dunder method to check if script runs from main
if __name__ == "__main__":

    # to keep on repeating the program
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")

        # program sleeps for 10 minutes. Then restarts and goes to while loop.
        # when while loop is executed program reaches the time.sleep() line
        # after which it goes back to sleep again for 10 minutes and the process repeats.
        time.sleep(time_wait * 60)

        
        
