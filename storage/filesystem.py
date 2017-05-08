import os

class FileSystemStorage(object):

    def __init__(self, root):
        self.root = root.rstrip('/')

    def __str__(self):
        return self.root

    def album(self, path, create):
        album = '/'.join((self.root, path))

        if not os.path.exists(album):
            if create:
                os.makedirs(album)
            else:
                return False

        return FileSystemAlbum(album)

class FileSystemAlbum(object):

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def photo(self, filename):
        filepath = '/'.join((self.path, filename))

        return FileSystemPhoto(filepath)

class FileSystemPhoto(object):

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def exists(self):
        return os.path.isfile(self.path)

    def create(self, url):
        with open(self.path, 'wb') as file:
            for chunk in url.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

    def delete(self):
        if exists():
            print "Deleting %s!" % self.path
            os.remove(self.path)
