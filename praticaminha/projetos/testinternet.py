import speedtest

st = speedtest.Speedtest()

st.get_best_server

dowload_speed = st.download() / 1_000_000

uplowd_speed = st.upload() / 1_000_000

ping = st.results.ping

print(f'Velocidade de download: {dowload_speed:.2f}')
print(f'Velocidade de Upload: {uplowd_speed:.2f}')
print(f'Ping: {ping}')
print(st.results.share())





















