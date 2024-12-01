import pandas as pd
from itertools import combinations
from collections import defaultdict

# Load the CSV files
general = pd.read_csv('/home/aswin/Fall-2024/DBMS/hw5/general.csv')[['university_name', 'rank']]
balanced = pd.read_csv('/home/aswin/Fall-2024/DBMS/hw5/balanced.csv')[['university_name', 'rank']]
star = pd.read_csv('/home/aswin/Fall-2024/DBMS/hw5/star.csv')[['university_name', 'rank']]
usnews = pd.read_csv('/home/aswin/Fall-2024/DBMS/hw5/usnews_university_rankings.csv')[['university_name', 'rank']][:54]

# Define a function to calculate Kendall Tau Correlation
def kendall_tau_correlation(rankings1, rankings2):
    """
    Compute Kendall Tau Correlation between two rankings.

    Args:
    rankings1: DataFrame with 'university_name' and 'rank' columns (e.g., star rankings).
    rankings2: DataFrame with 'university_name' and 'rank' columns (e.g., US News rankings).

    Returns:
    Float representing Kendall Tau Correlation.
    """
    # Create a union of universities
    universities = set(rankings1['university_name']).union(rankings2['university_name'])
    
    # Create rank dictionaries
    rank_dict1 = defaultdict(lambda: float('inf'))  # Use infinity for missing universities
    rank_dict2 = defaultdict(lambda: float('inf'))
    
    rank_dict1.update(dict(zip(rankings1['university_name'], rankings1['rank'])))
    rank_dict2.update(dict(zip(rankings2['university_name'], rankings2['rank'])))
    
    # Generate all pairs of universities
    pairs = list(combinations(universities, 2))
    
    # Count agreements and disagreements
    n_c, n_d = 0, 0
    for u1, u2 in pairs:
        rank1_u1, rank1_u2 = rank_dict1[u1], rank_dict1[u2]
        rank2_u1, rank2_u2 = rank_dict2[u1], rank_dict2[u2]
        
        # Compare rankings
        if rank1_u1 < rank1_u2 and rank2_u1 < rank2_u2:
            n_c += 1
        elif rank1_u1 > rank1_u2 and rank2_u1 > rank2_u2:
            n_c += 1
        elif rank1_u1 == rank1_u2 and rank2_u1 == rank2_u2:
            n_c += 1
        else:
            n_d += 1
    
    # Total number of pairs
    n = len(universities)
    total_pairs = n * (n - 1) / 2
    
    # Calculate Kendall Tau Correlation
    return (n_c - n_d) / total_pairs if total_pairs > 0 else 0

# Calculate Kendall Tau Correlation for each set of rankings
ktc_star = kendall_tau_correlation(star, usnews)
ktc_balanced = kendall_tau_correlation(balanced, usnews)
ktc_general = kendall_tau_correlation(general, usnews)

# Output the results
print(f"Kendall Tau Correlation (Star vs US News): {ktc_star:.3f}")
print(f"Kendall Tau Correlation (Balanced vs US News): {ktc_balanced:.3f}")
print(f"Kendall Tau Correlation (General vs US News): {ktc_general:.3f}")
