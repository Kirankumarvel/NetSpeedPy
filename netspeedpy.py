
import speedtest

# Initialize speed test object
st = speedtest.Speedtest()

# Perform tests
download = st.download() / 1024 / 1024  # Convert to Mbps
upload = st.upload() / 1024 / 1024      # Convert to Mbps
ping = st.results.ping                  # In milliseconds

# Display results
print(f"Download Speed: {download:.2f} Mbps")
print(f"Upload Speed: {upload:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")
