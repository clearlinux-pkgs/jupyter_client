#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_client
Version  : 6.0.0
Release  : 39
URL      : https://files.pythonhosted.org/packages/b9/ae/6abdd7d5df5a3af23b9c7ee1a509b7606eeb17f5857bb97de93bf92cf0dc/jupyter_client-6.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/ae/6abdd7d5df5a3af23b9c7ee1a509b7606eeb17f5857bb97de93bf92cf0dc/jupyter_client-6.0.0.tar.gz
Summary  : Jupyter protocol implementation and client libraries
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jupyter_client-bin = %{version}-%{release}
Requires: jupyter_client-license = %{version}-%{release}
Requires: jupyter_client-python = %{version}-%{release}
Requires: jupyter_client-python3 = %{version}-%{release}
Requires: jupyter_core
Requires: python-dateutil
Requires: pyzmq
Requires: tornado
Requires: traitlets
BuildRequires : buildreq-distutils3
BuildRequires : jupyter_core
BuildRequires : python-dateutil
BuildRequires : pyzmq
BuildRequires : tornado
BuildRequires : traitlets

%description
# Jupyter Client
[![Code Health](https://landscape.io/github/jupyter/jupyter_client/master/landscape.svg?style=flat)](https://landscape.io/github/jupyter/jupyter_client/master)

%package bin
Summary: bin components for the jupyter_client package.
Group: Binaries
Requires: jupyter_client-license = %{version}-%{release}

%description bin
bin components for the jupyter_client package.


%package license
Summary: license components for the jupyter_client package.
Group: Default

%description license
license components for the jupyter_client package.


%package python
Summary: python components for the jupyter_client package.
Group: Default
Requires: jupyter_client-python3 = %{version}-%{release}

%description python
python components for the jupyter_client package.


%package python3
Summary: python3 components for the jupyter_client package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyter_client package.


%prep
%setup -q -n jupyter_client-6.0.0
cd %{_builddir}/jupyter_client-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582560180
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter_client
cp %{_builddir}/jupyter_client-6.0.0/COPYING.md %{buildroot}/usr/share/package-licenses/jupyter_client/4864371bd27fe802d84990e2a5ee0d60bb29e944
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-kernel
/usr/bin/jupyter-kernelspec
/usr/bin/jupyter-run

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyter_client/4864371bd27fe802d84990e2a5ee0d60bb29e944

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
