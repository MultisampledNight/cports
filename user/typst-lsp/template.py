pkgname = "typst-lsp"
pkgver = "0_git20261007"
_rev = "d29e19159688be4d0309341eb4e9fd5eefbb8358"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=remote-packages,native-tls,fontconfig",
]
make_build_env = {"VERGEN_GIT_DESCRIBE": pkgver}
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel"]
depends = ["typst"]
pkgdesc = "Language server for Typst without slop"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/schrottkatze/typst-lsp"
source = f"{url}/archive/{_rev}.tar.gz"
sha256 = "f41bcba07163bbc417509b2e447499ca00b668bbb1c50a930fb7d494113087e8"
hardening = ["vis", "cfi"]
# hahahaAAAA [starts crying]
options = ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "typst-lsp"))
    for variant in license.split(" OR "):
        self.install_license(f"LICENSE-{variant}.txt")
