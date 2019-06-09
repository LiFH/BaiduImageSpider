# BaiduImageSpider
the repository use scrapy framework


# start the spider
scrapy crawl baiduSpider

# jobs
## start
scrapy crawl baiduSpider -s JOBDIR=remain/001

## pause
ctrl+C

## restart
scrapy crawl baiduSpider -s JOBDIR=remain/001

## a new job
scrapy crawl baiduSpider -s JOBDIR=remain/002