import timeit

def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for i in range(length - 1):
        table[pattern[i]] = length - 1 - i
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            return i - j
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(M - 1):
        h = (h * d) % q
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(N - M + 1):
        if p == t:
            if text[i:i + M] == pattern:
                return i
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
    return -1

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

if __name__ == "__main__":
    text1 = read_file("goit-algo-hw-05/task3/article1.txt")
    text2 = read_file("goit-algo-hw-05/task3/article2.txt")

    if text1 and text2:
        tasks = [
            ("article1", text1, "алгоритм"),
            ("article1", text1, "марсохід"),
            ("article2", text2, "рекомендації"),
            ("article2", text2, "марсохід")
        ]

        for name, text, pattern in tasks:
            print(f"File: {name}, Pattern: {pattern}")
            
            t_bm = timeit.timeit(lambda: boyer_moore_search(text, pattern), number=10)
            print(f"Boyer-Moore: {t_bm}")

            t_kmp = timeit.timeit(lambda: kmp_search(text, pattern), number=10)
            print(f"KMP: {t_kmp}")

            t_rk = timeit.timeit(lambda: rabin_karp_search(text, pattern), number=10)
            print(f"Rabin-Karp: {t_rk}")
            
            print("-" * 20)