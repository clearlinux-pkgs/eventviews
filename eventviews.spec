#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : eventviews
Version  : 24.12.1
Release  : 110
URL      : https://download.kde.org/stable/release-service/24.12.1/src/eventviews-24.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.1/src/eventviews-24.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.1/src/eventviews-24.12.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Library for creating events
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: eventviews-data = %{version}-%{release}
Requires: eventviews-lib = %{version}-%{release}
Requires: eventviews-license = %{version}-%{release}
Requires: eventviews-locales = %{version}-%{release}
BuildRequires : akonadi-calendar-dev
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : calendarsupport-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kdiagram-dev
BuildRequires : kholidays-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libkdepim-dev
BuildRequires : qt6base-dev
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

%package data
Summary: data components for the eventviews package.
Group: Data

%description data
data components for the eventviews package.


%package dev
Summary: dev components for the eventviews package.
Group: Development
Requires: eventviews-lib = %{version}-%{release}
Requires: eventviews-data = %{version}-%{release}
Provides: eventviews-devel = %{version}-%{release}
Requires: eventviews = %{version}-%{release}

%description dev
dev components for the eventviews package.


%package lib
Summary: lib components for the eventviews package.
Group: Libraries
Requires: eventviews-data = %{version}-%{release}
Requires: eventviews-license = %{version}-%{release}

%description lib
lib components for the eventviews package.


%package license
Summary: license components for the eventviews package.
Group: Default

%description license
license components for the eventviews package.


%package locales
Summary: locales components for the eventviews package.
Group: Default

%description locales
locales components for the eventviews package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n eventviews-24.12.1
cd %{_builddir}/eventviews-24.12.1
pushd ..
cp -a eventviews-24.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736783854
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1736783854
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/eventviews
cp %{_builddir}/eventviews-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/eventviews/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/eventviews-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/eventviews/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/eventviews-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/eventviews/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/eventviews-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/eventviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/eventviews-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/eventviews/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/eventviews-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/eventviews/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libeventviews6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/eventviews.categories
/usr/share/qlogging-categories6/eventviews.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/EventViews/EventViews/AgendaView
/usr/include/KPim6/EventViews/EventViews/CalendarDecoration
/usr/include/KPim6/EventViews/EventViews/ConfigDialogInterface
/usr/include/KPim6/EventViews/EventViews/EventView
/usr/include/KPim6/EventViews/EventViews/Helper
/usr/include/KPim6/EventViews/EventViews/JournalView
/usr/include/KPim6/EventViews/EventViews/ListView
/usr/include/KPim6/EventViews/EventViews/MonthView
/usr/include/KPim6/EventViews/EventViews/MultiAgendaView
/usr/include/KPim6/EventViews/EventViews/Prefs
/usr/include/KPim6/EventViews/EventViews/TimeLineView
/usr/include/KPim6/EventViews/EventViews/TodoView
/usr/include/KPim6/EventViews/EventViews/ViewCalendar
/usr/include/KPim6/EventViews/EventViews/WhatsNextView
/usr/include/KPim6/EventViews/EventViews/eventview.h
/usr/include/KPim6/EventViews/EventViews/helper.h
/usr/include/KPim6/EventViews/EventViews/prefs.h
/usr/include/KPim6/EventViews/eventviews/EventView
/usr/include/KPim6/EventViews/eventviews/Helper
/usr/include/KPim6/EventViews/eventviews/Prefs
/usr/include/KPim6/EventViews/eventviews/agendaview.h
/usr/include/KPim6/EventViews/eventviews/calendardecoration.h
/usr/include/KPim6/EventViews/eventviews/configdialoginterface.h
/usr/include/KPim6/EventViews/eventviews/eventview.h
/usr/include/KPim6/EventViews/eventviews/eventviews_export.h
/usr/include/KPim6/EventViews/eventviews/helper.h
/usr/include/KPim6/EventViews/eventviews/journalview.h
/usr/include/KPim6/EventViews/eventviews/listview.h
/usr/include/KPim6/EventViews/eventviews/monthview.h
/usr/include/KPim6/EventViews/eventviews/multiagendaview.h
/usr/include/KPim6/EventViews/eventviews/prefs.h
/usr/include/KPim6/EventViews/eventviews/timelineview.h
/usr/include/KPim6/EventViews/eventviews/todoview.h
/usr/include/KPim6/EventViews/eventviews/viewcalendar.h
/usr/include/KPim6/EventViews/eventviews/whatsnextview.h
/usr/include/KPim6/EventViews/eventviews_version.h
/usr/lib64/cmake/KPim6EventViews/KPim6EventViewsConfig.cmake
/usr/lib64/cmake/KPim6EventViews/KPim6EventViewsConfigVersion.cmake
/usr/lib64/cmake/KPim6EventViews/KPim6EventViewsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6EventViews/KPim6EventViewsTargets.cmake
/usr/lib64/libKPim6EventViews.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6EventViews.so.6.3.1
/usr/lib64/libKPim6EventViews.so.6
/usr/lib64/libKPim6EventViews.so.6.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/eventviews/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/eventviews/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/eventviews/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/eventviews/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/eventviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libeventviews6.lang
%defattr(-,root,root,-)

