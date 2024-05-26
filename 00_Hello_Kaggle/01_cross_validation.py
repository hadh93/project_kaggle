#%%
# 데이터 셋업
import numpy as np
from sklearn.model_selection import KFold

data = np.array([0,1,2,3,4,5,6,7,8,9])

#%%
# shuffle=False 하면 순차적으로 Fold됨
folds = KFold(n_splits=5, shuffle=False)

for train_idx, valid_idx in folds.split(data):
    print(f"훈련 데이터: {data[train_idx]}, 검증 데이터: {data[valid_idx]}")

#%%
# shuffle=True 하면 검증 데이터가 섞임.
folds = KFold(n_splits=5, shuffle=True)

for train_idx, valid_idx in folds.split(data):
    print(f"훈련 데이터: {data[train_idx]}, 검증 데이터: {data[valid_idx]}")

#%%
y = np.array(['스팸']*5 + ['일반']*45)

folds = KFold(n_splits=5, shuffle=True)

for idx, (train_idx, valid_idx) in enumerate(folds.split(y)):
    print(f"Fold {idx+1} 검증 데이터 타깃 값:")
    print(y[valid_idx], "\n")

#%%
from sklearn.model_selection import StratifiedKFold

X = np.array(range(50))
y = np.array(['스팸']*5 + ['일반']*45)

folds = StratifiedKFold(n_splits=5)

for idx, (train_idx, valid_idx) in enumerate(folds.split(X, y)):
    print(f'Fold {idx+1} 검증 데이터 타깃 값:')
    print(y[valid_idx], '\n')

