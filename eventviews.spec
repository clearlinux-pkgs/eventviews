#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : eventviews
Version  : 23.04.0
Release  : 57
URL      : https://download.kde.org/stable/release-service/23.04.0/src/eventviews-23.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.0/src/eventviews-23.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.0/src/eventviews-23.04.0.tar.xz.sig
Summary  : Library for creating events
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
BuildRequires : akonadi-calendar-dev
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : calendarsupport-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kdiagram-dev
BuildRequires : kholidays-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libkdepim-dev
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

%prep
%setup -q -n eventviews-23.04.0
cd %{_builddir}/eventviews-23.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682038349
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1682038349
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/eventviews
cp %{_builddir}/eventviews-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/eventviews/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/eventviews-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/eventviews/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/eventviews-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/eventviews/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/eventviews-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/eventviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/eventviews-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/eventviews/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/eventviews-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/eventviews/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/eventviews-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/eventviews/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
