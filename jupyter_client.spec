#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_client
Version  : 7.0.3
Release  : 60
URL      : https://files.pythonhosted.org/packages/db/96/4bc30e91d14abb3b459e15b86d25039a12ebc75df963b3005aa713d360bb/jupyter_client-7.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/db/96/4bc30e91d14abb3b459e15b86d25039a12ebc75df963b3005aa713d360bb/jupyter_client-7.0.3.tar.gz
Summary  : Jupyter protocol implementation and client libraries
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyter_client-bin = %{version}-%{release}
Requires: jupyter_client-license = %{version}-%{release}
Requires: jupyter_client-python = %{version}-%{release}
Requires: jupyter_client-python3 = %{version}-%{release}
Requires: entrypoints
Requires: jupyter_core
Requires: python-dateutil
Requires: pyzmq
Requires: tornado
Requires: traitlets
BuildRequires : buildreq-distutils3
BuildRequires : entrypoints
BuildRequires : python-dateutil
BuildRequires : pyzmq
BuildRequires : tornado
BuildRequires : traitlets

%description
# Jupyter Client
[![Build Status](https://github.com/jupyter/jupyter_client/workflows/CI/badge.svg)](https://github.com/jupyter/jupyter_client/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
Provides: pypi(jupyter_client)
Requires: pypi(entrypoints)
Requires: pypi(jupyter_core)
Requires: pypi(nest_asyncio)
Requires: pypi(python_dateutil)
Requires: pypi(pyzmq)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the jupyter_client package.


%prep
%setup -q -n jupyter_client-7.0.3
cd %{_builddir}/jupyter_client-7.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631891793
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter_client
cp %{_builddir}/jupyter_client-7.0.3/COPYING.md %{buildroot}/usr/share/package-licenses/jupyter_client/8fd549f28c3423c251b3b70e91bdad2fbfe6ef30
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
/usr/share/package-licenses/jupyter_client/8fd549f28c3423c251b3b70e91bdad2fbfe6ef30

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
