#%%
import seaborn as sns
titanic = sns.load_dataset(name='titanic')
titanic.head()

#%%
sns.histplot(data=titanic, x='age')

#%%
# bins 매개변수는 히스토그램의 막대 개수를 나타내며, 
# 여기서는 10으로 설정되어 있어 나이를 10개의 구간으로 나누어서 히스토그램이 생성됩니다.
sns.histplot(data=titanic, x='age', bins=10)

#%%
# hue 매개변수는 막대의 색상을 결정할 다른 변수(alive)를 지정합니다. 
# 이를 통해 생존한 승객과 생존하지 못한 승객 간의 나이 분포를 시각적으로 비교할 수 있습니다.
sns.histplot(data=titanic, x='age', hue='alive')

#%%
sns.histplot(data=titanic, x='age', hue='alive', multiple='stack')
# multiple 매개변수는 여러 범주에 대한 막대를 쌓아서 표시할 것인지를 지정합니다. 
# 여기서는 'stack'으로 설정되어 있어 생존 여부에 따라 막대가 쌓여서 표시됩니다.


# 커널밀도추정 함수 그래프 (kdeplot)
# Kernel Density Estimation은 주어진 데이터셋의 분포를 추정하여 부드러운 확률 밀도 곡선을 생성합니다. 
# 이를 통해 승객들의 나이에 대한 분포를 시각화할 수 있습니다.

#%%
# 나이('age')에 대한 커널 밀도 추정(KDE)을 시각화합니다.
sns.kdeplot(data=titanic, x='age')

#%%
# 나이에 대한 커널 밀도 추정(KDE)을 그리고, 생존 여부에 따라 다른 그룹으로 분리하여 겹쳐서 표시합니다.

# hue='alive' 매개변수는 생존 여부에 따라 데이터를 분리합니다.
# multiple='stack' 매개변수는 각 그룹의 커널 밀도 추정을 겹쳐서 표시합니다.
sns.kdeplot(data=titanic, x='age', hue='alive', multiple='stack')

#%%
# distplot은 histplot을 wrap합니다.
# default로 히스토그램을, 원한다면 KDE를 각각 혹은 함께 플로팅할 수 있습니다.

#%%
# displot-히스토그램만(default)
sns.displot(data=titanic, x='age')

#%% 
# displot-KDE만
sns.displot(data=titanic, x='age', kind='kde')

#%%
# displot - 히스토그램 + KDE
sns.displot(data=titanic, x='age', kde=True)


# 러그플롯 (rugplot)

# 데이터의 실제 위치를 x축 위의 작은 선분(rug)로 나타내어 데이터의 분포를 보여줍니다(주로 1차원 데이터).
#%%
# 커널밀도추정 + 러그플롯
sns.kdeplot(data=titanic, x='age')
sns.rugplot(data=titanic, x='age')