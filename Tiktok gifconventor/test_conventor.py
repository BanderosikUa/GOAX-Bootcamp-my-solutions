from pathlib import Path
from main import (
    _rename_file_to_gif,
    download_video,
    make_gif,
)

BASE_DIR = Path(__file__).resolve().parent

test_video = BASE_DIR.joinpath('test_files') / "test_video.mp4"


def test_rename():
    filename = test_video
    assert _rename_file_to_gif(filename.name) == 'test_video.gif'


def test_make_gif():
    output = make_gif(test_video, location_folder=BASE_DIR.joinpath("test_files"))
    assert output == str(BASE_DIR.joinpath('test_files') / "test_video.gif")

