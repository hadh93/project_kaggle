#%%
import seaborn as sns
flights = sns.load_dataset('flights')

flights.head()

#%%
# 히트맵(heatmap)

flights_pivot = flights.pivot(index='month', columns='year', values='passengers')

flights_pivot

#%%
sns.heatmap(data=flights_pivot)

#%%
# 라인플롯(lineplot)
sns.lineplot(x='year', y='passengers', data=flights)

#%%
# 산점도(scatterplot)
tips = sns.load_dataset('tips')
tips.head()

#%%
sns.scatterplot(x='total_bill', y='tip', data=tips)

#%%
# hue값을 주면 구분 라벨링이 된 scatterplot 생성 가능
sns.scatterplot(x='total_bill', y='tip', hue='time', data=tips)

#%%
# 회귀선을 포함한 산점도 그래프
sns.regplot(x='total_bill', y='tip', data=tips)

#%%
# 회귀선의 신뢰구간 (Confidence interval)을 조절할 수 있다.
sns.regplot(x='total_bill', y='tip', data=tips, ci=99)