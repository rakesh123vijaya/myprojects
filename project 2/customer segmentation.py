import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================
# Import Data
# =====================================

df = pd.read_csv("retail_customer_segmentation.csv")

print(df.head())
print(df.info())

# =====================================
# Data Cleaning
# =====================================

print(df.isnull().sum())

df.dropna(inplace=True)
df.drop_duplicates(subset=['customer_id'], inplace=True)

print("Dataset Shape:", df.shape)

# =====================================
# EDA - Age Distribution
# =====================================

# Create age groups
df['Age_Group'] = pd.cut(
    df['age'],
    bins=[18, 25, 35, 45, 55, 65, 100],
    labels=['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
)

# Count customers in each age group
df['Age_Group'].value_counts().sort_index().plot(kind='bar')

plt.title('Customers by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers')
plt.show()


# =====================================
# EDA - Annual Income Distribution
# =====================================

plt.figure(figsize=(6,4))
plt.hist(df['annual_income'], bins=20)
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income")
plt.ylabel("Number of Customers")
plt.show()

# =====================================
# Transforming Variables
# =====================================

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['payment_method_encoded'] = le.fit_transform(df['payment_method'])
df['region_encoded'] = le.fit_transform(df['region'])
df['customer_segment_encoded'] = le.fit_transform(df['customer_segment'])

print(df.info())

# =====================================
# Feature Engineering
# =====================================

df['CLV'] = (
    df['avg_monthly_spend']
    * df['months_active']
)

df['frequency_category'] = pd.cut(
    df['purchase_frequency'],
    bins=[0,2,5,100],
    labels=['Low','Medium','High']
)

# =====================================
# Correlation Heatmap
# =====================================

plt.figure(figsize=(10,8))

sns.heatmap(
    df[['annual_income',
        'avg_monthly_spend',
        'purchase_frequency',
        'avg_order_value',
        'CLV']].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

# =====================================
# Customer Segmentation
# =====================================

features = df[
    ['annual_income',
     'avg_monthly_spend',
     'purchase_frequency',
     'avg_order_value',
     'CLV']
]

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_features = scaler.fit_transform(features)

# =====================================
# Elbow Method
# =====================================

from sklearn.cluster import KMeans

wcss = []

for i in range(1,11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42
    )

    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(6,4))
plt.plot(range(1,11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# =====================================
# K-Means Clustering
# =====================================

kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

df['Cluster'] = kmeans.fit_predict(scaled_features)

# =====================================
# Customer Segments Scatter Plot
# =====================================

plt.figure(figsize=(8,6))

plt.scatter(
    df['annual_income'],
    df['avg_monthly_spend'],
    c=df['Cluster'],
    cmap='viridis'
)

plt.colorbar(label='Cluster')

plt.xlabel('Annual Income')
plt.ylabel('Average Monthly Spend')
plt.title('Customer Segmentation using K-Means')

plt.show()

# =====================================
# Customers per Cluster
# =====================================

s

plt.figure(figsize=(8,5))
sns.boxplot(x='Cluster', y='avg_monthly_spend', data=df)

plt.title('Monthly Spend by Cluster')
plt.show()

df['Cluster'].value_counts().sort_index().plot(
    kind='bar'
)

plt.title("Customers per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Number of Customers")
plt.show()

# =====================================
# Cluster Summary
# =====================================

cluster_summary = df.groupby('Cluster')[
    ['annual_income',
     'avg_monthly_spend',
     'purchase_frequency',
     'avg_order_value',
     'CLV']
].mean()

print(cluster_summary)

# =====================================
# Predictive Modeling
# =====================================

X = df[
    ['annual_income',
     'months_active',
     'purchase_frequency',
     'avg_order_value',
     'browsing_time_minutes']
]

y = df['avg_monthly_spend']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# =====================================
# Evaluation
# =====================================

from sklearn.metrics import mean_squared_error, r2_score

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R2 Score:", r2)

# =====================================
# Actual vs Predicted Graph
# =====================================

plt.figure(figsize=(6,6))

plt.scatter(
    y_test,
    y_pred
)

plt.xlabel("Actual Spend")
plt.ylabel("Predicted Spend")
plt.title("Actual vs Predicted")

plt.show()
