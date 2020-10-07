from os.path import join
from hash_video import hash_video

def main():
    v1 = open(join('videos', '6.1.intro.mp4_download'), 'rb')
    v2 = open(join('videos', '6.2.birthday.mp4_download'), 'rb')
    assert(hash_video(v2.read()) == '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8')
    print hash_video(v1.read()) # "5b96aece304a1422224f9a41b228416028f9ba26b0d1058f400200f06a589949"
    v1.close()
    v2.close()
# main

if __name__ == '__main__':
    main()
# if