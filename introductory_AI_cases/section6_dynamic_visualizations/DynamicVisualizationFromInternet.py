import pandas as pd

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://anvil.works/blog/img/plotting-in-python/uk-election-results.csv')

sns.set()
plt.figure()

ax = sns.barplot(
        data=df,
        x="year",
        y="seats",
        hue="party",
        palette=['blue', 'red', 'yellow', 'grey'],
        saturation=0.6,
    )

plt.show()

ax.set_title('UK election results')

    ax.grid(color='#cccccc')

    ax.set_ylabel('Seats')
    ax.set_xlabel(None)
    ax.set_xticklabels(df["year"].unique().astype(str), rotation='vertical')