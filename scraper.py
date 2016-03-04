# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
url = 'http://careerssearch.bbc.co.uk/jobs/search'
html = scraperwiki.scrape(url)
#create an empty dictionary variable called record - this will be added to in a line later on (look for record ['job'])
record = {}
root = lxml.html.fromstring(html)
# # Find something on the page using css selectors
jobtitles = root.cssselect("ul li a h3 span.job-list-title")
for job in jobtitles:
  jobhtml = lxml.html.tostring(job)
  jobhtmlpart1 = jobhtml.split('>')[1]
  jobhtmlpart2 = jobhtmlpart1.split('<')[0]
  print 'job title html:', jobhtml
  print 'job title cleaned up:', jobhtmlpart2
  record['job'] = jobhtmlpart2
  print record
  scraperwiki.sqlite.save(unique_keys=['job'], data=record)
#
# # An arbitrary query against the database


# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
