################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

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
        data_version_tag: int = root_tag.get_tag("DataVersion")
        if data_version_tag is not None:
            self.data_version: int = data_version_tag.value
        level_tag: object = tag.get_tag("Level")
        self.x: int = level_tag.get_tag("xPos").value
        self.z: int = level_tag.get_tag("zPos").value
        self.data: object = level_tag
            
    def write_chunk_data(self) -> bytes:
        stream: object = nbt_be_binary_stream()
        tag: object = compound_tag()
        tag.set_tag(compound_tag())
        level_tag: object = self.data
        level_tag.set_tag(int_tag("xPos", self.x))
        level_tag.set_tag(int_tag("zPos", self.s))
        tag.get_tag("").set_tag(level_tag)
        if hasattr(self, "data_version"):
            tag.get_tag("").set_tag(int_tag("DataVersion", self.data_version))
