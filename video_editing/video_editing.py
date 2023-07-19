from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
import moviepy.video.compositing.transitions as transfx
import numpy as np

def edit_video(video_file, overlay_file, output_file):
    main_clip = VideoFileClip(video_file).subclip(2, -2)
    overlay_clip = VideoFileClip(overlay_file).resize(main_clip.size)
    
    green_screen = (0, 255, 0)  # Green color for the green screen
    mask = overlay_clip.fl_image(lambda frame: np.where(frame.min(axis=-1) > 100, frame, green_screen))
    
    final_clip = CompositeVideoClip([main_clip.set_mask(mask, mask_color=green_screen)])
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')







