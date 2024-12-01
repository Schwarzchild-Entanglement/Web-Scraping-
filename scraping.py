from bs4 import BeautifulSoup
from scraping3 import find_jobs

with open('home.html') as html_file: # creating object for html file
    content = html_file.read() # reading html file
    
soup = BeautifulSoup(content, "lxml")
courses_tags = soup.find_all("h5") # finds all h5 tags in html file. (find() will only return the first)
print(soup.prettify()) # prints html file in a prettier way. use this to print html files
print(courses_tags)

for course in courses_tags: # iterates through all tags
    print(course.text) # prints the text attributes of each <h5> tag

find_jobs()