import shutil, os
os.makedirs("/output", exist_ok=True)
shutil.copyfile("image.jpg", "/output/entry.jpg")
print("Wrote /output/entry.jpg")
