import os
import glob
import pandas as pd
import numpy as np

#map user
'''df = pd.read_csv("master_map_user.csv")

print(df.head())

print(df.shape)

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print(df.columns)

print(df.isnull().sum())
df = df.dropna(
    subset=[
        "states",
        "year",
        "quarter",
        "district",
        "registered_user_counts"
    ]
)
print("Before:", df.shape)

df = df.drop_duplicates()

print("After:", df.shape)
df["states"] = (
    df["states"]
    .str.strip()
    .str.replace("-&-", " and ", regex=False)
    .str.replace("-", " ", regex=False)
    .str.title()
)

df["district"] = (
    df["district"]
    .str.strip()
    .str.title()
)

print(df[["states", "district"]].head())
df["year"] = pd.to_numeric(
    df["year"], errors="coerce"
)

df["quarter"] = pd.to_numeric(
    df["quarter"], errors="coerce"
)

df["registered_user_counts"] = pd.to_numeric(
    df["registered_user_counts"], errors="coerce"
)
df = df.dropna(
    subset=["year", "quarter", "registered_user_counts"]
)

df = df[
    (df["year"] > 0) &
    (df["quarter"].between(1, 4)) &
    (df["registered_user_counts"] >= 0)
]
df.to_csv(
    "cleaned_master_map_user.csv",
    index=False
)

print("Data cleaning completed successfully!")

print(df.head())

print(df.shape)

# =====================================
# STAGE 3: DATA TRANSFORMATION
# =====================================

# Read the cleaned dataset
df = pd.read_csv("cleaned_master_map_user.csv")

print("Before Transformation:")
print(df.head())
print(df.shape)

#Create Year-Quarter column

df["year_quarter"] = (
    df["year"].astype(str)
    + "-Q"
    + df["quarter"].astype(str)
)
#Create Quarter Name

df["quarter_name"] = "Q" + df["quarter"].astype(str)


#Create Quarter Start Date

df["quarter_start_date"] = pd.to_datetime(
    df["year"].astype(str) + "-" +
    (((df["quarter"] - 1) * 3) + 1).astype(str) +
    "-01"
)



# Create User Count Category

df["user_count_category"] = pd.cut(
    df["registered_user_counts"],
    bins=[-1, 10000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)

#Create State-District column

df["state_district"] = (
    df["states"] + " - " + df["district"]
)



# Display transformed data

print("\nTransformed Dataset:")
print(df.head(10))

print("\nNew Columns:")
print(df.columns.tolist())


#Save transformed dataset

df.to_csv(
    "transformed_master_map_user.csv",
    index=False
)

print("\nData transformation completed successfully!")'''



#map transaction
'''df = pd.read_csv("master_map_transaction.csv")

print(df.head())

print(df.shape)

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print(df.columns)

print(df.isnull().sum())
df = df.dropna(
    subset=[
        "states",
        "year",
        "quarter",
        "district",
        "trans_counts",
        "amount"
    ]
)
print("Before:", df.shape)

df = df.drop_duplicates()

print("After:", df.shape)
df["states"] = (
    df["states"]
    .str.strip()
    .str.replace("-&-", " and ", regex=False)
    .str.replace("-", " ", regex=False)
    .str.title()
)

df["district"] = (
    df["district"]
    .str.strip()
    .str.title()
)

print(df[["states", "district"]].head())
df["year"] = pd.to_numeric(
    df["year"], errors="coerce"
)

df["quarter"] = pd.to_numeric(
    df["quarter"], errors="coerce"
)

df["trans_counts"] = pd.to_numeric(
    df["trans_counts"], errors="coerce"
)
df = df.dropna(
    subset=["year", "quarter", "trans_counts"]
)

df = df[
    (df["year"] > 0) &
    (df["quarter"].between(1, 4)) &
    (df["trans_counts"] >= 0)
]

print(df["amount"].dtype)
print(df["amount"].isnull().sum())
print(df["amount"].describe())

df["amount"] = pd.to_numeric(
    df["amount"], errors="coerce")

print("Missing values:", df["amount"].isnull().sum())

print("Negative amounts:", (df["amount"] < 0).sum())

pd.set_option("display.float_format", "{:,.2f}".format)

print(df["amount"].head(30))

df.to_csv(
    "cleaned_master_map_transaction.csv",
    index=False
)

print("Data cleaning completed successfully!")

print(df.head())

print(df.shape)


# =====================================
# STAGE 3: DATA TRANSFORMATION
# =====================================

# Read the cleaned dataset
df = pd.read_csv("cleaned_master_map_transaction.csv")

print("Before Transformation:")
print(df.head())
print(df.shape)

#Create Year-Quarter column

df["year_quarter"] = (
    df["year"].astype(str)
    + "-Q"
    + df["quarter"].astype(str)
)
#Create Quarter Name

df["quarter_name"] = "Q" + df["quarter"].astype(str)


#Create Quarter Start Date

df["quarter_start_date"] = pd.to_datetime(
    df["year"].astype(str) + "-" +
    (((df["quarter"] - 1) * 3) + 1).astype(str) +
    "-01"
)



# Create User Count Category

df["trans_count_category"] = pd.cut(
    df["trans_counts"],
    bins=[-1, 10000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)

#Create State-District column

df["state_district"] = (
    df["states"] + " - " + df["district"]
)

df["amount_in_lakhs"] = df["amount"] / 100000

#Convert amount into crores
df["amount_in_crores"] = df["amount"] / 10000000
#Calculate average transaction value
df["average_transaction_value"] = (
    df["amount"] / df["trans_counts"].replace(0, float("nan"))
)


# Display transformed data

print("\nTransformed Dataset:")
print(df.head(10))

print("\nNew Columns:")
print(df.columns.tolist())


#Save transformed dataset

df.to_csv(
    "transformed_master_map_transaction.csv",
    index=False
)

print("\nData transformation completed successfully!")'''




