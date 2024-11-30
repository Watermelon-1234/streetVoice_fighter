import requests
import subprocess

id = input("請輸入歌曲id \n例如：\n \"https://streetvoice.com/api/v5/song/703692/hls/file/\"的id就是703692\n")

# Step 1: 發送 POST 請求取得 JSON
url = "https://streetvoice.com/api/v5/song/"+ id +"/hls/file/"
response = requests.post(url)

if response.status_code == 200:
    data = response.json()
    # 提取 .m3u8 的 URL
    m3u8_url = data.get("file")
    if m3u8_url:
        print(f".m3u8 文件 URL: {m3u8_url}")
        
        # Step 2: 使用 ffmpeg 下載並轉換 HLS
        output_file = "streetVoice_" + id + ".mp3"
        ffmpeg_command = [
            "ffmpeg",
            "-i", m3u8_url,       # 輸入 URL
            "-c", "copy",         # 保留原始音訊編碼
            output_file           # 輸出文件
        ]
        try:
            subprocess.run(ffmpeg_command, check=True)
            print(f"下載並轉換完成，保存為 {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"ffmpeg 運行失敗: {e}")
    else:
        print("無法從 JSON 中找到 'file' 屬性")
else:
    print(f"POST 請求失敗，HTTP 狀態碼: {response.status_code}")
