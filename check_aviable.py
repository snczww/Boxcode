import requests
import concurrent.futures


def check_url(line):
    # custom_headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    #     "Accept-Language": "en-US,en;q=0.9",
    # }

    session = requests.Session()
    if '#genre#' in line:
        return line
    if line.strip() == "":
        return None
    try:
        # response = requests.head(line.split(",")[1].strip(),headers=custom_headers,timeout=5)
        # if response.status_code == requests.codes.ok:
        #     return line


        # with session.get(line.split(",")[1].strip(), timeout=10,stream=True) as response:

        with requests.get(line.split(",")[1].strip(), timeout=10,stream=True) as response:
            if response.status_code == 200:
                # URL可用，返回该行
                # response.close()
                # session.close()  # 关闭会话对象
                return line
        # session.close()



    except:
        # URL不可用，不做处理
        print(f"URL不可用：{line}")
        pass
    # URL不可用或出现异常，返回 None


    return None


with open('output/ip6live.txt', 'r', encoding='utf-8') as f:
    # 遍历每一行，将需要检查的行添加到列表中
    # lines = []
    # for line in f:
    #     lines.append(line.strip())
    lines = iter(f)  # 使用迭代器逐行读取文件


    # 使用 ThreadPoolExecutor 创建一个线程池，将每个 URL 的检查过程提交给线程池进行并发处理
    with concurrent.futures.ThreadPoolExecutor(max_workers=4000) as executor:
        # 使用 executor.map 方法并发处理每个 URL 的检查过程
        results = executor.map(check_url, lines)

        # 将有效的 URL 写入文件，并保持和原来的顺序一致
        with open('output/ip6live.txt', 'w', encoding='utf-8') as f_out:
            for result in results:
                if result is not None:
                    # f_out.write(result + '\n')
                    f_out.write(result)

    # 手动关闭线程池
    executor.shutdown()
