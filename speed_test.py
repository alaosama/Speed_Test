from speed_test import Speedtest

wifi = Speedtest()

print("Getting Dowload Speed ...")
dow,load = wifi.download()
print(f"Download: {download}")


print("Getting Upload Speed...")

upload = wifi.upload()
print(f"Upload: {upload}")

