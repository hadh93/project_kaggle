#%%
import seaborn as sns
titanic = sns.load_dataset(name='titanic')
titanic.head()

#%%
sns.histplot(data=titanic, x='age')
