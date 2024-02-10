from sys import platform
from setuptools import Extension, setup

if platform.startswith("linux"):
	setup(
		ext_modules=[
			Extension(
				name="linfile",
				sources=["linfile.cpp"],
				language='c++',
				extra_objects=["linsys.o"]
			),
			Extension(
				name="connector",
				sources=["connector.cpp"],
				language='c++'
			)
		]
	)
elif platform == "win32":
	setup(
		ext_modules=[
			Extension(
				name="winfile",
				sources=["winfile.cpp"],
				language='c++'
			)
		]
	)
else:
	raise RuntimeError('Platform is not supported!')