import requests
import json


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
	token = 'your_tokken'
	
	r = requests.get('https://api.vk.com/method/photos.get?v=5.52', params={'owner_id': your_id,
																			 'access_token': token, 
																			 'need_system': 1,
																			 'album_id': 'saved', #optional
																			 'photo_sizes': 1})
	write_json(r.json())


	images = json.load(open('response.json'))['response']['items']
	for image in images:
		sizes = image['sizes']
		max_size_pic = max(sizes, key=get_large)['src']
		download(max_size_pic)


if __name__ == '__main__':
	main()