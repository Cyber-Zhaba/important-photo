import os

URL_PREFIX = 'https://github.com/Cyber-Zhaba/important-photo/blob/master/data/'
URL_SUFFIX = '?raw=true'

def main():

    photos = []
    gifs = []

    for file in os.listdir('data'):
        if file.endswith('.gif'):
            gifs.append(file)
        else:
            photos.append(file)

    with open('README.md', 'w') as f:
        f.write('# Important photo\n\n')

        f.write('## Photos\n\n')
        for photo in photos:
            url = f'{URL_PREFIX}{photo}{URL_SUFFIX}'
            f.write(f'![{photo}]({url})\n')
        f.write('\n')

        f.write('## GIFs\n\n')
        for gif in gifs:
            url = f'{URL_PREFIX}{gif}{URL_SUFFIX}'
            f.write(f'![{gif}]({url})\n')
        f.write('\n')


if __name__ == '__main__':
    main()
    print("README.md generated successfully.")
