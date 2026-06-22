import os
from typing import Dict, List

MAIN_ROOT_FOLDER = "workspace" # workspace adlı dosyanın absolute konumu. burada dosya okuma yazma yapılabilir
VIEWABLE_FOLDER_ROOT = "C:/" # C diski. yalnızca dosya okuma yapılabilir

def create_element(element_name: str, file_type: str, location: str = ""):
    """
    Create a file or folder at a given location.

    Parameters:
        element_name (str): Name of the element to create, or its relative path.
        file_type (str): Type of element. Expected values are 'file' or 'folder'.
        location (str): Optional target folder path where the element should be created.

    Returns:
        None: This function should create the element and does not return a value.
    """
    pass


def write_file(file_name: str, content: str):
    """
    Write string content into a file.

    Parameters:
        file_name (str): Name or relative path of the file to write.
        content (str): Text content to write into the file.

    Returns:
        None: This function writes the content and does not return a value.
    """
    pass


def empty_file(file_name: str):
    """
    Clear the contents of a file.

    Parameters:
        file_name (str): Name or relative path of the file to truncate.

    Returns:
        None: This function empties the file and does not return a value.
    """
    pass


def delete_element(element_name: str):
    """
    Delete a file or folder.

    Parameters:
        element_name (str): Name or relative path of the element to delete.

    Returns:
        None: This function removes the element and does not return a value.
    """
    pass


def read_file(file_name: str):
    """
    Read and return the text content of a file.

    Parameters:
        file_name (str): Name or relative path of the file to read.

    Returns:
        str: The contents of the file.
    """
    pass


def search_folder(folder_name: str):
    """
    Return a representation of a folder's contents.

    Parameters:
        folder_name (str): Name or relative path of the folder to search.

    Returns:
        dict or list: Structured representation of files and subfolders under the folder.
    """


def move_file(file_name: str, new_location: str):
    """
    Move a file to a new destination.

    Parameters:
        file_name (str): Name or relative path of the file to move.
        new_location (str): Destination folder path or new relative path for the file.

    Returns:
        None: This function moves the file and does not return a value.
    """
    pass

