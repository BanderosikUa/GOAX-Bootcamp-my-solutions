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
    name = filename.split(".")[0]
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