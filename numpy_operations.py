
import numpy as np
import pandas as pd

def apply_vectorized_business_rules(prices, quantities):
    """
    Apply business rules using NumPy vectorization.
    """
    # Calculate revenue (vectorized)
    revenue = prices * quantities
    
    # Apply classification rules (vectorized)
    categories = np.where(
        revenue > 10000,
        "HIGH_VALUE",
        np.where(
            revenue >= 2000,
            "MEDIUM_VALUE",
            "LOW_VALUE"
        )
    )
    
    # Create DataFrame
    results_df = pd.DataFrame({
        "price": prices,
        "quantity": quantities,
        "revenue": revenue,
        "category": categories
    })
    
    # Save results
    results_df.to_csv("numpy_revenue_analysis.csv", index=False)
    
    print("Vectorized business rules applied successfully!")
    print(f"  Total revenue: {revenue.sum():,.2f}")
    print(f"  Categories: {len(np.unique(categories))} unique values")
    
    return results_df

# execute the fuction 
prices = np.array([1500, 500, 12000, 1500, 12000])
quantities = np.array([2, 5, 1, 1, 2])

results = apply_vectorized_business_rules(prices, quantities)

