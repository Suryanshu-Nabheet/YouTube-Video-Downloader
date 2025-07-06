import os
import subprocess

def download_youtube_video(url, output_path='video'):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        print("Downloading using yt-dlp...")
        command = [
            'yt-dlp',
            '-f', 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
            '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
            url
        ]

        subprocess.run(command)
        print("✅ Download complete!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ").strip()
    download_youtube_video(url)
