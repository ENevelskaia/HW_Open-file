file_list = ['1.txt','2.txt','3.txt']
all_file_dict = {}
for f_1 in file_list:
    with open(f_1,'r',encoding='utf8') as file:
        text = file.readlines()
        file.seek(0)
        res = len(file.readlines())
        all_file_dict[res] = [f'{f_1}\n', f'{str(res)}\n', f"{''.join(text)}\n"]

sorted_file_list = []
for k in sorted(all_file_dict):
    sorted_file_list += all_file_dict[k]

with open('final_file.txt', 'w', encoding='utf8') as file:
    file.writelines(sorted_file_list)

