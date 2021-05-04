from binary_utils.binary_converter import binary_converter
import gzip
import time
import zlib

class region:
    def __init__(self, path: str) -> None:
        self.path: str = path

    def get_location(self, x: int, z: int) -> int:
        return 4 * ((x & 31) + (z & 31) * 32)

    def get_chunk(self, x: int, z: int) -> bytes:
        file: object = open(self.path, "rb")
        index_location: int = self.get_location(x, z)
        file.seek(index_location)
        offset: int = binary_converter.read_unsigned_triad_be(file.read(3))
        sector_count: int = binary_converter.read_unsigned_byte(file.read(1))
        if offset == 0 and sector_count == 0:
            return b""
        file.seek(offset * 4096)
        length: int = binary_converter.read_unsigned_int_be(file.read(4))
        compression_type: int = binary_converter.read_unsigned_byte(file.read(1))
        chunk_data: bytes = file.read(length)
        file.close()
        if compression_type == 1:
            return gzip.decompress(chunk_data)
        if compression_type == 2:
            return zlib.decompress(chunk_data)

    def put_chunk(self, x: int, z: int, chunk_data: bytes, compression_type: int = 2) -> None:
        file: object = open(self.path, "r+b")
        read: str = list(file.read())
        if compression_type == 1:
            cc: bytes = gzip.compress(chunk_data)
        elif compression_type == 2:
            cc: bytes = zlib.compress(chunk_data)
        else:
            return
        ccc: bytes = binary_converter.write_unsigned_int_be(len(cc))
        ccc += binary_converter.write_unsigned_byte(compression_type)
        ccc += cc
        i: int = 0
        while True:
            remaining: int = i - len(ccc)
            if remaining > 0:
                ccc += b"\x00" * remaining
                break
            i += 4096
        index_location_data: bytes = b""
        timestamp_data: bytes = b""
        chunks_data: bytes = b""
        temp_x: int = 0
        temp_z: int = 0
        offset: int = 2
        while temp_z < 256:
            if temp_x == x and temp_z == z:
                index_location_data += binary_converter.write_unsigned_triad_be(offset)
                index_location_data += binary_converter.write_unsigned_byte(len(ccc) >> 12)
                timestamp_data += binary_converter.write_unsigned_int(int(time.time()))
                chunks_data += ccc
                offset += len(ccc) >> 12
            else:
                index_location: int = self.get_location(temp_x, temp_z)
                file.seek(index_location)
                temp_offset: int = binary_converter.read_unsigned_triad_be(file.read(3))
                temp_sector_count: int = binary_converter.read_unsigned_byte(file.read(1))
                if temp_offset > 0 and temp_sector_count > 0:
                    index_location_data += binary_converter.write_unsigned_triad_be(offset)
                    index_location_data += binary_converter.write_unsigned_byte(temp_sector_count)
                    file.seek(index_location << 12)
                    timestamp_data += file.read(4)
                    file.seek(temp_offset << 12)
                    chunks_data += file.read(temp_sector_count << 12)
                    offset += temp_sector_count
                else:
                    index_location_data += b"\x00" * 4
                    timestamp_data += b"\x00" * 4
            if not temp_x < 256:
                temp_x: int = 0
                temp_z += 1
            temp_x += 1
        file.seek(0)
        file.write(index_location_data + timestamp_data + chunks_data)
        file.close()
