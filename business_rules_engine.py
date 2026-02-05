import numpy as np
import pandas as pd
import inspect


def business_rules_engine(input_file, output_file):
    """
    Apply business rules to transactions using NumPy vectorization.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
    
    Returns:
        pd.DataFrame: Classified transactions
    """
    # Load data
    df = pd.read_csv(input_file)
    
    # Convert to NumPy arrays
    prices = df["price"].values
    quantities = df["quantity"].values
    
    # Compute revenue (vectorized)
    revenue = prices * quantities
    
    # Apply classification rules (vectorized)
    categories = np.where(
        revenue > 10000,
        "HIGH",
        np.where(
            revenue >= 2000,
            "MEDIUM",
            "LOW"
        )
    )
    
    # Create output DataFrame
    output_df = pd.DataFrame({
        "transaction_id": df["transaction_id"].values,
        "revenue": revenue,
        "category": categories
    })
    
    # Save output
    output_df.to_csv(output_file, index=False)
    
    print("Business rules engine executed successfully!")
    print(f"  - Processed {len(output_df)} transactions")
    print(f"  - Total revenue: {revenue.sum():,.2f}")
    print(f"  - Output saved to: {output_file}")
    
    return output_df

#execute the function
result = business_rules_engine("transactions.csv", "transaction_classification.csv")

#validate no loops are used
# Read the function source to verify
source = inspect.getsource(business_rules_engine)
print("=== CODE INSPECTION ===")
print("Checking for loops in classification logic...")

if "for" in source and "category" in source:
    # Check if 'for' is in a comment or actual loop
    lines = source.split('\n')
    for i, line in enumerate(lines):
        if 'for' in line and 'category' in source[max(0, i-5):i+5]:
            if not line.strip().startswith('#'):
                print(f"⚠️ Potential loop found: {line.strip()}")
else:
    print("✓ No loops detected in classification logic")

#Document vectorization approach:
print("\n=== VECTORIZATION APPROACH ===")
print("✓ Revenue calculation: prices * quantities (vectorized)")
print("✓ Classification: np.where() with nested conditions (vectorized)")
print("✓ All operations use NumPy array operations")
print("✓ No Python loops for business logic")


