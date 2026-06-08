from sage.libs.gap.libgap import libgap
import tarfile, os

root = str(libgap.eval('GAPInfo.RootPaths[1]')).strip('"').rstrip('/')
pkg = root + '/pkg'
os.makedirs(pkg, exist_ok=True)
with tarfile.open('/tmp/ctbllib.tar.gz') as t:
    t.extractall(pkg)
print('CTblLib installed to', pkg)
