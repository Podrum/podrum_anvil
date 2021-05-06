from anvil.region import region
from nbt_utils.tag.compound_tag import compound_tag
from nbt_utils.utils.nbt_be_binary_stream import nbt_be_binary_stream

reg: object = region("./r.0.0.mca")
chunk: bytes = reg.get_chunk_data(0, 4)
reg.put_chunk_data(0, 4, chunk)
chunk: bytes = reg.get_chunk_data(0, 4)
stream: object = nbt_be_binary_stream(chunk)
tag: object = compound_tag()
tag.read(stream)
print(tag.get_tag("").get_tag("Level").value)
