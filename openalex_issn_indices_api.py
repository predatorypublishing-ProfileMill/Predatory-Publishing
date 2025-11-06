import os
import re
import time
import logging
import json
import pandas as pd
import requests

INPUT_CSV          = "/home/yuying/Documents/scholar/analysis/citation_growth/norm_with_meta.csv"
ISSN_METRICS_CSV   = "meta_data/norm_issn_metrics.csv"
CACHE_JSON         = "meta_data/norm_issn_metrics_cache.json"
MAILTO             = "yuyingli@ku.edu"

logging.basicConfig(
    filename='error.log',
    filemode='a',
    level=logging.WARNING,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

PLACEHOLDER = None

issn_pattern = re.compile(r'^\d{4}-\d{3}[\dX]$')

header = [
    "issn", "display_name", "cited_by_count", "works_count",
    "h_index", "i10_index", "mean_2yr_citedness", "is_core", "is_oa"
]
if not os.path.exists(ISSN_METRICS_CSV):
    pd.DataFrame(columns=header).to_csv(ISSN_METRICS_CSV, index=False)

if os.path.exists(CACHE_JSON):
    try:
        with open(CACHE_JSON, 'r', encoding='utf-8') as f:
            cache = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse {CACHE_JSON}: {e}, resetting cache")
        os.rename(CACHE_JSON, CACHE_JSON + ".broken")
        cache = {}
else:
    cache = {}

processed = set(cache.keys())

df = pd.read_csv(INPUT_CSV, dtype=str)
issn_series = df['issn'].dropna().str.split(',', expand=True).stack().str.strip().reset_index(drop=True)
unique_issns = issn_series.unique()

for issn in unique_issns:
    if not issn or issn == "Unknown":
        logging.warning(f"Skipping empty or Unknown ISSN")
        continue
    if not issn_pattern.match(issn):
        logging.warning(f"Invalid ISSN format: {issn}")
        continue
    if issn in processed:
        continue

    # API request
    try:
        resp = requests.get(
            "https://api.openalex.org/sources",
            params={"filter": f"issn:{issn}", "per_page": 1, "mailto": MAILTO},
            timeout=10
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
    except Exception as e:
        logging.error(f"API error for ISSN {issn}: {e}")
        continue

    if not results:
        logging.warning(f"No source found for ISSN {issn}")
        cache[issn] = None
        processed.add(issn)
        continue

    src = results[0]
    stats = src.get("summary_stats", {})

    record = {
        "issn": issn,
        "display_name": src.get("display_name"),
        "cited_by_count": src.get("cited_by_count"),
        "works_count": src.get("works_count"),
        "h_index": stats.get("h_index"),
        "i10_index": stats.get("i10_index"),
        "mean_2yr_citedness": stats.get("2yr_mean_citedness"),
        "is_core": src.get("is_core"),
        "is_oa": src.get("is_oa")
    }

    pd.DataFrame([record]).to_csv(
        ISSN_METRICS_CSV,
        mode='a',
        header=False,
        index=False
    )

    cache[issn] = record
    with open(CACHE_JSON, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

    processed.add(issn)
    time.sleep(0.2)

print(f"Completed ISSN metric fetching. Results in {ISSN_METRICS_CSV}.")
