import multiprocessing
import os
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s%')

def worker():
    logging.info(f"Chile process started. PID : {os.getpid()}")
    try:
        for i in range(10):
            logging.info(f"Child process running... {i+1}")

    except KeyboardInterrupt:
        logging.info("Child process interrupted.")
    finally:
        logging.info("Child process ending.")

if __name__ == "__main__":
    logging.info(f"Parent process started. PID: {os.getpid()}")

    process = multiprocessing.Process(target=worker)

    process.start()

    time.sleep(5)

    logging.info("Terminating the child process.")
    process.terminate()

    process.join()

    logging.info("Child process has been terminated")