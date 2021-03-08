# JHUScraper

## Description
Are you a Python user looking to work at Johns Hopkins University? You can use this file or framework to scrape job infromation from [jobs.jhu.edu](jobs.jhu.edu) so you can filter and sort job posts and not have to click that pesky 'Show More' button ever again!

### Background
I check jobs.jhu.edu almost daily for job postings at Johns Hopkins, but the site isn't the easiest to use. I am usually only interested in the newest postings because I have already seen the older posts, but the site doesn't allow you to sort the posts by date. One way you can get sorted posts, is by using their 'Job Alert' system, but I've had issues with the system not sending me emails, so I decided to build my own scraper that I could automate and run daily.

Using the JHUScraper class that is defined in the JHUScraper.py file, you can search, scrape, and export job information in just a few lines of code.

## Installation
Assuming you already have Python installed on your machine (I have only tested with Python 3.9), just download the JHUScraper.py file to a folder where you'd like to receive your job information.

## Usage
Like with the ExampleUsage.py file you can create another Python file in the same folder as JHUScraper.py, import the JHUScraper information from the file and then follow 3 steps:

```Python
from JHUScraper import *
```
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

Now you'll have a csv file with date-sorted job information so you can browse the file and follow links for jobs that look interesting. Happy job hunting! 

You can also create a task in something like Windows Task Scheduler to automate the process and get your list of jobs daily.

## License
I opted for the MIT License so that others are able to use this code as they please.
