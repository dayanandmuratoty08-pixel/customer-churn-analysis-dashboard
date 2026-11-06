import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# Customer Churn Analysis
# -----------------------------------------

# Load dataset
file_path = "../data/customer_churn.csv"
df = pd.read_csv(file_path)

print("===== CUSTOMER CHURN ANALYSIS =====\n")

# Basic information
print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------------------
# Churn Overview
# -----------------------------------------

total_customers = len(df)

churned_customers = len(
    df[df["Churn"].astype(str).str.lower() == "yes"]
)

churn_rate = (churned_customers / total_customers) * 100

print("\n===== CHURN OVERVIEW =====")
print(f"Total Customers : {total_customers}")
print(f"Churned Customers: {churned_customers}")
print(f"Churn Rate       : {churn_rate:.2f}%")

# -----------------------------------------
# Churn by Contract Type
# -----------------------------------------

if "Contract" in df.columns:

    contract_analysis = (
        df.groupby("Contract")["Churn"]
        .apply(lambda x: (x.astype(str).str.lower() == "yes").mean() * 100)
        .round(2)
        .sort_values(ascending=False)
    )

    print("\n===== CHURN BY CONTRACT TYPE =====")
    print(contract_analysis)

# -----------------------------------------
# Churn by Gender
# -----------------------------------------

if "gender" in df.columns:

    gender_analysis = (
        df.groupby("gender")["Churn"]
        .apply(lambda x: (x.astype(str).str.lower() == "yes").mean() * 100)
        .round(2)
    )

    print("\n===== CHURN BY GENDER =====")
    print(gender_analysis)

# -----------------------------------------
# Churn by Payment Method
# -----------------------------------------

if "PaymentMethod" in df.columns:

    payment_analysis = (
        df.groupby("PaymentMethod")["Churn"]
        .apply(lambda x: (x.astype(str).str.lower() == "yes").mean() * 100)
        .round(2)
        .sort_values(ascending=False)
    )

    print("\n===== CHURN BY PAYMENT METHOD =====")
    print(payment_analysis)

# -----------------------------------------
# Average Monthly Charges
# -----------------------------------------

if "MonthlyCharges" in df.columns:

    average_charges = df.groupby("Churn")["MonthlyCharges"].mean()

    print("\n===== AVERAGE MONTHLY CHARGES =====")
    print(average_charges.round(2))

# -----------------------------------------
# Visualization
# -----------------------------------------

if "Contract" in df.columns:

    contract_analysis.plot(
        kind="bar",
        figsize=(8, 5),
        title="Customer Churn Rate by Contract Type"
    )

    plt.xlabel("Contract Type")
    plt.ylabel("Churn Rate (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig(
        "../screenshots/churn_by_contract.png",
        dpi=300
    )

    plt.show()

print("\nAnalysis completed successfully!")
