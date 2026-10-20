"""Minimal example: run the jobware-scraper Actor and print the results.

Usage: APIFY_TOKEN=... python run.py   (pip install apify-client)
"""
import os
import sys

from apify_client import ApifyClient

token = os.environ.get("APIFY_TOKEN")
if not token:
    sys.exit("Set the APIFY_TOKEN environment variable first.")

client = ApifyClient(token)

run_input = {
    "keywords": "entwickler",
    "location": "Berlin",
    "maxItems": 50,
}

run = client.actor("bibian/jobware-scraper").call(run_input=run_input)

count = 0
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    count += 1
    salary_min = item.get("salaryMin")
    salary_max = item.get("salaryMax")
    currency = item.get("salaryCurrency") or ""
    print(f"{item['title']} | {item.get('companyName')} | {item.get('city')} | {salary_min}-{salary_max} {currency}")
print(f"{count} results")
