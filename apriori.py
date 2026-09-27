from collections import Counter
from itertools import combinations


def find_frequent_itemsets(candidates,database,min_sup):
    """
        Find frequent k-itemsets from candidate k-itemsets
    """
    # Initialize a Counter to store the support count of each candidate item set
    frequent_itemsets = Counter()
    for candidate in candidates:
        for transaction in database:
            if set(candidate).issubset(set(transaction)):
                # Increment the support count for the candidate item set
                frequent_itemsets[candidate] += 1
    # Filter the frequent itemsets based on the minimum support threshold and return frequent itemsets
    return [item for item,support in frequent_itemsets.items() if support >= min_sup] 
def generate_candidates(frequent_itemsets):
    """
        Generate candidate k-itemsets from frequent k-1-itemsets.
    """
    candidates = []
    for l1 in frequent_itemsets:
        for l2 in frequent_itemsets:
            # Consider pairs where the first k-1 elements are the same and the last element of l1 is less than l2
            if l1[:-1] == l2[:-1] and l1[-1] < l2[-1]:
                # Join Step: Generate candidates
                # Create a candidate itemset by joining
                candidate = l1 + (l2[-1],)
                # Pruning Step: Remove unfruitful candidate
                # Check if the candidate item set has infrequent subsets (Apriori Property)
                if not has_infrequent_subset(candidate,frequent_itemsets,len(candidate)-1):
                    candidates.append(candidate)
    return candidates
def has_infrequent_subset(candidate,frequent_itemsets,k):
    """
        Check if a candidate item set has any infrequent subset of size k.
    """
    # Generate all subsets of size k from the candidate item set
    k_subsets = combinations(candidate,k)
    # Check if any subset is infrequent
    for subset in k_subsets:
        # If infrequent subset found, return True
        if not(subset in frequent_itemsets):
            return True
    # If no infrequent subset found, return False
    return False

# Read transactions from file and convert them to tuples of integers
with open("retail.dat") as file:
    transactions = [tuple(map(int, transaction.split())) for transaction in file.read().split("\n")]

# Set minimum support threshold
min_sup = 4500
# Count occurrences of 1-itemsets
candidate_1_itemsets = Counter()
for transaction in transactions:
    for item in transaction:
        candidate_1_itemsets[(item,)] += 1
# Filter the frequent 1-itemsets based on the minimum support threshold
frequent_1_itemsets = [item for (item,support) in candidate_1_itemsets.items() if support >= min_sup]

frequent_itemsets = Counter()
candidate_itemsets = []
current_frequent_itemsets = frequent_1_itemsets
k=1
# Apriori algorithm loop to find frequent item sets of increasing length
while current_frequent_itemsets != []:
   # Store frequent itemsets of current length
   frequent_itemsets[k] = current_frequent_itemsets
   # Generate candidate itemsets of next length from frequent item sets of current length
   candidate_itemsets = generate_candidates(current_frequent_itemsets)
   # Find frequent item sets of next length
   current_frequent_itemsets = find_frequent_itemsets(candidate_itemsets,transactions,min_sup)
   k += 1
frequent_itemsets = [[set(i) for i in frequent_itemsets] for frequent_itemsets in frequent_itemsets.values()]
print(frequent_itemsets)
