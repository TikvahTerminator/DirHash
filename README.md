# DirHash
*Tool to hash an entire directory of files as MD5 and SHA-512 and save to a Comma Seperated Values file.*

## Requirements
Dirhash requires the following:

 - glob
 - hashlib

## How to use
Clone or download the repo, then simply run:
```bash
python DirHash.py [Path to Directory]
```

Results will be output to a "*Results.csv*" file in the same directory as DirHash.py.
**NOTE**: DirHash doesn't like folders in your directories, so move files to a clean directory if necessary.
