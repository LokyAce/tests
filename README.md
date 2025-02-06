# tests
Write a script that will read log files and calculate how many events occur per sec\min\hour. 
Log format sample follows:

52.167.144.54 - - [25/Oct/2024:00:13:02 +0000] "GET /robots.txt HTTP/1.1" 301 574 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/116.0.1938.76 Safari/537.36"
52.167.144.54 - - [25/Oct/2024:00:13:02 +0000] "GET /robots.txt HTTP/2.0" 200 498 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/116.0.1938.76 Safari/537.36"
52.167.144.214 - - [25/Oct/2024:00:13:11 +0000] "GET /sitemap.xml HTTP/1.1" 301 520 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/116.0.1938.76 Safari/537.36"