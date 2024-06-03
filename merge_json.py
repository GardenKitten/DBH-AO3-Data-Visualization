import json


def merge_to_array(file1, file2, file3, file4, file5, file6, output_file):
    # 读取JSON文件
    with open(file1, 'r') as f1:
        data1 = json.load(f1)

    with open(file2, 'r') as f2:
        data2 = json.load(f2)

    with open(file3, 'r') as f3:
        data3 = json.load(f3)

    with open(file4, 'r') as f4:
        data4 = json.load(f4)

    with open(file5, 'r') as f5:
        data5 = json.load(f5)

    with open(file6, 'r') as f6:
        data6 = json.load(f6)

    # 合并数据为一个数组
    merged_data = [data1, data2, data3, data4, data5, data6]

    # 将合并后的数据写入新的JSON文件
    with open(output_file, 'w') as output_f:
        json.dump(merged_data, output_f, indent=4)


# 示例用法
merge_to_array('1700/counts.json', 'Simarkus/counts.json', 'RK1K/counts.json', 'Convin/counts.json',
               'Reed900/counts.json', 'HankCon/counts.json',
               'total_counts.json')
