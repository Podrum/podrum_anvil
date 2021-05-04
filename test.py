from region import region

reg = region("./r.0.0.mca")
chunk = reg.get_chunk(0, 4)
reg.put_chunk(0, 4, chunk)
chunk = reg.get_chunk(0, 4)
print(chunk)
