import pandas as pd
raw_data = pd.read_excel("D:/03_ML/practice/Book1.xlsx")
col_content = raw_data.drop(columns=["content"])
col_sentiment = raw_data.drop(columns=["sentiment"])
col_spam = raw_data.drop(columns=["spam"])

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(col_content, col_spam)
result = model.predict(["Đồ ăn ngon view đẹp"])
print(result)