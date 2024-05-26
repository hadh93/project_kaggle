#%%
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_squared_log_error, r2_score

true = np.array([1, 2, 3, 2, 3, 5, 4, 6, 5, 6, 7, 8, 8]) # 실제값
preds = np.array([1, 1, 2, 2, 3, 4, 4, 5, 5, 7, 7, 6, 8]) # 예측값

#%%
MAE = mean_absolute_error(true, preds)
MSE = mean_squared_error(true, preds)
RMSE = np.sqrt(MSE)
MSLE = mean_squared_log_error(true, preds)
RMSLE = np.sqrt(MSLE)
R2 = r2_score(true,preds)

# MAE: 평균 절대 오차
print(f"MAE:\t {MAE:.4f}")

# MSE: 평균 제곱 오차
# 특이치에 민감
print(f"MSE:\t {MSE:.4f}")

# RMSE: 평균 제곱근 오차 (MSE의 제곱근)
# 제곱근 오차는 목표 변수와 동일한 단위이므로 해석이 더 쉽다는 장점이 있음!
print(f"RMSE:\t {RMSE:.4f}")

# MSLE: 평균 제곱 로그 오차
# 예측 값의 자연 로그와 실제 값의 자연 로그 간의 제곱 차이의 평균
# 목표 변수가 지수적 성장을 보일 때 유용함.
print(f"MSLE:\t {MSLE:.4f}")

# RMSLE: 평균 제곱근 로그 오차
# MLSE의 제곱근
# RMSE와 마찬가지로, 제곱근 오차는 목표 변수와 동일한 단위이므로 해석이 더 쉽다는 장점이 있음!
print(f"RMSLE:\t {RMSLE:.4f}")

# R2: 결정 계수
# 종속 변수의 분산 중 독립 변수로부터 예측 가능한 부분의 비율을 나타냄
# 0에서 1까지의 범위를 가지며, 1은 완벽한 적합을 나타냄
print(f"R2:\t {R2:.4f}")
