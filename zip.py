import os
import time
import sys, warnings
import zipfile

# Проверка версии python
if sys.version_info[0] < 3:
    warnings.warn("Для выполнения этой программы необходима как минимум версия Python 3.0", RuntimeWarning)
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = sys.argv[2]

# 2. Каталог хранения резервной копии
target_dir = sys.argv[1]

try:
    os.mkdir(target_dir)
except OSError:
    print ("The directory %s already exist" % target_dir )
else:
    print ("Successfully created the directory %s " % target_dir)
target = target_dir + os.sep + time.strftime('%Y_%m_%d_%H%M') + '.zip'

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = { zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED:   'stored',
          }

print('creating archive')
zf = zipfile.ZipFile(target, mode='w')
for dirname, subdirs, files in os.walk(source):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename), compress_type=compression)
print('archive create complite')
zf.close()