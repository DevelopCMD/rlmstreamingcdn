@echo OFF
for %%a in ("*.mp4") do extract.py "%%a"
cls
mkdir preview
move *.jpg "preview"