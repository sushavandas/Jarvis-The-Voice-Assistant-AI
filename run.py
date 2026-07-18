# import multiprocessing
# import subprocess

# # To run Jarvis
# def startJarvis():
#         # Code for process 1
#         print("Process 1 is running.")
#         from main import start
#         start()

# # To run hotword
# def listenHotword():
#         # Code for process 2
#         print("Process 2 is running.")
#         from engine.features import hotword
#         hotword()

# # Start both processes
# if __name__ == '__main__':
#         p1 = multiprocessing.Process(target=startJarvis)
#         p2 = multiprocessing.Process(target=listenHotword)
#         p1.start()
#         p2.start()
#         p1.join()

#         if p2.is_alive():
#             p2.terminate()
#             p2.join()

#         print("system stop")

import sys
import os

if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")

if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")


def startJarvis():
    """Main UI + Eel process (MUST be main process)"""
    print("Jarvis UI starting...")
    from main import start
    start()


def listenHotword():
    """Background hotword listener"""
    print("Hotword listener starting...")
    from engine.features import hotword
    hotword()


if __name__ == "__main__":
    import multiprocessing

    multiprocessing.freeze_support()

    # Start hotword in background process
    hotword_process = multiprocessing.Process(
        target=listenHotword,
        daemon=True
    )
    hotword_process.start()

    # Run Eel / UI in main process
    startJarvis()

    # Cleanup
    if hotword_process.is_alive():
        hotword_process.terminate()
        hotword_process.join()

    print("System stopped")