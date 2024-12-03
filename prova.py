import time 

start = time.time()
print("ciao")
time.sleep(2)
end = time.time()

print(f"Tempo impiegato: {round(end-start, 5)}")

start = time.process_time()
print("ciao")
time.sleep(2)
end = time.process_time()

print(f"Tempo impiegato: {round(end-start, 5)}")