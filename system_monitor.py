import psutil
import time
import os

while True:
	#Clear the screen
	os.system('clear')

	#Get system information
	cpu_usage = psutil.cpu_percent()
	mem_usage = psutil.virtual_memory().percent
	disk_usage = psutil.disk_usage('/').percent

	#Display system information
	print(f'CPU usage: {cpu_usage}%')
	print(f'Memory usage: {mem_usage}%')
	print(f'Disk usage: {disk_usage}%')

	#Sleep for 1 second before the next update
	time.sleep(1)

