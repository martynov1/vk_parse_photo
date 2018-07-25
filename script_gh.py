import requests
import json
import timeit
import os

def write_json(data):
	with open('response.json', 'w', encoding='utf-8') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


def get_large(size_dict):
	if size_dict['height'] >= size_dict['width']:
		return size_dict['height']
	else:
		return size_dict['width']


def download(url):	
	

	r = requests.get(url, stream=True)
	filename = url.split('/')[-1]
	
	with open(filename, 'bw') as file:
		for chunk in r.iter_content():
			file.write(chunk)


def main():
	start = timeit.default_timer()
	
<<<<<<< HEAD
	token = 'YOUR_TOKKEN'
	
	r = requests.get('https://api.vk.com/method/photos.get?v=5.52', params={'owner_id': YOUR_ID,
																			'access_token': token, 
																			'need_system': 1,
																			'album_id': 'saved', #optional
																			'photo_sizes': 1})
=======
	r = requests.get('https://api.vk.com/method/photos.get?v=5.52', params={'owner_id': your_id,
									        'access_token': token, 
				                                		'need_system': 1,
										'album_id': 'saved', #optional
										'photo_sizes': 1})
>>>>>>> 79385f9c72b73a6e42becedaa8452f4c71053c66
	write_json(r.json())
	
	

	images = json.load(open('response.json'))['response']['items']
	count = json.load(open('response.json'))['response']['count']
	
	os.mkdir('.\images')
	os.chdir('.\images')	
	
	for image in images:
		sizes = image['sizes']
		max_size_pic = max(sizes, key=get_large)['src']
		download(max_size_pic)
	
	stop = timeit.default_timer()
	
	print('Load time: ', stop - start)
	print('Download {} files'.format(count))


if __name__ == '__main__':
	main()
