import setuptools

with open('README.md', 'r') as file:
	long_desc = file.read()

setuptools.setup(
	name = 'preprocess_text_jm', #unique package name
	version = '0.0.3',
	author = 'Jacek Malecki',
	author_email = 'jacmal86@gmail.com',
	describtion = 'This is preprocessin package',
	long_describtion = long_desc,
	long_describtion_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	'Operating Systems :: OS Independent'],
	python_requires = '>=3.5'
	)