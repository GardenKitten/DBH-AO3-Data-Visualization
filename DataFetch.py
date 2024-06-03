import pandas as pd

import AO3

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    session = AO3.Session("amekuwa", "capmup-hazjas-2rodsY")
    session.refresh_auth_token()

    search = AO3.Search(relationships="Carter Blake/Norman Jayden", session=session)
    search.update()

    # 创建一个空列表用于存储结果
    results_list = []

    while (search.results):

        # 遍历搜索结果，并将每个结果添加到列表中
        for result in search.results:
            print(result)
            print("-------------------")

            results_list.append({
                "title": result.title,
                "date_updated": result.date_updated.strftime("%Y-%m-%d"),
                "rating": result.rating,
                "warnings": ", ".join(result.warnings),
                "relationships": ", ".join(result.relationships),
                "characters": ", ".join(result.characters),
                "fandoms": ", ".join(result.fandoms),
                "tags": ", ".join(result.tags),
                "words": result.words,
            })

        search.page = search.page + 1
        search.update()

    # 创建 DataFrame
    df = pd.DataFrame(results_list)

    # 保存为 CSV 文件
    df.to_csv('Carter／Norman/works.csv', index=False, encoding='utf-8')

    # # 将结果列表转换为 JSON 字符串
    # json_data = json.dumps(results_list, indent=4)
    #
    # # 将 JSON 字符串写入文件
    # with open('search_results.json', 'w') as json_file:
    #     json_file.write(json_data)

# work = AO3.Work(17428628)
#
# print(work.chapters[0].title)  # Second chapter name
# print(work.date_published)
