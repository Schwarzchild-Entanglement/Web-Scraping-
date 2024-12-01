# basic web scraping project. scraping from a local html file. My first scraping project
from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, "lxml") # creating object of html file
course_cards = soup.find_all("div", class_="card") # finding all course tags

for course in course_cards: # iterating through each <div> tag containing information about course
    course_name = course.h5.text # getting course name (stored in <h5> tag)
    course_price = course.a.text.split()[2] # getitng last element of course price in <a> tag stored in a string
                                            # can also use split()[2]
    print(f"{course_name} costs {course_price}") # dynamic string printing course name and price

    
