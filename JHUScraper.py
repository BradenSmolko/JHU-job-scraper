import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
JHUScraper objects take keywords in the form of a single string (like you would search the site). Calling the object's
get_all_results method will scrape the jobs.jhu.edu site for all results of the search. Calling the object's 
jobs_to_csv function will export the job information to a csv in the same directory as the file. Happy job hunting!
'''


class JHUScraper:
    # Each scraper has a base search url, search terms, and growing lists of job information
    base_url = ''
    search_terms = ''
    scraped_titles = []
    scraped_dates = []
    scraped_links = []

    # Each object is initialized with search terms
    def __init__(self, search_terms):
        self.search_terms = str(search_terms).replace(' ', '+')
        self.base_url = 'https://jobs.jhu.edu/tile-search-results/?q={}'.format(self.search_terms)

    '''
        The jobs.jhu.edu/search-tile-results/ endpoint generates 25 job postings starting at 'startrow=0'. This method
        takes an integer value for startrow and then scrapes the page for the job information. This method returns a 
        list of the job titles, dates that the job was posted, links to each job, and a Boolean flag 'rowsmaxed' 
        indicating if the max number of results (25 jobs) was returned in the scrape. We know that we've found the end 
        of the jobs list when fewer than 25 jobs are returned and rowsmaxed is False.
    '''
    def scrape_page_body(self, startrow=0):
        # Create a search url with the given value of startrow and grab the HTML
        url = self.base_url + '&startrow={}'.format(startrow)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Initialize empty lists to fill
        job_titles = []
        job_dates = []
        job_links = []

        # Get the title, date, and link for each posting on that page
        for div in soup.find_all('div', role='gridcell'):  # Each collection of posts (3 per job) is an a gridcell div
            desktop_version_info = div.find('div').find_all('div')
            title_link_div = desktop_version_info[0]
            job_div = desktop_version_info[2]

            # Dig down to title and link info
            title_link_info = title_link_div.find('a')

            # Get the job link
            job_specific_link = title_link_info['href']
            base = 'https://jobs.jhu.edu'
            job_link = base + job_specific_link
            job_links.append(job_link)

            # Get the title
            title = title_link_info.prettify().splitlines()[1].strip()
            job_titles.append(title)

            # Get the date
            date_div = job_div.find_all('div')[9]
            date = date_div.prettify().splitlines()[1].strip()
            job_dates.append(date)

        rows_maxed = (len(job_links) == 25)
        return job_titles, job_dates, job_links, rows_maxed

    # Add all of the job information to the appropriate instance variables
    def extend_jobs(self, titles, dates, links):
        self.scraped_titles.extend(titles)
        self.scraped_dates.extend(dates)
        self.scraped_links.extend(links)

    '''
    This is the method that you will call to get all of the results (likely what you'll want anytime you use this). It 
    iterates over values of startrow, increasing by 25 to get fully new pages, until it hits a page with fewer than 25 
    jobs. This means that the search results are done and we can stop scraping urls. With each iteration, the job 
    information is added to the appropriate instance variables.
    '''
    def scrape_all_results(self):
        startrow = 0
        rows_maxed = True
        while rows_maxed:
            titles, dates, links, rows_maxed = self.scrape_page_body(startrow)
            self.extend_jobs(titles, dates, links)
            startrow += 25  # Update the startrow parameter for search

    def jobs_to_csv(self):
        data_dict = {'Job Title': self.scraped_titles,
                     'Date Posted': self.scraped_dates,
                     'Link': self.scraped_links}

        # Each unique job has a unique link, so we create a DataFrame and drop duplicates based on this property
        scraped_table = pd.DataFrame(data_dict).drop_duplicates(subset='Link')

        # Convert dates to datetime and sort descending so that newer jobs appear on top
        scraped_table['Date Posted'] = pd.to_datetime(scraped_table['Date Posted'], format='%b %d, %Y')
        scraped_table.sort_values(by=['Date Posted'], ascending=False, inplace=True)

        # Export to csv in directory with a file name based on the search results (trim name if the search is long)
        if len(self.search_terms) > 150:
            search_name = self.search_terms[:151]
        else:
            search_name = self.search_terms

        scraped_table.to_csv('JHUJobs_{}.csv'.format(search_name), index=False)
