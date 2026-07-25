import imageio.v3 as iio

# Read all frames from the MP4
frames = iio.imread("output/output.mp4")

# Save as GIF
iio.imwrite(
    "output.gif",
    frames,
    duration=50,   # milliseconds per frame (≈20 FPS)
    loop=0
)
