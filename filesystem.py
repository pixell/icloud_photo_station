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

    def item(self, filename):
        filepath = '/'.join((self.path, filename))
        if os.path.isfile(filepath):
            return FileSystemPhoto(filepath, os.path.getmtime(filepath))

    def create_item(self, filename, filetype, created, modified = None, filesize = None, title = None, description = None, rating = None, latitude = None, longitude = None):
        filepath = '/'.join((self.path, filename))
        return FileSystemPhoto(filepath, created)

class FileSystemPhoto(object):

    def __init__(self, path, created):
        self.path = path
        self.created = created

    def __str__(self):
        return self.path

    def merge(self):
        return os.path.isfile(self.path)

    def save_content(self, url):
        with open(self.path, 'wb') as file:
            for chunk in url.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        os.utime(self.path, (self.created / 1000,self.created / 1000))

    def delete(self):
        print ("Deleting %s!" % self.path)
        os.remove(self.path)
