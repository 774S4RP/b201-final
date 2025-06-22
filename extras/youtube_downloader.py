from pytube import YouTube

url = input("🎬 Please paste your YouTube video link: ")

try:
    yt = YouTube(url)
    yt.check_availability()

    print(f"📺 Video Title: {yt.title}")
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("✅ Download completed!")

except Exception as e:
    print("❌ An error occurred:", e)
    print("ℹ️ Try a different video link. Some YouTube videos have restrictions.")
