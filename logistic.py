import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [10, 20, 30, 40, 50],
    'Feature3': ['A', 'B', 'A', 'C', 'B'],
    'Target': [1, 0, 1, 1, 0]
})

label_encoder = preprocessing.LabelEncoder()
obj = (data.dtypes == 'object')
for col in list(obj[obj].index):
    data[col] = label_encoder.fit_transform(data[col].astype(str))

X = data.drop(['Target'], axis=1)
y = data['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_train_pred = model.predict(X_train)
print("Accuracy score on training data =", 100 * metrics.accuracy_score(y_train, y_train_pred))
y_test_pred = model.predict(X_test)
accuracy_test = 100 * metrics.accuracy_score(y_test, y_test_pred)
print("Accuracy score on testing data =", accuracy_test)
