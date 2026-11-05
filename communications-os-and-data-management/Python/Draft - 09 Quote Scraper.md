# Draft 09 - Quote Scraper

**Status:** Draft - needs review  
**Source prompt:** Homework 2.pdf and introduction notebook.

## Goal

Fetch the Quotes to Scrape practice page, parse quote text, and save it to a text file.

## Work through these steps in order

1. Install/import only the packages needed for the assignment.
2. Request the practice page with a timeout and check the HTTP status.
3. Parse the returned HTML and select the quote text elements.
4. Write results to a fresh UTF-8 text file with a context manager.
5. Run twice and confirm the file does not accumulate accidental duplicate output.

## Completion checklist

- [ ] Request has a timeout.
- [ ] HTTP failure is handled visibly.
- [ ] Only intended text is extracted.
- [ ] Output is saved using safe file handling.
- [ ] Site terms and reasonable request rates are respected.

## Current evidence

A scraping example exists in the supplied PDF, but it has duplicate imports, does not show robust request handling, and is not verified.

## Submission note

Follow the exact requirements in the original course prompt. Historical due dates shown in the supplied material are from 2022. Do not include private identifiers in a portfolio copy unless the course submission specifically requires them.
