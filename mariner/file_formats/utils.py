import os
from typing import Mapping, Set, Type

from mariner.file_formats import SlicedModelFile
from mariner.file_formats.ctb import CTBFile
from mariner.file_formats.cbddlp import CBDDLPFile
from mariner.file_formats.fdg import FDGFile


EXTENSION_TO_FILE_FORMAT: Mapping[str, Type[SlicedModelFile]] = {
    ".ctb": CTBFile,
    ".cbddlp": CBDDLPFile,
    ".fdg": FDGFile,
}


def get_file_extension(filename: str) -> str:
    (_, extension) = os.path.splitext(filename)
    return extension.lower()


def get_file_format(filename: str) -> Type[SlicedModelFile]:
    file_format = EXTENSION_TO_FILE_FORMAT.get(get_file_extension(filename))

    assert file_format is not None
    return file_format


def get_supported_extensions() -> Set[str]:
    return set(EXTENSION_TO_FILE_FORMAT.keys())
