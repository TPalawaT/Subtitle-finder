from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import exit

video_formats = ['webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'drc', 'gif', 'gifv', 'mng', 'avi', 'mts', 'm2ts', 'mov', 'qt', 'wmv', 'yuv', 'rm', 'rmvb', 'asf', 'amv', 'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'm2v', 'm4v', 'svi', '3gp', '3g2', 'mxf', 'roq', 'nsv', 'flv', 'f4v', 'f4p', 'f4a', 'f4b']
audio_formats = ['3gp', 'aa', 'aac', 'aax', 'act', 'aiff', 'amr', 'ape', 'au', 'awb', 'dct', 'dss', 'dvf', 'flac', 'gsm', 'iklax', 'ivs', 'm4a', 'm4b', 'm4p', 'mmf', 'mp3', 'mpc', 'msv', 'nmf', 'nsf', 'ogg', 'oga', 'mogg', 'opus', 'ra', 'rm', 'raw', 'sln', 'tta', 'vox', 'wav', 'wma', 'wv', 'webm', '8svx']

for i in range(len(video_formats)-1):
	k=i+1
	for j in range(k,len(video_formats)):
		if video_formats[i] == video_formats[k]:
			del video_formats[k]

for i in range(len(audio_formats)-1):
	k=i+1
	for j in range(k,len(audio_formats)):
		if audio_formats[i] == audio_formats[k]:
			del audio_formats[k]

temp_a = set(audio_formats)
temp_v = set(video_formats)
audio_video_foramts = list(temp_a.intersection(temp_v))

loc = input("Enter address of the file: ").split('\\')
file_name = loc[-1]
file  = loc[-1].split('.')
file_type = file[-1]

file_type = file_type.lower()

result = 'NaN'

for i in video_formats:
	if file_type == i:
		result = 'v'

if result == 'v':
	for j in audio_video_foramts:
		if file_type == str(j):
			result = 'av'

if result == 'NaN':				
	for k in audio_formats:
		if file_type == k:
			result = 'a'

if result == 'NaN':
	print("File type not recognized")
	exit()

print(result)

driver = webdriver.Firefox()

if result == 'v':
	driver.get("http://www.moviesubtitles.org/movies.html")
	main_window = driver.current_window_handle
	search_movie = driver.find_element_by_class_name('search')
	search_movie.clear()
	search_movie.send_keys(file_name)
	search_movie.send_keys(Keys.ENTER)

	driver.execute_script("window.open();")
	driver.switch_to_window(driver.window_handles[1])
	driver.get("http://www.tvsubtitles.net/")
	search_tv = driver.find_element_by_class_name('search')
	search_tv.clear()
	search_tv.send_keys(file_name)
	search_tv.send_keys(Keys.ENTER)

elif result == 'a':
	driver.get("http://www.mldb.org/search")
	driver.find_element_by_id('mmany').click()
	search_song = driver.find_element_by_id('mq')
	search_song.clear()
	search_song.send_keys(file_name)
	search_song.send_keys(Keys.ENTER)

elif result == 'av':
	driver.get("http://www.moviesubtitles.org/movies.html")
	main_window = driver.current_window_handle
	search_movie = driver.find_element_by_class_name('search')
	search_movie.clear()
	search_movie.send_keys(file_name)
	search_movie.send_keys(Keys.ENTER)

	driver.execute_script("window.open();")
	driver.switch_to_window(driver.window_handles[1])
	driver.get("http://www.tvsubtitles.net/")
	search_tv = driver.find_element_by_class_name('search')
	search_tv.clear()
	search_tv.send_keys(file_name)
	search_tv.send_keys(Keys.ENTER)

	driver.execute_script("window.open();")
	driver.switch_to_window(driver.window_handles[2])
	driver.get("http://www.mldb.org/search")
	driver.find_element_by_id('mmany').click()
	search_song = driver.find_element_by_id('mq')
	search_song.clear()
	search_song.send_keys(file_name)
	search_song.send_keys(Keys.ENTER)