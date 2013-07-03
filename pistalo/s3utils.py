from storages.backends.s3boto import S3BotoStorage


class S3StaticStorage(S3BotoStorage):
    def url(self, name):
        url = super(S3StaticStorage, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url


StaticRootS3BotoStorage = lambda: S3StaticStorage(location='static')
MediaRootS3BotoStorage = lambda: S3BotoStorage()
