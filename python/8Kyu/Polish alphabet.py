def correct_polish_letters(st: str) -> str:
    # your code here
    dic: Dict[str, str] = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}
    return "".join(dic.get(_, _) for _ in st)