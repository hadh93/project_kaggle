#%%
import pandas as pd
height_weight_dict = {'키':[1.7, 1.5, 1.8], '몸무게':[75,55,60]}
df = pd.DataFrame(height_weight_dict, index=['광일','혜성','덕수'])

print(df)

#%%
from sklearn.preprocessing import MinMaxScaler

# min-max 정규화 객체 생성
scaler = MinMaxScaler()
scaler.fit(df)
df_scaled = scaler.transform(df)

print(df_scaled)

#%%
# min-max 정규화 객체 생성
scaler = MinMaxScaler()

#min-max 정규화 적용
df_scaled = scaler.fit_transform(df)

print(df_scaled)

#%%
# 표준화
from sklearn.preprocessing import StandardScaler

# StandardScaler 객체 생성
scaler = StandardScaler()

# 표준화 적용
df_scaled = scaler.fit_transform(df)

print(df_scaled)