pkgname = "python-pygit2"
pkgver = "1.20.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
]
makedepends = ["libgit2-devel", "python-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Python bindings for libgit2"
license = "GPL-2.0-only WITH GCC-exception-2.0"
url = "https://www.pygit2.org/index.html"
source = f"$(PYPI_SITE)/p/pygit2/pygit2-{pkgver}.tar.gz"
sha256 = "b52fb94c73664f383e6205955c80e228edee098ba37b9b94e46facc6333f102f"


def post_install(self):
    self.install_license("COPYING")
