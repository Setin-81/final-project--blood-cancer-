import pandas as pd
import matplotlib.pyplot as plt

# خواندن داده‌ها از فایل اکسل
df = pd.read_excel("cancer.xlsx")

# تحلیل ابتدایی: تعداد موارد سرطان بر اساس جنسیت
cancer_counts = df['Gender'].value_counts()

# نمایش نمودار
plt.figure(figsize=(6, 4))
cancer_counts.plot(kind='bar', color=['lightgreen', 'orange'])
#cancer_counts.plot(kind="pie", color=['blue', 'pink'])
plt.title('The Number of people who have Blood-cancer')
plt.xlabel('Gender')
plt.ylabel('Amount')
plt.xticks(rotation=0)
plt.show()
