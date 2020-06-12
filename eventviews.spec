#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : eventviews
Version  : 20.04.2
Release  : 25
URL      : https://download.kde.org/stable/release-service/20.04.2/src/eventviews-20.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.2/src/eventviews-20.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.2/src/eventviews-20.04.2.tar.xz.sig
Summary  : Library for creating events
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
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
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev

%description
No detailed description available

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
%setup -q -n eventviews-20.04.2
cd %{_builddir}/eventviews-20.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591934049
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1591934049
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/eventviews
cp %{_builddir}/eventviews-20.04.2/COPYING %{buildroot}/usr/share/package-licenses/eventviews/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/eventviews-20.04.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/eventviews/9a1929f4700d2407c70b507b3b2aaf6226a9543c
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
/usr/include/KF5/EventViews/AgendaView
/usr/include/KF5/EventViews/CalendarDecoration
/usr/include/KF5/EventViews/ConfigDialogInterface
/usr/include/KF5/EventViews/EventView
/usr/include/KF5/EventViews/Helper
/usr/include/KF5/EventViews/JournalView
/usr/include/KF5/EventViews/ListView
/usr/include/KF5/EventViews/MonthView
/usr/include/KF5/EventViews/MultiAgendaView
/usr/include/KF5/EventViews/Prefs
/usr/include/KF5/EventViews/TimeLineView
/usr/include/KF5/EventViews/TodoView
/usr/include/KF5/EventViews/ViewCalendar
/usr/include/KF5/EventViews/WhatsNextView
/usr/include/KF5/EventViews/eventview.h
/usr/include/KF5/EventViews/helper.h
/usr/include/KF5/EventViews/prefs.h
/usr/include/KF5/eventviews/EventView
/usr/include/KF5/eventviews/Helper
/usr/include/KF5/eventviews/Prefs
/usr/include/KF5/eventviews/agendaview.h
/usr/include/KF5/eventviews/calendardecoration.h
/usr/include/KF5/eventviews/configdialoginterface.h
/usr/include/KF5/eventviews/eventview.h
/usr/include/KF5/eventviews/eventviews_export.h
/usr/include/KF5/eventviews/helper.h
/usr/include/KF5/eventviews/journalview.h
/usr/include/KF5/eventviews/listview.h
/usr/include/KF5/eventviews/monthview.h
/usr/include/KF5/eventviews/multiagendaview.h
/usr/include/KF5/eventviews/prefs.h
/usr/include/KF5/eventviews/timelineview.h
/usr/include/KF5/eventviews/todoview.h
/usr/include/KF5/eventviews/viewcalendar.h
/usr/include/KF5/eventviews/whatsnextview.h
/usr/include/KF5/eventviews_version.h
/usr/lib64/cmake/KF5EventViews/KF5EventViewsConfig.cmake
/usr/lib64/cmake/KF5EventViews/KF5EventViewsConfigVersion.cmake
/usr/lib64/cmake/KF5EventViews/KF5EventViewsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5EventViews/KF5EventViewsTargets.cmake
/usr/lib64/libKF5EventViews.so
/usr/lib64/qt5/mkspecs/modules/qt_EventViews.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5EventViews.so.5
/usr/lib64/libKF5EventViews.so.5.14.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/eventviews/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/eventviews/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f libeventviews.lang
%defattr(-,root,root,-)

