import math
def so_nguyen_to_cua_n(n):
    factors = set()
    if n <= 1:
        return factors
    if n % 2 == 0:
        factors.add(2)
        while n % 2 == 0:
            n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
    if n > 2:
        factors.add(n)
    return sorted(list(factors))
def process_files(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
                line = line.strip()
                if not line:
                    continue
                try:
                    num = int(line)
                    prime_factors = so_nguyen_to_cua_n(num)
                    result = " ".join(map(str, prime_factors))
                    f_out.write(result + "\n")
                except ValueError:
                    f_out.write("Dòng không phải là số tự nhiên hợp lệ\n")
        print(f"Xử lý thành công! Kết quả đã được ghi vào {output_file}")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp {input_file}")
if __name__ == "__main__":
    process_files('input.txt', 'output.txt')