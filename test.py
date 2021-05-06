from anvil.region import region

reg: object = region("./r.0.0.mca")
chunk: bytes = reg.get_chunk_data(0, 4)
reg.put_chunk_data(0, 4, chunk)
chunk: bytes = reg.get_chunk_data(0, 4)
print(chunk)
