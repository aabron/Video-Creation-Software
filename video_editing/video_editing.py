from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

def edit_video(video_file, overlay_file, output_file):
    # Load the main video clip
    main_clip = VideoFileClip(video_file)

    # Load the overlay video clip
    overlay_clip = VideoFileClip(overlay_file).resize(main_clip.size)

    # Add the overlay clip to the main clip
    final_clip = concatenate_videoclips([main_clip, overlay_clip.set_duration(main_clip.duration)])

    # Write the final clip to the output file
    final_clip.write_videofile(output_file, codec='libx264')
