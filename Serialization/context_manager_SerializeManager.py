import json
import pickle
from enum import Enum

#Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
#This class should contain method serialize for serialize object to filename according to  type.
#For defining format create enum FileType with values JSON, BYTE.
#Create function serialize(object, filename, filetype).
#This function use SerializeManager and should serialize object to filename according to type.

class FileType(Enum):
    JSON = "json"
    BYTE = "byte"


class SerializeManager():
    def __init__(self, filename, file_type):
        self.filename = filename
        self.file_type = file_type
        self.file = None

    def __enter__(self):
        if self.file_type == FileType.BYTE:
            mode = 'wb'
        else:
            mode = 'w'
        self.file = open(self.filename, mode)
        return self

    def serialize(self, obj):
        if self.file_type == FileType.JSON:
            json.dump(obj, self.file)
        elif self.file_type == FileType.BYTE:
            pickle.dump(obj, self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


