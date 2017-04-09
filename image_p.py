import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("file:///home/guoke/douban.xlsx",
"Sheet1")
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(df['A'],bins=12)
plt.title('douban books analyze')
plt.xlabel('month')
plt.ylabel('number')
plt.show()



   