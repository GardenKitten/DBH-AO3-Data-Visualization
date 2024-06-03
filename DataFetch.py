import time

import pandas as pd

import AO3

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    session = AO3.Session("amekuwa", "capmup-hazjas-2rodsY")
    session.refresh_auth_token()

    search = AO3.Search(relationships="Markus/Simon (Detroit: Become Human)", session=session)
    search.update()



    # 创建一个空列表用于存储结果
    results_list = []

    while (search.results):

        # 遍历搜索结果，并将每个结果添加到列表中
        for result in search.results:
            print(result)

            results_list.append({
                "title": result.title,
                "date_updated": result.date_updated.strftime("%Y-%m-%d"),
                "rating": result.rating,
                "warnings": ", ".join(result.warnings),
                "relationships": ", ".join(result.relationships),
                "characters": ", ".join(result.characters),
                "fandoms": ", ".join(result.fandoms),
                "tags": ", ".join(result.tags),
            })

        search.page = search.page + 1
        print(f"page:{search.page}")

        if search.page % 2 == 1:
            # 等待5秒
            time.sleep(5)
        else:
            # 等待8秒
            time.sleep(9)

        search.update()

    # 创建 DataFrame
    df = pd.DataFrame(results_list)

    # 保存为 CSV 文件
    df.to_csv('Simarkus/works.csv', index=False, encoding='utf-8')
