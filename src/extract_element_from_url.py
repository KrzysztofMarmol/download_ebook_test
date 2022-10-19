def extract_filename(url: str) -> str:
    name = url.split('/')[-1].split("?")[0].replace("_download", "_ebook")
    return name
