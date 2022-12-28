def remove(s: str, n: int) -> str:
    removed = 0
    result = ""
    for c in s:
        if c == "!" and removed < n:
            removed += 1
            continue
        result += c
    return result