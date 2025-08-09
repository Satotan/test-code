# Simple EDA Tool

This repository contains a small utility that automates a few common steps of exploratory data analysis (EDA).

## Features
- Generates descriptive statistics for all columns.
- Saves histograms for numeric features.
- Creates a correlation matrix heatmap.
- Optionally produces a pair plot when there are multiple numeric features.

## Usage
1. Install dependencies:

```bash
pip install pandas seaborn matplotlib
```

2. Run the tool on a CSV file:

```bash
python eda_tool.py path/to/data.csv -o eda_output
```

The summary statistics and plots will be saved to the specified output directory.
