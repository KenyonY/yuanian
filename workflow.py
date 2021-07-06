from sparrow.version_ops import VersionControl


pkgname = "yuanian"
pkgdir = pkgname
vc = VersionControl(pkgname, pkgdir)
vc.update_version(version_step=1)
vc.update_readme(license="GNU_GPL--V3")
# os.system(f"yapf -i -r ./{pkgdir}")
vc.upload_pypi(pkgname)
