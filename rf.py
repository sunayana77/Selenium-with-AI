import pandas as pd
# import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('file.csv')
test = pd.read_csv('test.csv')


df = df.fillna('None')
test = test.fillna('None')

X_train = pd.get_dummies(df.drop('element', axis=1))
y_train = df['element']

rf = RandomForestClassifier(n_estimators=50, random_state=0)
rf.fit(X_train, y_train)


element_dict = dict(zip(df['element'].unique(),
                    range(df['element'].nunique())))

joblib.dump(rf, 'random_forest_model.pkl')
joblib.dump(X_train.columns, 'train_features.pkl')
joblib.dump(element_dict, 'element_dict.pkl')


X_test = pd.get_dummies(test)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

predicted_labels = rf.predict(X_test)

print("Predicted action labels:", predicted_labels)
print(element_dict)
