import threading

print("Current Thread running: " + threading.current_thread().getName())

if(threading.current_thread == threading.main_thread()):
    print("main Thread")
else:
    print("some other thread")
