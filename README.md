# Zillow Listings to Google Form Automation

A Python bot that scrapes rental listings (address, price, link) from a Zillow clone site and enters each one into a Google Form, which collects them in a Google Sheet.

![Demo](/docs/demo.gif)
<!-- TODO: add a short GIF of the bot filling in the form, plus the finished Google Sheet with correct columns -->

## Features

- Scrapes the address, monthly price and link for every listing on the page using BeautifulSoup
- Keeps the three fields lined up by looping through them together with `zip()`
- Fills in and submits the Google Form once per listing using Selenium
- Form responses collect automatically in a linked Google Sheet

## Tech stack

- Python 3
- BeautifulSoup (scraping)
- Selenium (browser automation)
- Google Forms and Google Sheets (data collection)

## How to run

1. Clone the repo and move into it:
```
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
```
2. Install the requirements:
```
   pip install -r requirements.txt
```
3. Create a `.env` file in the project folder (see `.env.example`):
```
   FORM_URL=<your-google-form-link>
```
4. Run the script (Chrome must be installed):
```
   python main.py
```

The form needs three short-answer questions: address, price per month, and link.

## About this project

This was a capstone from a Python course. The course supplied the task and the cloned listing site (`appbrewery.github.io/Zillow-Clone`). I wrote the solution myself from my own TODO list, inspecting the page to choose elements, and did not follow a walkthrough.

## What I learned / challenges

- **XPath scoping (`//` vs `.//`):** Filling in the form failed unpredictably with `NoSuchElementException`. When it did run, all three answers went into the first input. The cause was that `//` searches the whole page, while `.//` searches only inside the element I'm working from. Reading the XPath documentation fixed it.
- **Swapped columns from `zip()`:** I changed the loop variables so the address came before the link, but forgot to reorder the arguments to `zip()`. The sheet showed addresses and links in the wrong columns. I deleted the bad rows, fixed the order, and re-ran.
- **Takeaway:** Reading the documentation properly would have saved me hours of trial and error.

## Possible next improvements

- Add proper error handling and explicit waits, so one missing element doesn't crash the run
- Clean up prices into one consistent format before submitting