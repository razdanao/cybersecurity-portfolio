# Python for Security Tooling: Web Scraping and Core Programming Habits

## Platform
Coursework exercises — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Programming for Cybersecurity). Tools: Python, Jupyter, `requests`, BeautifulSoup, pandas.

## Goal
To practice the Python skills that security tooling is built on: pulling data from a web page, handling input safely, and understanding how Python stores data in memory. Scripts that fetch, parse, and check things automatically are the basis of reconnaissance, OSINT, and monitoring work.

## Part 1: Web Scraping with requests and BeautifulSoup

### The setup
I scraped **quotes.toscrape.com**, a site built specifically for scraping practice. `requests` downloads the page, and BeautifulSoup parses the HTML into a structure I can search.

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
```

### Three tasks
1. **Parse the page and inspect its structure.** Searching for the `<head>` tag returned the page's metadata, including the title "Quotes to Scrape", which confirmed the page had parsed correctly.
2. **Extract only the quotes.** Each quote's text sits in a `<span class="text">` element, so I searched for those and saved them to a text file.
   ```python
   for span in soup.find_all("span", class_="text"):
       print(span.text)
   ```
3. **Strip out the HTML and keep only the text.** `soup.get_text()` removes every tag and returns the page's visible text.

### Going further: structured data
Beyond the plain text, I collected each quote's **author, tags, and author-page link** into a table and exported it. The result was a 100-row table covering every quote on the site, saved as a CSV file.

<img width="1134" height="729" alt="py-scraper-dataframe-100-quotes" src="https://github.com/user-attachments/assets/9390e6e5-607f-4663-b2c6-e0a577ceec8c" />

<img width="1031" height="460" alt="py-scraper-csv-export" src="https://github.com/user-attachments/assets/c160ef12-ec40-4c70-8a34-b12040ff6d63" />

### What I'd improve
- **Open the output file once, not once per quote.** My loop reopened the file in append mode for every quote, which is slow, and running the cell twice silently duplicated the data. Opening it once, in write mode, fixes both.
- **`get_text()` keeps the page furniture.** Navigation links and sidebar text come through along with the quotes, so it's useful for a quick look but not for clean data.
- **Know your parser.** I used the `lxml` parser, which has to be installed separately. Python's built-in `html.parser` has no extra dependency.

### Scraping: ethics and legality
This site exists to be scraped, so there was no risk. Real sites are different: scraping can violate a site's terms of service, put load on its servers, or collect personal data. Before scraping anything real I'd check its `robots.txt` and terms, rate-limit my requests, and avoid anything behind a login or containing personal information. It's the same principle as my Wireshark exercise: a legal tool becomes a problem when used without authorization.

## Part 2: Control Flow and Boundary Testing

I wrote a grade classifier that reads a mark and prints a category: 90 and above is "excellent", 75 to 89 is "good", 40 to 74 is "average", and below 40 is "fail". To test it I used values on and around the boundaries.

<img width="1115" height="506" alt="py-grade-classifier-boundary-tests" src="https://github.com/user-attachments/assets/a75edd02-2834-4e81-b049-8ed0f47b9ab7" />

Testing the edges (90, 40, and 39) matters most, because that's where off-by-one mistakes hide. But the script had weaknesses I'd fix on review:
- **It never stops.** `while True` has no way out.
- **It crashes on bad input.** Typing letters instead of a number raises an error, and marks like 101 or -5 are accepted.

A more robust version:

```python
while True:
    raw = input("enter mark (q to quit): ")
    if raw.lower() == "q":
        break
    try:
        mark = int(raw)
    except ValueError:
        print("Please enter a whole number.")
        continue
    if not 0 <= mark <= 100:
        print("Mark must be between 0 and 100.")
    elif mark >= 90:
        print("excellent")
    elif mark >= 75:
        print("good")
    elif mark >= 40:
        print("average")
    else:
        print("fail")
```

I ran this version against 90, 89, 75, 74, 40, 39, "abc", 101, and -5, and every case behaved as expected. Validating input before using it is the same habit that prevents entire classes of security bugs, including injection.

## Part 3: Copies vs. References

Appending a list to another list doesn't copy it; it stores a *reference* to the same list. Change the original in place and the stored entry changes too. `copy.deepcopy()` stores an independent snapshot instead.

```python
import copy

a = [1, 8, 10]
b = []
b.append(a)            # stores a reference
a[0] = 0               # change the original in place
print(b)               # [[0, 8, 10]]  <- the stored entry changed too

b = []
a = [1, 8, 10]
b.append(copy.deepcopy(a))   # stores an independent copy
a[0] = 0
print(b)               # [[1, 8, 10]]  <- unaffected
```

<img width="1147" height="497" alt="py-list-copy-vs-reference" src="https://github.com/user-attachments/assets/dc3759ff-79bf-4ad9-8300-4910f0900f68" />

This kind of unintended shared state is a common source of subtle bugs, the kind that are hard to spot in logs and tests.

## Key Takeaways
- **Scraping is automation of reconnaissance.** The same fetch-and-parse pattern powers OSINT gathering, and knowing how it works also helps a defender understand what rate limiting and bot detection are for.
- **Test the boundaries, then test the nonsense.** Edge values catch logic errors; bad input catches the assumptions I forgot I was making.
- **Reviewing my own code found more than writing it did.** Every improvement above came from rereading finished code with a security mindset.
