from tqdm import tqdm
from pathlib import Path  # python> = 3.5

from constants import content_length


def create_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)


def save_response_to_file_by_tqdm(path, response):
    total = int(response.headers.get(content_length, 0))
    with open(path, 'wb') as file, tqdm(
        desc=path,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
