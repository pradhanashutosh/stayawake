from PIL import Image

img = Image.new("RGB", (256, 256), color=(30, 144, 255))
img.save("icon.png")
img.save("icon.ico", format="ICO", sizes=[(256, 256)])
print("Icon created: icon.png, icon.ico")
