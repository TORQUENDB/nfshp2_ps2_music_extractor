import os
import sys

class Track:
    def __init__(self,title,audio_start,audio_length):
        self.title = title
        self.audio_start = audio_start
        self.audio_length = audio_length

def main(args=None):
    if args is None or len(args) < 2:
        cl5 = input("Enter location of NFSHP2 CL5 archive file: ").strip("\"'")
    else:
        cl5 = args[1]
    if not os.path.exists(cl5):
        return 1
    file_data = open(cl5,"rb").read()
    
    curr_offset = int("0x60",16)

    file_info = []

    while True:
        audio_start = int.from_bytes(file_data[curr_offset:(curr_offset := curr_offset+4)],"little")
        audio_length = int.from_bytes(file_data[curr_offset:(curr_offset := curr_offset+4)], "little")
        
        title_info_start = curr_offset + 4
        while True:
            if file_data[curr_offset:(curr_offset := curr_offset+4)] == b'\xcc\xcc\xcc\xcc':
                title_info_end = curr_offset-4
                break
        
        title = bytes.decode(file_data[title_info_start:title_info_end], "ascii").split('\x00')[0]
        print(title)

        while True:
            if file_data[curr_offset:(curr_offset := curr_offset+4)] == b'\xcc\xcc\xcc\x00':
                break
        
        file_info.append(Track(title,audio_start,audio_length))

        if file_data[curr_offset:curr_offset+1] != b'\xd0': #All audio data addresses start with D0
            break

    for track in file_info:
        with open(f"{track.title}.vag","wb") as track_output:
            track_output.write(file_data[track.audio_start:track.audio_start+track.audio_length])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))