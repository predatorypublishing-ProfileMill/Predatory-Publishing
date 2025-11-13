# README

This repository contains all notebooks, scripts, and data needed to reproduce the experiments in our paper. After downloading the ZIP, extract it as-is (do not rename or move any files/folders). From the project root, you can open and run each Jupyter notebook to reproduce figures and results.

## Quick Start

### Download & Extract

- Unzip the package to a local path, put the data folder under the main directory.
- Do not change any directory or file names.

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

- **citation_growth.ipynb** — Citation growth & temporal evolution analyses and visualizations.
- **citation_network.ipynb** — Louvain Clustering, Citation network construction, topology, and community detection.
- **citation_preference.ipynb** — Citation preference/propensity metrics and comparative experiments.
- **collaboration_network.ipynb** — Collaboration network and frequently collaborated authors affiliation relation.
- **journal_analysis.ipynb** — Journal-level analyses (ISSN metrics, distributions, contributions).
- **single_repeated_authors.ipynb** — Repeated publishing and individual-level differences.
- **Socioeconomic.ipynb** — Associations with socioeconomic factors (uses country_income.csv).
- **temporal.ipynb** — Time-sliced statistics and robustness checks.
- **topic_analysis.ipynb** — Topic-level comparisons and interpretation.
- **topic_test.ipynb** — Topic method validation and auxiliary experiments.


All notebooks read paths relative to the project root. Keep the folder names and hierarchy intact.
To reproduce the paper’s results, you do not need to rerun some of experiments (such as API calls and clustering), the metadata is provided in the 'data/' folder; they are provided for completeness and re-training if needed.

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

## License`

Unless otherwise noted, the materials are provided for academic research use. For commercial use or redistribution, please contact the authors.


[![DOI](https://zenodo.org/badge/1091328274.svg)](https://doi.org/10.5281/zenodo.17547082)