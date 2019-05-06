#COVERBROWSER-SCRAPER

This is a webscraper for [cover browser](http://www.coverbrowser.com). It requires that you install scrapy `pip install scrapy` and boto `pip install boto`.
##Setup

Once everything is installed, simply replace the `http://www.coverbrowser.com/covers/XXXX` with the coverbrowser URL of your choice (for a specific magazine), and set up your preferred image pipeline using the `IMAGES_STORE` variable in the `settings.py` file. If you’d like to write to an S3 bucket instead of your local system, uncoment the `# “s3://yourbucket` after the filesystem variable and add your access key and secret below. You can also create different folders of differently-sized images by adding to the `IMAGES_THUMBS` variable in settings, for example:

`IMAGES_THUMBS = {
  ‘little’: (20, 20),
  ‘big’:(100, 100)
}`

