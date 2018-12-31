clean:
	-rm -rf build
	-rm -rf dist
	-rm -rf *.egg-info
	-rm -f tests/.coverage

build: clean
	python setup.py bdist_wheel --universal

uninstall:
	-pip uninstall -y vlab-mgr

install: uninstall build
	pip install -U dist/*.whl

test: uninstall install
	cd tests && nosetests -v --with-coverage --cover-package=vlab_mgr
