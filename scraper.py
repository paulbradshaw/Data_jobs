# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
url = 'http://careerssearch.bbc.co.uk/jobs/search'
html = scraperwiki.scrape(url)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
#results > ul > li:nth-child(1) > a > h3 > span
jobtitles = root.cssselect("ul li a h3 span.job-list-title")
for job in jobtitles:
  job = lxml.html.tostring(job)
  print 'job title1:', job
  print 'job title:', job.split('>')[1].split('<')[0]
  record['job'] = job
  scraperwiki.sqlite.save(unique_keys=['job'], data=record)
#
# # An arbitrary query against the database


# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
