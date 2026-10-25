pkgname = "python-audioread"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Cross-library audio decoding for Python"
license = "MIT"
url = "https://github.com/beetbox/audioread"
source = (
    f"https://github.com/beetbox/audioread/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "73a31af0d329e633d6166ff70cab31aec3e33b35c05c80d183337fcc2b417f42"
# needs working audio backends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
