# Apriori Market Basket Analysis

A from-scratch Python implementation of the **Apriori algorithm** for mining frequent itemsets from retail transaction data. No external libraries required — just the Python standard library.

## Overview

This project applies the classic Apriori algorithm to a real-world retail transaction dataset to discover **frequent itemsets**: groups of items that are frequently purchased together. This is a foundational technique in **market basket analysis**, commonly used to power recommendation systems, product placement decisions, and cross-selling strategies.

The algorithm works iteratively:

1. Count the support (frequency) of individual items (1-itemsets) and keep those meeting the minimum support threshold.
2. Generate candidate itemsets of the next size by joining frequent itemsets from the previous step.
3. **Prune** candidates whose subsets aren't already known to be frequent (the *Apriori property*: every subset of a frequent itemset must itself be frequent).
4. Scan the transaction database to count support for the surviving candidates and filter by the minimum support threshold.
5. Repeat until no new frequent itemsets are found.

## Dataset

The script reads from `retail.dat`, a plain-text file where each line represents one transaction as space-separated item IDs.

- **Transactions:** ~88,000
- **Format:** each line = one basket, items represented as integers

The script will:
1. Load transactions from `retail.dat`
2. Mine frequent itemsets using a minimum support count of `4500` (an absolute transaction count, not a percentage — adjust based on your dataset size)
3. Print all frequent itemsets, grouped by size (1-itemsets, 2-itemsets, 3-itemsets, ...)

### Adjusting the support threshold

Edit the `min_sup` variable near the top of `apriori.py`:

```python
min_sup = 4500  # minimum number of transactions an itemset must appear in
```

Lower values will surface more (and smaller/less common) itemsets at the cost of longer runtime; higher values will be faster but more selective.

## How it works

| Function | Purpose |
|---|---|
| `find_frequent_itemsets` | Counts support for candidate itemsets against the transaction database and filters by `min_sup` |
| `generate_candidates` | Joins frequent (k-1)-itemsets into candidate k-itemsets |
| `has_infrequent_subset` | Applies the Apriori pruning property to discard candidates with any infrequent subset |

## Data

This implementation was tested against the [retail dataset](http://fimi.uantwerpen.be/data/) from the FIMI (Frequent Itemset Mining Implementations) repository, a common benchmark dataset for frequent itemset mining research. Download `retail.dat` and place it in the project root before running the script.
