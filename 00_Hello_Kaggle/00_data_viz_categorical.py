#%%
import seaborn as sns
titanic = sns.load_dataset(name='titanic')

#%%
# 막대 그래프 (barplot)
# 'hue'매개변수를 사용하면, 특정 열(e.g. 'class')을 기준으로,
# 각 막대 그래프를 색으로 구분하여 표시할 수 있다.
sns.barplot(x='class', y='fare', data=titanic, hue='class')

#%%
# 포인트플롯 (pointplot) - 꺾은선그래프
sns.pointplot(x='class', y='fare', data=titanic)

#%%
# 박스플롯 (boxplot)
sns.boxplot(x='class', y='age', data=titanic)

#%%
# 바이올린플롯 (violinplot)
sns.violinplot(x='class', y='age', data=titanic, hue='class')

#%%
# 'split' 매개변수를 True로 설정하여, 바이올린플롯을 split하여 표시할 수도 있다.
sns.violinplot(x='class', y='age', hue='sex', data=titanic, split=True)

#%%
# 카운트플롯(countplot) - 막대그래프지만 1개 매개변수의 개수만을 세는 것
sns.countplot(x='class', data=titanic, hue='class')

#%%
# 카운트플롯을 x축이 아닌 y축에 표시할 수도 있다.
sns.countplot(y='class', data=titanic, hue='class')

#%%
import matplotlib.pyplot as plt

x = [10,60,30]
labels = ['A','B','C']

plt.pie(x=x, labels=labels, autopct='%.1f%%') # %.1f%% - 소수점 첫 번째 자리까지의 실수를 퍼센트 형태로 표시