#aggregated transaction
'''df = pd.read_csv("master_aggregated_transaction.csv")

print(df.head())

print(df.shape)

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print(df.columns)

print(df.isnull().sum())
df = df.dropna(
    subset=[
        "states",
        "year",
        "quarter",
        "trans_type",
        "trans_counts",
        "amount"
    ]
)
print("Before:", df.shape)

df = df.drop_duplicates()

print("After:", df.shape)
df["states"] = (
    df["states"]
    .str.strip()
    .str.replace("-&-", " and ", regex=False)
    .str.replace("-", " ", regex=False)
    .str.title()
)

print(df[["states"]].head())
df["year"] = pd.to_numeric(
    df["year"], errors="coerce"
)

df["quarter"] = pd.to_numeric(
    df["quarter"], errors="coerce"
)

df["trans_counts"] = pd.to_numeric(
    df["trans_counts"], errors="coerce"
)
df = df.dropna(
    subset=["year", "quarter", "trans_counts"]
)

df = df[
    (df["year"] > 0) &
    (df["quarter"].between(1, 4)) &
    (df["trans_counts"] >= 0)
]

print(df["amount"].dtype)
print(df["amount"].isnull().sum())
print(df["amount"].describe())

df["amount"] = pd.to_numeric(
    df["amount"], errors="coerce")

print("Missing values:", df["amount"].isnull().sum())

print("Negative amounts:", (df["amount"] < 0).sum())

pd.set_option("display.float_format", "{:,.2f}".format)

print(df["amount"].head(30))

df.to_csv(
    "cleaned_master_aggregated_transaction.csv",
    index=False
)

print("Data cleaning completed successfully!")

print(df.head())

print(df.shape)

# =====================================
# STAGE 3: DATA TRANSFORMATION
# =====================================


# Read the cleaned dataset
df = pd.read_csv("cleaned_master_aggregated_transaction.csv")

print("Before Transformation:")
print(df.head())
print(df.shape)

#Create Year-Quarter column

df["year_quarter"] = (
    df["year"].astype(str)
    + "-Q"
    + df["quarter"].astype(str)
)
#Create Quarter Name

df["quarter_name"] = "Q" + df["quarter"].astype(str)


#Create Quarter Start Date

df["quarter_start_date"] = pd.to_datetime(
    df["year"].astype(str) + "-" +
    (((df["quarter"] - 1) * 3) + 1).astype(str) +
    "-01"
)



# Create User Count Category

df["trans_count_category"] = pd.cut(
    df["trans_counts"],
    bins=[-1, 10000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)



df["amount_in_lakhs"] = df["amount"] / 100000

#Convert amount into crores
df["amount_in_crores"] = df["amount"] / 10000000
#Calculate average transaction value
df["average_transaction_value"] = (
    df["amount"] / df["trans_counts"].replace(0, float("nan"))
)

# 1. Standardize transaction type
df["trans_type"] = (
    df["trans_type"]
    .str.strip()
    .str.title()
)

# 2. Create short category names
category_mapping = {
    "Recharge & Bill Payments": "Recharge & Bills",
    "Peer-To-Peer Payments": "Peer-to-Peer",
    "Merchant Payments": "Merchant",
    "Financial Services": "Financial Services",
    "Others": "Others"
}

df["trans_category"] = df["trans_type"].map(category_mapping)

# 3. Create transaction category codes
code_mapping = {
    "Recharge & Bill Payments": "TT01",
    "Peer-To-Peer Payments": "TT02",
    "Merchant Payments": "TT03",
    "Financial Services": "TT04",
    "Others": "TT05"
}

df["trans_type_code"] = df["trans_type"].map(code_mapping)

# 4. Create broader transaction groups
group_mapping = {
    "Recharge & Bill Payments": "Payments",
    "Peer-To-Peer Payments": "Payments",
    "Merchant Payments": "Payments",
    "Financial Services": "Financial Services",
    "Others": "Others"
}

df["trans_group"] = df["trans_type"].map(group_mapping)

# Display transformed data

print("\nTransformed Dataset:")
print(df.head(10))

print("\nNew Columns:")
print(df.columns.tolist())


#Save transformed dataset

df.to_csv(
    "transformed_master_aggregated_transaction.csv",
    index=False
)

print("\nData transformation completed successfully!")'''






