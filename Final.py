# import libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# import data
stock = pd.read_csv("sp500_stocks.csv")
index = pd.read_csv("sp500_index.csv")
company = pd.read_csv("sp500_companies.csv")

# data pre-processing: remove missing value
stock = stock.dropna()
index = index.dropna()
# data pre-processing: remove duplicated value
stock = stock.drop_duplicates()
index = index.drop_duplicates()
# data pre-processing: Convert Date data to datetime type
stock['Date'] = pd.to_datetime(stock['Date'])
index['Date'] = pd.to_datetime(index['Date'])
# data pre-processing: Remove stocks with missing data from the dataset
stock_counts = stock.groupby('Symbol').size()
full_data_length = stock_counts.max()
incomplete_stocks = stock_counts[stock_counts < full_data_length].index
stock_cleaned = stock[~stock['Symbol'].isin(incomplete_stocks)]
# data pre-processing: Add sector info from company to stock_cleaned
stock_cleaned = pd.merge(stock_cleaned, company, how='left', left_on='Symbol', right_on='Symbol')

# Question 1
# pre-processing
stock_cleaned['Daily_Return'] = stock_cleaned.groupby('Symbol')['Adj Close'].pct_change()
features = stock_cleaned.groupby('Symbol').agg({
    'Daily_Return': ['mean', 'std', 'skew'],  
    'Volume': ['mean', 'std'],  
    'High': lambda x: x.max() - x.min(),  
    'Low': lambda x: x.max() - x.min(),  
    'Open': lambda x: x.max() - x.min(),  
}).reset_index()
features.columns = ['Symbol', 'Return_Mean', 'Return_Std', 'Return_Skew',
                    'Volume_Mean', 'Volume_Std', 'High_Range', 'Low_Range', 'Open_Range']

X = features.set_index('Symbol')
y = stock_cleaned.groupby('Symbol')['Sector'].first()
y = y.dropna()
X = X.loc[y.index]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# random forest
rf = RandomForestClassifier(n_estimators=500, random_state=42, max_depth=10, class_weight='balanced')
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=1))

import matplotlib.pyplot as plt
import numpy as np
feature_importances = rf.feature_importances_
features = X_train.columns  
plt.figure(figsize=(10, 6))
indices = np.argsort(feature_importances)[::-1]
plt.bar(range(len(features)), feature_importances[indices], align="center")
plt.xticks(range(len(features)), [features[i] for i in indices], rotation=45)
plt.title("Feature Importances")
plt.show()

from sklearn.metrics import classification_report
import seaborn as sns
import pandas as pd
report = classification_report(y_test, y_pred, output_dict=True)
df_report = pd.DataFrame(report).transpose()
plt.figure(figsize=(10, 6))
sns.heatmap(df_report.iloc[:-1, :-1], annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Classification Report")
plt.show()


# Question 2
amzn_data = stock_cleaned[stock_cleaned['Symbol'] == 'AMZN'].copy()
amzn_data['Price_Change'] = (amzn_data['Adj Close'].shift(-1) > amzn_data['Adj Close']).astype(int)
amzn_data['SMA_5'] = amzn_data['Adj Close'].rolling(window=5).mean().shift(1)
amzn_data['SMA_10'] = amzn_data['Adj Close'].rolling(window=10).mean().shift(1)
amzn_data['SMA_20'] = amzn_data['Adj Close'].rolling(window=20).mean().shift(1)

amzn_data['Daily_Return'] = amzn_data['Adj Close'].pct_change().shift(1)
amzn_data['Volume_Change'] = amzn_data['Volume'].pct_change().shift(1)
amzn_data = amzn_data.dropna()
features = ['SMA_5', 'SMA_10', 'SMA_20', 'Daily_Return', 'Volume_Change']
X = amzn_data[features]
y = amzn_data['Price_Change']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)
print(classification_report(y_test, y_pred))


