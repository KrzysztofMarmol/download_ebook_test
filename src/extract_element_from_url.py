def extract_filename(url: str) -> str:
    name = [s for s in url.replace("?", "/").split('/') if ".pdf" in s][0]
    return name
