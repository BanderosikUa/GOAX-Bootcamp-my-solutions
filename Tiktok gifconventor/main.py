import urllib

from pathlib import Path
from moviepy.editor import VideoFileClip

BASE_DIR = Path(__file__).resolve().parent


def download_video(url: str) -> Path:
    # returning file location
    filename, headers = urllib.request.urlretrieve(
        url, "tiktok_video.mp4"
    )
    return BASE_DIR / filename


def _rename_file_to_gif(filename: str) -> str:
    """Rename mp4 to gif or ,if file exists, create new name"""
    name = filename.split(".")[0]
    list_of_gifs = list(BASE_DIR.glob("*.gif"))
    if len(list_of_gifs) > 1:
        split_file_num = list_of_gifs[-1].name.split("-")
        previous_num = int(split_file_num[1].split('.')[0])
        name = split_file_num[0] + f"-{previous_num + 1}"
    elif len(list_of_gifs) == 1:
        name = name + '-1'
    return name + ".gif"


def make_gif(filename: Path, location_folder: Path = None) -> str:
    output_file = _rename_file_to_gif(filename.name)
    clip = (VideoFileClip(str(filename)))
    location = location_folder / output_file if location_folder \
        else BASE_DIR / output_file
    clip.write_gif(location,
                   fps=20,
                   program='ffmpeg',
                   verbose=False,
                   logger=None)
    return str(location)


def delete_video(filename: Path) -> None:
    filename.unlink()


if __name__ == "__main__":
    url = input('Enter tiktok video url:')
    video = download_video(url)
    output = make_gif(video)
    delete_video(video)
    print(output)
