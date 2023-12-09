from setuptools import Extension, setup

setup(
	ext_modules=[Extension(
		name="winfile",
		sources=["winfile.cpp"],
		language='c++'
	)]			
)