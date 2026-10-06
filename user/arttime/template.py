pkgname = "arttime"
pkgver = "2.5.0"
pkgrel = 0
makedepends = ["zsh"]
depends = ["zsh"]
pkgdesc = "Beauty of text-art meets functionality of a feature-rich clock/timer"
# the license's CFLA addendum makes it impossible to buy food with it as clock, weirdly enough (cf. clause d)
license = "GPL-3.0-only AND custom:arttime"
url = "https://github.com/poetaman/arttime"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7f90fb45232b7aef3831cde0f48c28d4eedc77d67edb7642f352c4b852624a1c"
# no tests, but 2400+ lines of zsh code. is that good? idk
options = ["!check"]


def install(self):
    # the provided install.sh script is buggy and too long for its rather simple job,
    # i can't figure out how to make it not spuriously error out.
    # hence do the install ourselves.
    self.install_files("bin", "usr", 0o755)
    self.install_files("share", "usr")
    for variant in ["CODE", "ART", "ADDENDUM_CFLA"]:
        self.install_license(f"LICENSE_{variant}")
