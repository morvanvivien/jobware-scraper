# How to Scrape Jobware.de: German Jobs, Company & Salary Data

> **Run it now, no code: [jobware-scraper on the Apify Store](https://apify.com/bibian/jobware-scraper)** &nbsp;|&nbsp; $2.00 per 1,000 postings &nbsp;|&nbsp; no login, no browser needed

Jobware is a major German job board with over 300,000 live postings across every occupation. It has no public export and no official API for third parties. This guide shows how to get its postings as clean structured data — title, company, location, employment type, salary estimate and full description — with a free Apify Actor, from the console or from code.

Searches this page answers: jobware scraper, German jobs scraper, jobware.de job postings, German salary data scraper.

## What you get from the Jobware scraper

- Every live posting, with title, hiring company, city, region and employment type.
- A `remote` flag and a salary estimate (`salaryMin`, `salaryMax`, `salaryCurrency`) pre-parsed from the posting's own structured data.
- Publication and expiry dates as published by the site.
- Full job description as plain text, with any named recruiter's signature, e-mail or direct phone number removed.

Export the dataset as JSON, CSV or Excel, or read it through the Apify API. A real sample (five results, personal data removed) is in [`sample-output.json`](sample-output.json).

## Output fields

| Field | What it is |
|---|---|
| `id`, `url` | Stable numeric id and the canonical posting URL on jobware.de |
| `title` | Job title as published |
| `companyName`, `companyUrl` | Hiring company (including recruitment agencies when the employer uses one) and its own website |
| `city`, `postalCode`, `region` | Work location |
| `remote` | `true` when the posting is flagged as remote-friendly |
| `employmentType` | schema.org value, for example `FULL_TIME` or `PART_TIME` |
| `salaryMin`, `salaryMax`, `salaryPeriod`, `salaryCurrency` | Pay range from the posting's own structured data, empty when the posting carries none |
| `datePosted`, `validThrough` | Publication and expiry dates |
| `description` | Full job description as plain text |

## Use cases

- **Monitor the German job market.** New postings by job title, location or both, across every occupation.
- **Feed a job alert or an aggregator.** Run it daily and get the newest postings, deduplicated by their stable numeric `id`.
- **Find companies that are hiring.** See which employers recruit for a given role right now, with city, region and the company's own website.
- **Screen for salary and remote work.** Salary estimate and a `remote` flag come pre-parsed instead of a block of free text to re-read yourself.

## Input

| Field | What it does |
|---|---|
| `keywords` | Job title or skill, for example `entwickler` or `pflege`. Leave empty to get postings across every occupation. |
| `location` | City or German state (`Bundesland`), for example `Berlin` or `Bayern`. Leave empty for all of Germany. |
| `maxItems` | The run stops once this many postings are saved (default 50). |

Example input:

```json
{
  "keywords": "entwickler",
  "location": "Berlin",
  "maxItems": 50
}
```

## Three ways to use it

### 1. Apify console, no code

1. Open [the Actor page](https://apify.com/bibian/jobware-scraper) and click **Try for free** (a free Apify account is enough).
2. Fill in the input form (keywords, location and the maximum number of results) and click **Start**.
3. When the run finishes, open the **Output** tab, check the table, then **Export** as CSV, Excel or JSON.
4. For a daily alert, open **Schedules**, create a daily schedule for the Actor and, optionally, add an integration that sends new results to Slack, e-mail or Google Sheets.

### 2. Apify API with JavaScript

```bash
npm install apify-client
export APIFY_TOKEN="your token from Apify console, Settings, Integrations"
node examples/run.js
```

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('bibian/jobware-scraper').call({
  keywords: 'entwickler',
  location: 'Berlin',
  maxItems: 50,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
```

The complete file is [`examples/run.js`](examples/run.js) (ES module, Node 18 or later).

### 3. Apify API with Python

```bash
pip install apify-client
export APIFY_TOKEN="your token from Apify console, Settings, Integrations"
python examples/run.py
```

```python
from apify_client import ApifyClient

client = ApifyClient(token="<APIFY_TOKEN>")
run = client.actor("bibian/jobware-scraper").call(run_input={
    "keywords": "entwickler",
    "location": "Berlin",
    "maxItems": 50
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
```

The complete file is [`examples/run.py`](examples/run.py). Never put your token in the code: read it from the `APIFY_TOKEN` environment variable as above.

## Pricing

Pay per result: **$2.00 per 1,000 postings**, plus a tiny start fee of $0.00005 per run. For example, 100 postings cost about $0.20. You only pay for the postings you receive, and platform usage is included in that price. Prices are those shown on the [Store page](https://apify.com/bibian/jobware-scraper) when this guide was written; the Store page is the reference.

## Limits and honest notes

- **Salary is Jobware's own estimate, not always the employer's figure.** Jobware fills in a `baseSalary` on most postings to satisfy Google's job-schema requirements, even when the employer never disclosed a real number. Treat `salaryMin`/`salaryMax` as a market estimate, not a confirmed offer.
- Some postings omit salary or a precise city; the matching fields are then empty rather than guessed.
- No browser and no proxy needed: a plain HTTP request reads every page, so runs are fast and cheap.
- The dataset contains job postings only. Any line that carries a named recruiter's signature, e-mail or direct phone number is removed from the description before it is saved; the hiring company's own name, address and application e-mail are kept only when they are not tied to a named individual.
- This is an unofficial tool, not affiliated with Jobware. Check the site terms and the data protection rules that apply to your use.

## FAQ

**Do I need an account, cookies or a proxy for jobware.de?**
No. The Actor reads publicly visible pages only.

**How do I get only the new postings every day?**
Save a task and schedule it daily with Apify Schedules. Deduplicate on the `id` field if you keep your own copy.

**Which formats can I export?**
JSON, CSV, Excel, XML, HTML table or RSS, from the dataset page or through the API.

**Can I filter by city and job title together?**
Yes, set `keywords` and `location` in the same run to target a role in a specific city or region.

**Is it legal to scrape?**
The actor collects publicly visible postings and respects the robots.txt rules of the site. How you use the data is your responsibility: check the site's terms and the laws that apply to you, for example the GDPR.

## Try it

**[Open jobware-scraper on the Apify Store](https://apify.com/bibian/jobware-scraper)**

The code in `examples/` is released under the MIT license (see [LICENSE](LICENSE)). The data belongs to its original publishers.
