# JHUScraper

## Description
JHUScraper is a Python tool that uses BeautifulSoup to more easily get job infromation from [jobs.jhu.edu](jobs.jhu.edu). If you have Python downloaded on your computer and are looking for a comprehensive way to look at job postings on the Johns Hopkins career site, give this tool a try! Search with your preferred keywords and get a .csv file of all of the resulting job titles, dates they were posted, and links to learn more and apply!

### Personal Background
I find myself checking the Johns Hopkins career page quite often to look for new postings (they are updated daily). My biggest issue with the search on the site is that the posts are not ordered by date, and there is no option to do so. In order to look at the newest jobs, I tried setting up job alerts through their system, but found that emails were consistently not coming through. To stay up to date with jobs and to practice "automating the boring stuff," I created a tool to scrape all of the job postings that are returned by a simple search on the career page.

Leveraging the JHUScraper.py code, you can search, scrape, and export job information in just a few lines of code. You can also run the QuickSearch.py file to interactively type your search terms and get results exported to a .csv file.

## Installation
Assuming you already have Python and some standard libraries installed on your computer (pandas, requests, BeautifulSoup), all you have to do is clone this repository or download the .zip file to your computer.

## Usage
Basic usage of this tool is as easy as 1, 2, 3!

```Python
from JHUScraper import *
```
#  
1. Create a JHUScraper instance with your search terms
```Python
scraper = JHUScraper('search terms')
```
2. Scrape all the results from the jobs.jhu.edu site
```Python
scraper.scrape_all_results()
```
3. Export the job information to a .csv
```Python
scraper.jobs_to_csv()
```

## Interactive Use
If you find yourself not wanting to edit the code or do any programming, you can also just run the interactive QuickSearch.py file and type your search terms when prompted.

1. Double-click on the QuickSearch.py file from your prefered directory 

![image](https://user-images.githubusercontent.com/50993629/110374678-f1db7e00-801e-11eb-868a-a41b3174bbf6.png)

2. Type your search terms when prompted and hit enter

![image](https://user-images.githubusercontent.com/50993629/110375209-aaa1bd00-801f-11eb-9d42-3f9b0cc21f6a.png)

3. Open the resulting .csv and explore your job options

![image](https://user-images.githubusercontent.com/50993629/110375445-f7859380-801f-11eb-9d43-ae3fb21b042d.png)

## License
I opted for the MIT License so that others are able to use this code as they please.
