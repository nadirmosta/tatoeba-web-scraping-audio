## Tatoeba Audio Downloader for Anki Cards (Web scraping)
# Description
This Python script allows you to scrape audio files from the Tatoeba website and download them to create Anki flashcards with audio. The script automates the process of fetching audio recordings for sentences from different languages, making it easier to enhance your language learning experience on Anki.

# how to use this script
to use this you have to install these libraries :
## installation
```bash
pip install selenium
```
```bash
pip install bs4
```
```bash
pip install requests
```
## usage
to download the audios from the Tatoeba site, choose the language you want to  and copy the URL to the script  
```python
url = 'https://tatoeba.org/en/audio/index?page='
```
and modify the path where you want to download your audio
```python
paths = 'type here the path of the folder you want to download the audio into'
```
example :
```python
paths = 'C:\Users\ASUS\Desktop\audios'
```
and here choose how many pages you want to download (from which page to which page). 
as an example here 
```python
for pages in range (1,12):
```
from pages 1 to 12 the audio of the language is going to be downloaded when you run the script.
### references 
[how to scrape multiple web pages](https://www.geeksforgeeks.org/how-to-scrape-multiple-pages-of-a-website-using-python/)

[download audio from webpage using web scraping](https://stackoverflow.com/questions/59539194/how-to-download-all-mp3-url-as-mp3-from-a-webpage-using-python3)
