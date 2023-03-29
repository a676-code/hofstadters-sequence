# hofstadters_sequence.py
# Andrew Lounsbury
# 28/3/23
# Purpose: generate Hofstadter's sequence; https://www.youtube.com/watch?v=j0o-pMIR8uk

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# generates Hofstader's sequence to the n-th number
def generate_hofstadter(n):
    a = [1, 1]
    i = 0
    while len(a) < n:
        a.append(a[i - a[i - 1]] + a[i - a[i - 2]])
    return a

print(generate_hofstadter(20))

# Basic Scatter Plots
n = 10
sequence = generate_hofstadter(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.show()

n = 100
sequence = generate_hofstadter(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.show()

n = 1000
sequence = generate_hofstadter(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.show()

n = 10000
sequence = generate_hofstadter(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.show()

n = 100000
sequence = generate_hofstadter(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.show()