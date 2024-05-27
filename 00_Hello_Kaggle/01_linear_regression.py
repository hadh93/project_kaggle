#%%
# 예제 데이터 생성
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0) # 시드값 고정

w0 = 5 # y절편
w1 = 2 # 회귀 계수
noise = np.random.randn(100,1) # 노이즈

x = 4*np.random.rand(100,1)
y = w1*x + w0 + noise

plt.scatter(x,y)

#%%
# 모델 훈련
from sklearn.linear_model import LinearRegression

linear_reg_model = LinearRegression() #선형 회귀 모델
linear_reg_model.fit(x,y)

print("y절편(w0): ", linear_reg_model.intercept_)
print("회귀계수(w1): ", linear_reg_model.coef_)

#%%
y_pred = linear_reg_model.predict(x) # 예측

plt.scatter(x,y)
plt.plot(x, y_pred)

