# compress_config.py
COMPRESSED = False

COMPRESS_ALGORITHM = "gzip"
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
# COMPRESS_BRUTAL = True
COMPRESS_MIMETYPES = [
    "text/html",
    "text/css",
    "text/xml",
    "application/json",
    "application/javascript",
    "text/javascript",
    "application/octet-stream",
]
