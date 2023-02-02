from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

ffmpeg_extract_subclip("test.mp4", 2, 18, targetname="test_fin.mp4")