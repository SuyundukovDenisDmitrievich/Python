# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.

with open("nginx_logs.txt", "r", encoding="utf-8") as file:
    lst_id = []
    for content in file.readlines():
        remote_add = content.split("-")[0].split()[0]
        request_type = content.split("-")[2].split('"')[1].split()[0]
        requested_resource = content.split("-")[2].split('"')[1].split()[1]
        tup_add = (remote_add, request_type, requested_resource)
        lst_id.append(remote_add)
    counter = {}

    for elem in lst_id:
        counter[elem] = counter.get(elem, 0) + 1
        lst_num_req = []
    for meaning in counter.values():
        lst_num_req.append(meaning)
    lst_num_req.sort()
    for key, meaning in counter.items():
        if meaning == lst_num_req[-1]:
            print(f"IP - ({key}) спамера! \nКолличество его запросов - '{meaning}' ")
