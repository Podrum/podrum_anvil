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

class section:
    def __init__(self, pallete: list, block_states: list, block_light: list = [], sky_light: list = []) -> None:
        self.pallete: list = pallete
        self.block_states: int = block_states
        if len(block_light) == 2048:
            self.block_light: list = block_light
        else:
            self.block_light: list = [0] * 2048
        if len(sky_light) == 2048:
            self.sky_light: list = sky_light
        else:
            self.sky_light: list = [255] * 2048
       
    @staticmethod
    def to_block_index(x: int, y: int, z: int) -> int:
        return y << 8 + z << 4 + x
    
    @staticmethod
    def nibble_4(items: list, index: int) -> int:
        if index % 2 == 0:
            return items[index >> 1] & 0x0f
        else:
            return (items[index >> 1] >> 4) & 0x0f
        
    @staticmethod
    def is_first_sub_index(number: int):
        return True if (number - (number / 2) - (number >> 1)) == 0 else False
        
    def get_sky_light(self, x: int, y: int, z: int) -> int:
        block_index: int = section.to_block_index(x, y, z)
        return section.nibble_4(self.sky_light, block_index)
    
    def set_sky_light(self, x: int, y: int, z: int, light_level: int) -> None:
        block_index: int = section.to_block_index(x, y, z)
        is_first_sub_index: int = section.is_first_sub_index(block_index)
        if is_first_sub_index:
            pass
        else:
            pass
