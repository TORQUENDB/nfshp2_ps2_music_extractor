# nfshp2_ps2_music_extractor
Utility to extract the ADPCM music tracks from the PS2 version of Need for Speed: Hot Pursuit 2 (only tested with US release)

Requirements:
Python 3.10+

.cl5 files from ZZDATA.BIN (instructions for extracting using 3rd party tools are below)


How to find and extract ZZDATA.BIN archive:

1. Copy ZDIR.BIN (SHA1: C3F68C904F6A9342443F96723E1873668EAF3C4D) and ZZDATA.BIN (SHA1: 72AC8E46357627ED2CC0D0AD8650D0B052C8D307) from the NFSHP2 folder on the Need for Speed: Hot Pursuit 2 game disc and place in the same folder on your computer
2. Download QuickBMS and the Nfsu Bun script from https://aluigi.altervista.org/quickbms.htm
3. Extract quickbms and run quickbms_4gb_files.exe
  3a. Select the nfsu_bun.bms file, the ZZDATA.BIN file you copied to your computer in step 1, and specify the directory to extract the files
4. If you've followed the instructions correctly, you should have 372 files, including 2 .cl5 files. They have nearly identical contents, but the larger file contains tracks with slightly higher bitrates (~1kbps)


Extracting the music tracks:

Run extract_nfshp2ps2_music.py. You can either pass the file path to one of the .cl5 files as an argument or enter it when the script prompts

The files have .vag extension and are PlayStation 4-bit ADPCM format. They can be played with many different utilties, I recommend https://github.com/vgmstream/vgmstream
