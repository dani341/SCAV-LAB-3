import os
import subprocess
import tkinter



def stream_exercise_1():
    #from https://ottverse.com/hls-packaging-using-ffmpeg-live-vod/
    subprocess.call("ffmpeg -i bbb_160x120.mp4 \
        -filter_complex \
        '[0:v]split=3[v1][v2][v3]; \
        [v1]copy[v1out]; [v2]scale=w=1280:h=720[v2out]; [v3]scale=w=640:h=360[v3out]' \
        -map [v1out] -c:v:0 libx264 -x264-params 'nal-hrd=cbr:force-cfr=1' -b:v:0 5M -maxrate:v:0 5M -minrate:v:0 5M -bufsize:v:0 10M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map [v2out] -c:v:1 libx264 -x264-params 'nal-hrd=cbr:force-cfr=1' -b:v:1 3M -maxrate:v:1 3M -minrate:v:1 3M -bufsize:v:1 3M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map [v3out] -c:v:2 libx264 -x264-params 'nal-hrd=cbr:force-cfr=1' -b:v:2 1M -maxrate:v:2 1M -minrate:v:2 1M -bufsize:v:2 1M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map a:0 -c:a:0 aac -b:a:0 96k -ac 2 \
        -map a:0 -c:a:1 aac -b:a:1 96k -ac 2 \
        -map a:0 -c:a:2 aac -b:a:2 48k -ac 2 \
        -f hls \
        -hls_time 2 \
        -hls_playlist_type vod \
        -hls_flags independent_segments \
        -hls_segment_type mpegts \
        -hls_segment_filename stream_%v/data%02d.ts \
        -master_pl_name master.m3u8 \
        -var_stream_map 'v:0,a:0 v:1,a:1 v:2,a:2' stream_%v.m3u8", shell=True)

stream_exercise_1()


def stream_exercise_2():
    #fragment
    subprocess.call("$ mp4fragment --fragment-duration 15 bbb_160x120.mp4.mp4 bbb_160x120_frag.mp4", shell=True)
    #encrypt
    subprocess.call(f"mp4encrypt --method MPEG-CENC \
        --key 1:1234567890123456:12345678901234567890123456789012 \
        bbb_160x120_frag.mp4 bbb_160x120_frag_encrypted.mp4", shell=True)
    #dash
    subprocess.call("$ mp4dash --mpd-name myvideo.mpd bbb_160x120_frag_encrypted.mp4", shell=True)
    subprocess.call(f"mp4dash bbb_160x120_frag_encrypted.mp4", shell=True)

stream_exercise_2()

def stream_exercise_3():
    #from https://ottverse.com/hls-packaging-using-ffmpeg-live-vod/
    subprocess.call("ffmpeg -i bbb_160x120.mp4 \
        -filter_complex \
        '[0:v]split=3[v1][v2][v3]; \
        [v1]copy[v1out]; [v2]scale=w=1280:h=720[v2out]; [v3]scale=w=640:h=360[v3out]' \
        -map [v1out] -c:v:0 libx264 -x264-params 'nal-hrd=cbr:force-cfr=1' -b:v:0 5M -maxrate:v:0 5M -minrate:v:0 5M -bufsize:v:0 10M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map [v2out] -c:v:1 libx264 -x264-params 'nal-hrd=cbr:force-cfr=1' -b:v:1 3M -maxrate:v:1 3M -minrate:v:1 3M -bufsize:v:1 3M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map [v3out] -c:v:2 libx264 -x264-params 'nal-hrd=cbr:force-cfr=1' -b:v:2 1M -maxrate:v:2 1M -minrate:v:2 1M -bufsize:v:2 1M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map a:0 -c:a:0 aac -b:a:0 96k -ac 2 \
        -map a:0 -c:a:1 aac -b:a:1 96k -ac 2 \
        -map a:0 -c:a:2 aac -b:a:2 48k -ac 2 \
        -f hls \
        -hls_time 2 \
        -hls_list_size 2\
        -hls_flags independent_segments \
        -hls_segment_type mpegts \
        -hls_segment_filename stream_%v/data%02d.ts \
        -master_pl_name master.m3u8 \
        -var_stream_map 'v:0,a:0 v:1,a:1 v:2,a:2' stream_%v.m3u8", shell=True)

stream_exercise_3()
