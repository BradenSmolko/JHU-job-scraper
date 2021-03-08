from JHUScraper import *

'''
This is an example of scraping the jobs.jhu.edu site with JHUScraper. Three easy steps:

1. Create a JHUScraper object and pass in your search terms (i.e. 'data analyst')
2. Scrape all jobs from the site
3. Export these jobs to a .csv file in your directory
'''

# Step 1.
scraper = JHUScraper('data analyst')

# Step 2.
scraper.scrape_all_results()

# Step 3.
scraper.jobs_to_csv()
