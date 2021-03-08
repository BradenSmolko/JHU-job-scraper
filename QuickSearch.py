"""
This script can be run to enter search terms manually and scrape all of the results to your directory.
"""

from JHUScraper import *

search_terms = input('Enter your search terms and hit enter to run: ')
print('\nGetting job information...')

scraper = JHUScraper(search_terms=search_terms)
scraper.scrape_all_results()
scraper.jobs_to_csv()

print('Done! File can be found in your current working directory.')
