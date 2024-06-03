import json


def merge_to_array(file1, file2, output_file):
    # 读取第一个JSON文件
    with open(file1, 'r') as f1:
        data1 = json.load(f1)

    # 读取第二个JSON文件
    with open(file2, 'r') as f2:
        data2 = json.load(f2)

    # 合并数据为一个数组
    merged_data = [data1, data2]

    # 将合并后的数据写入新的JSON文件
    with open(output_file, 'w') as output_f:
        json.dump(merged_data, output_f, indent=4)

# 示例用法
merge_to_array('Carter／Norman/counts.json', 'Norman／Ethan/counts.json', 'total_counts.json')
