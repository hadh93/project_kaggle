#%%
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    cancer_data['data'],
    cancer_data['target'],
    stratify=cancer_data['target'],
    test_size=0.4,
    random_state=42
)

randomforest = RandomForestClassifier(random_state=42)
randomforest.fit(X_train, y_train)

accuracy = randomforest.score(X_test, y_test)

print(f"랜덤 포레스트 정확도: {accuracy:.3f}")
