import time

from queue import Queue
from threading import Thread

from classes.ApiWrapper import ApiWrapper
from classes.RobotWrapper import RobotWrapper


def main():
	queue = Queue()
	ApiWrapper(queue).start()
	RobotWrapper(queue).start()

if __name__ == "__main__":
	main()
	# while True: time.sleep(1)