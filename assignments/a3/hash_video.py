from sys import path
path.append('..')
from common import get_blocks, sha_256

# Hashing in reverse allows the server to publicize just one checksum.
# Otherwise, it would have to provide a checksum for each video block.
def hash_video(video):
    blocks = get_blocks(video, pad=False, block_size=1024)
    h = ''
    for block in reversed(blocks):
        h = sha_256(block + h.decode('hex'))
    # for
    return h
# hash_video