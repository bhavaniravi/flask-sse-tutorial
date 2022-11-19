import sseclient

messages = sseclient.SSEClient("http://127.0.0.1:5000/stream", chunk_size=500000)

i = 0
for msg in messages:
    i += 1
    print("msg", i)
