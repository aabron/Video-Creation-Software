from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
    
def overlay_videos(video_file, overlay_file, output_file):
    video1 = VideoFileClip(overlay_file, has_mask=True)
    video2 = VideoFileClip(video_file)
    video2 = video2.set_duration(video1.duration)

    final_clip = CompositeVideoClip([video1, video2], (1920, 1080),(101,220, 8) , True, True)
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

    video1.close()
    video2.close()





