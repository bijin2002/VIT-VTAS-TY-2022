import os
import hashlib
import time

#clearing the chunks folder and creating it again
if os.path.exists("Chunks"):
    for filename in os.listdir("Chunks"):
        os.remove("./Chunks/"+filename)
else:
    os.mkdir("Chunks")

chunkSize = 64  # bytes
filePath = "College/time.jpg"

# File to open and break apart
fileR = open(filePath, "rb")

chunk = 0

byte = fileR.read(chunkSize)
print("Now splitting binary file")
while byte:
    # Open a temporary file and write a chunk of bytes
    fileN = "Chunks/chunkFile_" + str(chunk)
    fileT = open(fileN, "wb+")
    fileT.write(byte)
    fileT.close()

    # Read next 64 bytes
    byte = fileR.read(chunkSize)
    chunk += 1

print("Now finding duplicates")
time_MD5 = time.time()
# time_SHA1 = time.time()
# time_SHA256 = time.time()

for j in range(0, chunk):
     with open("Chunks/chunkFile_" +(str(j)), "rb") as f:
        data = f.read()
        with open("Hashes/MD5/hashFile_"+(str(j))+".txt", "wt+") as hash_file_MD5:
            hash_file_MD5.write(hashlib.md5(data).hexdigest())

dedupHashTable_MD5 = {}
for j in range(0, chunk):
    with open("Hashes/MD5/hashFile_"+(str(j))+".txt", "r") as f:
        data = f.read()
        if data in dedupHashTable_MD5:
            dedupHashTable_MD5[data].append(j)
        else:
            dedupHashTable_MD5[data] = [j]

print("Duplicates found using MD5: ")
for k in range(len(dedupHashTable_MD5)):
    if(len(dedupHashTable_MD5[list(dedupHashTable_MD5.keys())[k]])>1):
        print( list(dedupHashTable_MD5.keys())[k], " : ", dedupHashTable_MD5[list(dedupHashTable_MD5.keys())[k]])
end_MD5 = time.time()

print("Time taken for MD5: ", end_MD5-time_MD5 )