import time

from queue import Queue
from threading import Thread

from classes.ApiWrapper import ApiWrapper


def main():
	queue = Queue()
	ApiWrapper(queue).start()
	while True:
		print(queue.get())

if __name__ == "__main__":
	main()
	# while True: time.sleep(1)