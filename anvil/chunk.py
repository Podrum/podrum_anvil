from nbt_utils.tag.compound_tag import compound_tag
from nbt_utils.tag.int_tag import int_tag
from nbt_utils.utils.nbt_be_binary_stream import nbt_be_binary_stream

class chunk:
    def __init__(self, x: int, z: int) -> None:
        self.x: int = x
        self.z: int = z
  
    def read_chunk_data(self, chunk_data: bytes) -> None:
        stream: object = nbt_be_binary_stream(chunk_data)
        tag: object = compound_tag()
        tag.read(stream)
        root_tag: object = tag.read_tag("")
        self.data_version: int = root_tag.get_tag("DataVersion").value
        level_tag: object = tag.read_tag("Level")
        self.x: int = level_tag.get_tag("xPos").value
        self.z: int = level_tag.get_tag("zPos").value
        self.data: object = level_tag
            
    def write_chunk_data(self) -> bytes:
        stream: object = nbt_be_binary_stream()
        tag: object = compound_tag()
        tag.set_tag(compound_tag())
        level_tag: object = self.data
        level_tag.set_tag(int_tag("xPos", self.x)
        level_tag.set_tag(int_tag("zPos", self.s)
        tag.get_tag("").set_tag(level_tag)
        tag.get_tag("").set_tag(int_tag("DataVersion", self.data_version))
