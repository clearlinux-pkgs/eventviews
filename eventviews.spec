#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : eventviews
Version  : 22.04.0
Release  : 42
URL      : https://download.kde.org/stable/release-service/22.04.0/src/eventviews-22.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.0/src/eventviews-22.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.0/src/eventviews-22.04.0.tar.xz.sig
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
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcontacts-dev
BuildRequires : kdiagram-dev
BuildRequires : kguiaddons-dev
BuildRequires : kholidays-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kservice-dev
BuildRequires : libkdepim-dev
BuildRequires : qttools-dev

%description
SPDX-License-Identifier: CC0-1.0

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
%setup -q -n eventviews-22.04.0
cd %{_builddir}/eventviews-22.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650842143
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1650842143
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/eventviews
cp %{_builddir}/eventviews-22.04.0/.krazy.license %{buildroot}/usr/share/package-licenses/eventviews/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
cp %{_builddir}/eventviews-22.04.0/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/eventviews/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
cp %{_builddir}/eventviews-22.04.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/eventviews/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/eventviews-22.04.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/eventviews/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/eventviews-22.04.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/eventviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/eventviews-22.04.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/eventviews/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/eventviews-22.04.0/README.md.license %{buildroot}/usr/share/package-licenses/eventviews/cadc9e08cb956c041f87922de84b9206d9bbffb2
cp %{_builddir}/eventviews-22.04.0/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/eventviews/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang libeventviews

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservicetypes5/calendardecoration.desktop
/usr/share/qlogging-categories5/eventviews.categories
/usr/share/qlogging-categories5/eventviews.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/EventViews/EventViews/AgendaView
/usr/include/KF5/EventViews/EventViews/CalendarDecoration
/usr/include/KF5/EventViews/EventViews/ConfigDialogInterface
/usr/include/KF5/EventViews/EventViews/EventView
/usr/include/KF5/EventViews/EventViews/Helper
/usr/include/KF5/EventViews/EventViews/IncidenceTreeModel
/usr/include/KF5/EventViews/EventViews/JournalView
/usr/include/KF5/EventViews/EventViews/ListView
/usr/include/KF5/EventViews/EventViews/MonthView
/usr/include/KF5/EventViews/EventViews/MultiAgendaView
/usr/include/KF5/EventViews/EventViews/Prefs
/usr/include/KF5/EventViews/EventViews/TimeLineView
/usr/include/KF5/EventViews/EventViews/TodoModel
/usr/include/KF5/EventViews/EventViews/TodoView
/usr/include/KF5/EventViews/EventViews/ViewCalendar
/usr/include/KF5/EventViews/EventViews/WhatsNextView
/usr/include/KF5/EventViews/EventViews/eventview.h
/usr/include/KF5/EventViews/EventViews/helper.h
/usr/include/KF5/EventViews/EventViews/prefs.h
/usr/include/KF5/EventViews/eventviews/EventView
/usr/include/KF5/EventViews/eventviews/Helper
/usr/include/KF5/EventViews/eventviews/Prefs
/usr/include/KF5/EventViews/eventviews/agendaview.h
/usr/include/KF5/EventViews/eventviews/calendardecoration.h
/usr/include/KF5/EventViews/eventviews/configdialoginterface.h
/usr/include/KF5/EventViews/eventviews/eventview.h
/usr/include/KF5/EventViews/eventviews/eventviews_export.h
/usr/include/KF5/EventViews/eventviews/helper.h
/usr/include/KF5/EventViews/eventviews/incidencetreemodel.h
/usr/include/KF5/EventViews/eventviews/journalview.h
/usr/include/KF5/EventViews/eventviews/listview.h
/usr/include/KF5/EventViews/eventviews/monthview.h
/usr/include/KF5/EventViews/eventviews/multiagendaview.h
/usr/include/KF5/EventViews/eventviews/prefs.h
/usr/include/KF5/EventViews/eventviews/timelineview.h
/usr/include/KF5/EventViews/eventviews/todomodel.h
/usr/include/KF5/EventViews/eventviews/todoview.h
/usr/include/KF5/EventViews/eventviews/viewcalendar.h
/usr/include/KF5/EventViews/eventviews/whatsnextview.h
/usr/include/KF5/EventViews/eventviews_version.h
/usr/lib64/cmake/KF5EventViews/KF5EventViewsConfig.cmake
/usr/lib64/cmake/KF5EventViews/KF5EventViewsConfigVersion.cmake
/usr/lib64/cmake/KF5EventViews/KF5EventViewsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5EventViews/KF5EventViewsTargets.cmake
/usr/lib64/libKF5EventViews.so
/usr/lib64/qt5/mkspecs/modules/qt_EventViews.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5EventViews.so.5
/usr/lib64/libKF5EventViews.so.5.20.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/eventviews/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/eventviews/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/eventviews/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/eventviews/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/eventviews/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/eventviews/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/eventviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libeventviews.lang
%defattr(-,root,root,-)

