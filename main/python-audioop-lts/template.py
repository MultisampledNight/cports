pkgname = "python-audioop-lts"
pkgver = "0.2.2"
pkgrel = 0
build_style = "python_pep517"
make_check_env = {"PYTHONPATH": "build/lib.linux-x86_64-cpython-314"}
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Manipulate raw audio data"
license = "PSF-2.0"
url = "https://github.com/AbstractUmbra/audioop"
source = f"$(PYPI_SITE)/a/audioop-lts/audioop_lts-{pkgver}.tar.gz"
sha256 = "64d0c62d88e67b98a1a5e71987b7aa7b5bcffc7dcee65b635823dbdd0a8dbbd0"


def check(self):
    self.do("pytest", env={"PYTHONPATH": "src"})
