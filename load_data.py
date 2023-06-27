def download_dataset(competition_name="spaceship-titanic", data_dir="data"):
    """
    Downloads a dataset from Kaggle competition and extracts its contents to a specified directory.

    Args:
        competition_name (str, optional): Name of the Kaggle competition. Defaults to "spaceship-titanic".
        data_dir (str, optional): Directory where the dataset will be extracted. Defaults to "data".
    """
    from kaggle.api import competition_download_files
    from pathlib import Path
    from zipfile import ZipFile

    data_path = Path.cwd().joinpath(data_dir)

    # Download the zip file containing competition files to the
    # current working directory
    competition_download_files(competition_name)

    # Open and extract the contents of the file to the data path
    zip_file_path = Path.cwd().joinpath(competition_name).with_suffix(".zip")
    with ZipFile(zip_file_path, "r") as zObject:
        zObject.extractall(path=data_path)

    # Delete the zip file
    Path(zip_file_path).unlink()


if __name__ == "__main__":
    download_dataset()
