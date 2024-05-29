#%%
from sklearn.tree import DecisionTreeClassifier
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

decisiontree = DecisionTreeClassifier(random_state=42)
decisiontree.fit(X_train, y_train)

accuracy = decisiontree.score(X_test, y_test)


print(f"결정 트리 정확도: {accuracy:.3f}")
