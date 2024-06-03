import pandas as pd
import json
from collections import Counter

# 读取CSV文件
df = pd.read_csv('1700/works.csv')

# 将日期按升序排列
df['date_updated'] = pd.to_datetime(df['date_updated'])
df.sort_values(by='date_updated', inplace=True)

# 统计rating列中每个不同数值的出现次数
rating_counts = df['rating'].value_counts().to_dict()

# 拆分warnings列中的标签并统计每个标签的出现次数
warnings_series = df['warnings'].dropna().apply(lambda x: x.split(', '))
warnings_list = [item for sublist in warnings_series for item in sublist]
warnings_counts = dict(Counter(warnings_list))

# 累计统计date_updated列中每个日期的出现次数
date_counts = {}
total_count = 0
for date, count in df['date_updated'].value_counts().sort_index().items():
    total_count += count
    date_counts[date.strftime('%Y-%m-%d')] = total_count

# 将统计结果包装在一个JSON对象中
count_data = {
    "relationship": "1700",
    "rating_counts": rating_counts,
    "warnings_counts": warnings_counts,
    "date_counts": date_counts
}

# 将统计结果保存到JSON文件
with open('1700/counts.json', 'w') as json_file:
    json.dump(count_data, json_file, indent=4)

print("统计结果已成功保存到counts.json文件中")
