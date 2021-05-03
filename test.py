x = 0
z = 0

while z < 256:
     print(f"{z} {x}")
     if not x < 256:
         x = 0
         z += 1
     x += 1
