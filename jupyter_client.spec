#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_client
Version  : 5.1.0
Release  : 9
URL      : https://pypi.debian.net/jupyter_client/jupyter_client-5.1.0.tar.gz
Source0  : https://pypi.debian.net/jupyter_client/jupyter_client-5.1.0.tar.gz
Summary  : Jupyter protocol implementation and client libraries
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jupyter_client-legacypython
Requires: jupyter_client-python
Requires: ipykernel
Requires: ipython
Requires: jupyter_core
Requires: pytest
Requires: python-dateutil
Requires: pyzmq
Requires: traitlets
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Jupyter Client
[![Code Health](https://landscape.io/github/jupyter/jupyter_client/master/landscape.svg?style=flat)](https://landscape.io/github/jupyter/jupyter_client/master)

%package legacypython
Summary: legacypython components for the jupyter_client package.
Group: Default

%description legacypython
legacypython components for the jupyter_client package.


%package python
Summary: python components for the jupyter_client package.
Group: Default
Requires: jupyter_client-legacypython

%description python
python components for the jupyter_client package.


%prep
%setup -q -n jupyter_client-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505004489
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505004489
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