#aggregated user
df = pd.read_csv("master_aggregated_user.csv")

print(df.head())

print(df.shape)

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print(df.columns)

print(df.isnull().sum())
df = df.dropna(
    subset=[
        "states",
        "year",
        "quarter",
        "brand",
        "user_counts",
        "percentage"
    ]
)
print("Before:", df.shape)

df = df.drop_duplicates()

print("After:", df.shape)
df["states"] = (
    df["states"]
    .str.strip()
    .str.replace("-&-", " and ", regex=False)
    .str.replace("-", " ", regex=False)
    .str.title()
)
df["brand"] = df["brand"].str.strip()

print(df[["states"]].head())
df["year"] = pd.to_numeric(
    df["year"], errors="coerce"
)

df["quarter"] = pd.to_numeric(
    df["quarter"], errors="coerce"
)

df["user_counts"] = pd.to_numeric(
    df["user_counts"], errors="coerce"
)

df["percentage"] = pd.to_numeric(
    df["percentage"], errors="coerce"
)

df = df.dropna(
    subset=["year", "quarter", "user_counts", "percentage"]
)

df = df[
    (df["year"] > 0) &
    (df["quarter"].between(1, 4)) &
    (df["user_counts"] >= 0)&
    (df["percentage"].between(0,1))
]

df["year"] = df["year"].astype(int)
df["quarter"] = df["quarter"].astype(int)
df["user_counts"] = df["user_counts"].astype(int)

df["year_quarter"] = (
    df["year"].astype(str) +
    "-Q" +
    df["quarter"].astype(str)
)

print("Final missing values:")
print(df.isnull().sum())

print("Final shape:", df.shape)

print(df.head(10))

df.to_csv(
    "cleaned_master_aggregated_user.csv",
    index=False
)

print("Data cleaning completed successfully!")

print(df.head())

print(df.shape)


# =====================================
# STAGE 3: DATA TRANSFORMATION
# =====================================


import pandas as pd
import os

# Read your cleaned user CSV file
df = pd.read_csv("cleaned_master_aggregated_user.csv")

# Create calculated fields
df["year_quarter"] = (
    df["year"].astype(str) + "-Q" +
    df["quarter"].astype(str)
)

df["quarter_name"] = "Q" + df["quarter"].astype(str)

df["quarter_start_date"] = pd.to_datetime(
    df["year"].astype(str) + "-" +
    (((df["quarter"] - 1) * 3) + 1).astype(str) +
    "-01"
)

df["percentage_display"] = df["percentage"] * 100

