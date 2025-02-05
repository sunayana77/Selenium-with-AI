# import pandas as pd
# import numpy as np
# import joblib

# df = pd.read_csv('file.csv')
# test = pd.read_csv('test.csv')

# df = df.fillna('None')

# X_train = pd.get_dummies(df.drop('element',axis=1))

# df['element'].unique()

# train_features = X_train.columns
# joblib.dump(train_features, 'train_features.pkl')
 
# element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))


# y_train = df['element'].replace(element_dict)

# from sklearn.ensemble import RandomForestClassifier
# rf = RandomForestClassifier(n_estimators=50, random_state=0)
# rf.fit(X_train, y_train)

# def predict_elements():
#     test_ = test.fillna('None')
#     X_test = pd.get_dummies(test_)
#     X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

#     probabilites = rf.predict_proba(X_test)
#     scores = [list(zip(element_dict.keys(), prob)) for prob in probabilites]

#     element_indices = np.argmax(probabilites, axis=1)
#     element_names = [
#         f"Hence, the name of our predicted element is {list(element_dict.keys())[i]}"
#         for i in element_indices
#     ]

#     return scores, element_names, test


# scores, element_name, test_df = predict_elements()
# print(scores)
# print(element_name)


# joblib.dump(rf, 'random_forest_model.pkl')  # Save the model to a file
# print("Model saved successfully!")

# joblib.dump(element_dict, 'element_dict.pkl')