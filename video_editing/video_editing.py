from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
import cv2
    
def overlay_videos(video_file, overlay_file, output_file):
    video1 = VideoFileClip(overlay_file)
    video2 = VideoFileClip(video_file)
    video2.set_duration(video1.duration)

    final_clip = CompositeVideoClip([video1, video2], (1920, 1080),(101,220, 8) , True, True)
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

    video1.close()
    video2.close()
    
def overlay_transparent(video_file, overlay_file, output_file):
    tmp = cv2.VideoCapture(video_file)
    framesps = float(tmp.get(cv2.CAP_PROP_FPS))
    video1 = VideoFileClip(video_file, target_resolution=(1080, 1920))
    video2 = VideoFileClip(overlay_file, has_mask=True, target_resolution=(1080, 1920))
    
    final_video = CompositeVideoClip([video1, video2])
    
    final_video.write_videofile(
        output_file,
        fps=framesps,
        codec="mpeg4",
    )





