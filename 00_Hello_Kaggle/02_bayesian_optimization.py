#%%
# 하이퍼 파라미터 탐색 범위 설정 (딕셔너리 형태)
param_bounds = {"x": (-1, 5),
                "y": (0, 4)}

#%%
# 평가지표 계산 함수 정의
def eval_function(x, y):
    return -x ** 2 - (y - 2) ** 2 + 10

#%%
from bayes_opt import BayesianOptimization
# 베이지안 최적화 객체 생성
optimizer = BayesianOptimization(f=eval_function,
                                 pbounds=param_bounds,
                                 random_state=0)

#%%
# 최적화 수행
optimizer.maximize(init_points=2, n_iter=10)

#%%
# 평가점수가 최대일 때 타깃 x,y 값 출력
optimizer.max