import requests
import concurrent.futures

def check_url(line):
    if '#genre#' in line:
        return line
    if line.strip() == "":
        return None
    try:
        response = requests.get(line.split(",")[1].strip(), timeout=5)
        if response.status_code == 200:
            # URL可用，返回该行
            return line
    except:
        # URL不可用，不做处理
        print(f"URL不可用：{line}")
        pass
    # URL不可用或出现异常，返回 None
    return None

with open('output/ip6live.txt', 'r', encoding='utf-8') as f:
    # 遍历每一行，将需要检查的行添加到列表中
    lines = []
    for line in f:
        lines.append(line.strip())

    # 使用 ThreadPoolExecutor 创建一个线程池，将每个 URL 的检查过程提交给线程池进行并发处理
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        # 使用 executor.map 方法并发处理每个 URL 的检查过程
        results = executor.map(check_url, lines)

        # 将有效的 URL 写入文件，并保持和原来的顺序一致
        with open('output/ip6live.txt', 'w', encoding='utf-8') as f_out:
            for result in results:
                if result is not None:
                    f_out.write(result + '\n')