df["user_count_category"] = pd.cut(
    df["user_counts"],
    bins=[-1, 10000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)

df["brand_category"] = df["brand"].str.title()

# Save the transformed file
df.to_csv("transformed_aggregated_user.csv", index=False)

print("Transformation completed!")
print("File saved at:", os.path.abspath(
    "transformed_aggregated_user.csv"
))
print(df.head())




#top transaction
'''df = pd.read_csv("master_top_transaction.csv")

print(df.head())

print(df.shape)

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print(df.columns)

print(df.isnull().sum())
df = df.dropna(
    subset=[
        "states",
        "year",
        "quarter",
        "district",
        "trans_counts",
        "amount"
    ]
)
print("Before:", df.shape)

df = df.drop_duplicates()

print("After:", df.shape)
df["states"] = (
    df["states"]
    .str.strip()
    .str.replace("-&-", " and ", regex=False)
    .str.replace("-", " ", regex=False)
    .str.title()
)

df["district"] = (
    df["district"]
    .str.strip()
    .str.title()
)

print(df[["states", "district"]].head())
df["year"] = pd.to_numeric(
    df["year"], errors="coerce"
)

df["quarter"] = pd.to_numeric(
    df["quarter"], errors="coerce"
)

df["trans_counts"] = pd.to_numeric(
    df["trans_counts"], errors="coerce"
)
df = df.dropna(
    subset=["year", "quarter", "trans_counts"]
)

df = df[
    (df["year"] > 0) &
    (df["quarter"].between(1, 4)) &
    (df["trans_counts"] >= 0)   
]

print(df["amount"].dtype)
print(df["amount"].isnull().sum())
print(df["amount"].describe())

df["amount"] = pd.to_numeric(
    df["amount"], errors="coerce")

print("Missing values:", df["amount"].isnull().sum())

print("Negative amounts:", (df["amount"] < 0).sum())

pd.set_option("display.float_format", "{:,.2f}".format)

print(df["amount"].head(30))


df.to_csv(
    "cleaned_master_top_transaction.csv",
    index=False
)

print("Data cleaning completed successfully!")

print(df.head())

print(df.shape)


# =====================================
# STAGE 3: DATA TRANSFORMATION
# =====================================


# Read the cleaned dataset
df = pd.read_csv("cleaned_master_top_transaction.csv")

print("Before Transformation:")
print(df.head())
print(df.shape)

#Create Year-Quarter column

df["year_quarter"] = (
    df["year"].astype(str)
    + "-Q"
    + df["quarter"].astype(str)
)
#Create Quarter Name

df["quarter_name"] = "Q" + df["quarter"].astype(str)


#Create Quarter Start Date

df["quarter_start_date"] = pd.to_datetime(
    df["year"].astype(str) + "-" +
    (((df["quarter"] - 1) * 3) + 1).astype(str) +
    "-01"
)



# Create User Count Category

df["trans_count_category"] = pd.cut(
    df["trans_counts"],
    bins=[-1, 10000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)

#Create State-District column

df["state_district"] = (
    df["states"] + " - " + df["district"]
)

df["amount_in_lakhs"] = df["amount"] / 100000

#Convert amount into crores
df["amount_in_crores"] = df["amount"] / 10000000
#Calculate average transaction value
df["average_transaction_value"] = (
    df["amount"] / df["trans_counts"].replace(0, float("nan"))
)


# Display transformed data

print("\nTransformed Dataset:")
print(df.head(10))

print("\nNew Columns:")
print(df.columns.tolist())


#Save transformed dataset

df.to_csv(
    "transformed_master_top_transaction.csv",
    index=False
)

print("\nData transformation completed successfully!")'''



#top map
'''df = pd.read_csv("master_top_user.csv")

print(df.head())

print(df.shape)

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print(df.columns)

print(df.isnull().sum())
df = df.dropna(
    subset=[
        "states",
        "year",
        "quarter",
        "district",
        "registered_user_counts"
    ]
)
print("Before:", df.shape)

df = df.drop_duplicates()

print("After:", df.shape)
df["states"] = (
    df["states"]
    .str.strip()
    .str.replace("-&-", " and ", regex=False)
    .str.replace("-", " ", regex=False)
    .str.title()
)

df["district"] = (
    df["district"]
    .str.strip()
    .str.title()
)


print(df[["states", "district"]].head())
df["year"] = pd.to_numeric(
    df["year"], errors="coerce"
)

df["quarter"] = pd.to_numeric(
    df["quarter"], errors="coerce"
)

df["registered_user_counts"] = pd.to_numeric(
    df["registered_user_counts"], errors="coerce"
)


df = df.dropna(
    subset=["year", "quarter", "registered_user_counts"]
)

df = df[
    (df["year"] > 0) &
    (df["quarter"].between(1, 4)) &
    (df["registered_user_counts"] >= 0)
]



print("Final missing values:")
print(df.isnull().sum())

print("Final shape:", df.shape)

print(df.head(10))

df.to_csv(
    "cleaned_master_top_user.csv",
    index=False
)

print("Data cleaning completed successfully!")

print(df.head())

print(df.shape)



# =====================================
# STAGE 3: DATA TRANSFORMATION
# =====================================


# Read the cleaned dataset
df = pd.read_csv("cleaned_master_top_user.csv")

print("Before Transformation:")
print(df.head())
print(df.shape)

#Create Year-Quarter column

df["year_quarter"] = (
    df["year"].astype(str)
    + "-Q"
    + df["quarter"].astype(str)
)
#Create Quarter Name

df["quarter_name"] = "Q" + df["quarter"].astype(str)


#Create Quarter Start Date

df["quarter_start_date"] = pd.to_datetime(
    df["year"].astype(str) + "-" +
    (((df["quarter"] - 1) * 3) + 1).astype(str) +
    "-01"
)



# Create User Count Category

df["registered_count_category"] = pd.cut(
    df["registered_user_counts"],
    bins=[-1, 10000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)

#Create State-District column

df["state_district"] = (
    df["states"] + " - " + df["district"]
)




# Display transformed data

print("\nTransformed Dataset:")
print(df.head(10))

print("\nNew Columns:")
print(df.columns.tolist())


#Save transformed dataset

df.to_csv(
    "transformed_master_top_user.csv",
    index=False
)

print("\nData transformation completed successfully!")'''



