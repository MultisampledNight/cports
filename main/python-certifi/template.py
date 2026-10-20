pkgname = "python-certifi"
pkgver = "2026.10.19"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["ca-certificates", "python"]
pkgdesc = "Python package for providing Mozilla's CA bundle"
license = "MPL-2.0"
url = "https://github.com/certifi/python-certifi"
source = f"$(PYPI_SITE)/c/certifi/certifi-{pkgver}.tar.gz"
sha256 = "035c1e85572b141bf1c3a3eff0e33a8eb74917522f2559075ff8d2fea780a1ae"
# no tests
options = ["!check"]
