import re
with open("input1.txt", "r", encoding="utf-8") as f:
    data = f.read()
so_list = re.findall(r'\d+', data)
chu = re.sub(r'\d+', '', data)
with open("outso.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(so_list))   
with open("outchu.txt", "w", encoding="utf-8") as f:
    f.write(chu.strip())
print("Đã tách đúng định dạng!")