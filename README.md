# README

This repository contains all notebooks, scripts, and data needed to reproduce the experiments in our paper. After downloading the ZIP, extract it as-is (do not rename or move any files/folders). From the project root, you can open and run each Jupyter notebook to reproduce figures and results.

## Quick Start

### Download & Extract

- Unzip the package to a local path, unzip 'norm.tar.xz' and 'pred.tar.xz' and put them in '/data'.
- No need to change any directory or file names.

### Create Environment (Conda recommended)

```bash
conda create -n cite-env python=3.10 -y
conda activate cite-env
pip install -U pip wheel
pip install jupyterlab pandas numpy scipy matplotlib networkx python-louvain scikit-learn openpyxl tqdm
```

### Notes on data/:
```txt
data/
  
├── country_income.csv
├── norm/
│   ├── dataset/
│   │   ├── csv/
│   │   └── pkl/
│   └── metadata/
├── pred/
│   ├── dataset/
│   │   ├── csv/
│   │   └── pkl/
│   └── metadata/
├── shared_analysis.csv
├── shared_journal_papers.csv
├── similarity_matrix_30_abs_clean.csv
└── topic_period_dup_order_stats.csv
```

- Shared metadata (used by multiple notebooks) resides directly under data/ (e.g., shared_analysis.csv, shared_journal_papers.csv, topic_period_dup_order_stats.csv).
- Each dataset (norm/, pred/) contains:
  - dataset/{csv,pkl}: the main tables; PKL mirrors the CSVs for speed. Notebooks prefer PKL when present, otherwise fall back to CSV.
  - metadata/: dataset-specific artifacts (e.g., edge_list.txt, Louvain outputs under louvain/, training logs, journal stats, crossref/ISSN metadata, etc.).

### Notes on figure/:

- Contains the figures that appear in the paper. Notebooks may read from or export to this directory.

## Notebooks

- **citation_growth.ipynb** — Citation growth and temporal evolution analyses: yearly citation count trend and growth-rate comparisons.
- **citation_network.ipynb** — Citation network construction, Louvain clustering, community detection, and analysis of coordinated citation structures.
- **citation_preference.ipynb** — Citation-target preference analyses, including AI-to-AI citation tendencies and source–target composition contrasts.
- **cross_topic_citation.ipynb** — Measurement of cross-topic citation patterns using BERTopic-derived topic distances and identification of weak or cross-boundary citation links.
- **self_citation.ipynb** — Detection and quantification of self-citation behavior at the author level, with comparisons between Predatory and Normal authors.
- **collaboration_network.ipynb** — Co-authorship network construction, identification of frequent collaborators, institutional-coherence measurement, and affiliation–country homophily analyses.
- **single_repeated_authors.ipynb** — Analysis of repeated author-order motifs, single authorship paper, and comparison of templated collaboration patterns before and after the LLM era.
- **Socioeconomic.ipynb** — Author-country inference using surnames and affiliation data, income-group distributions, and socioeconomic composition comparisons.
- **temporal.ipynb** — Temporal indicators of production behavior, including yearly changes in activity, author-level output timelines, and expansion patterns.
- **topic_analysis.ipynb** — Topic modeling with BERTopic, topic-breadth classification using Gaussian mixture modeling, and quantification of author thematic consistency.
- **journal_analysis.ipynb** — Journal-level metric retrieval (e.g., h-index, i10-index, cited-by counts), quality-gap comparisons, and characterization of low-barrier or rapidly expanding venues.

All notebooks read paths relative to the project root. Keep the folder names and hierarchy intact.
To reproduce the paper’s results, you do not need to rerun some of experiments (such as API calls and clustering), they are provided for completeness and re-training if needed. Instead, the metadata is provided in the 'data/' folder, and can be directly used.

## Reproducibility & Conventions

- One-click run: unzip → create env → open notebook from repo root → “Run All”.

## Minimal Dependencies

- Python ≥ 3.10
- JupyterLab / Notebook
- pandas, numpy, scipy, matplotlib
- networkx, python-louvain
- scikit-learn
- openpyxl (for .xlsx)
- tqdm

If a package is missing at runtime, install it via:

```bash
pip install <package>
```

## License

Unless otherwise noted, the materials are provided for academic research use. For commercial use or redistribution, please contact the authors.


[![DOI](https://zenodo.org/badge/1091328274.svg)](https://doi.org/10.5281/zenodo.17547082)