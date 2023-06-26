import kaggle.api
from pathlib import Path
from zipfile import ZipFile

data_path = Path.cwd().joinpath("data")
kaggle.api.competition_download_files("spaceship-titanic")
with ZipFile("spaceship-titanic.zip", "r") as zObject:
    zObject.extractall(path=data_path)
Path("spaceship-titanic.zip").unlink()
