from scrapy import cmdline
cmdline.execute('scrapy crawl personal -s LOG_FILE=all.log'.split())

# -s LOG_FILE=all.log