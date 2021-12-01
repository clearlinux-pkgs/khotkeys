#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : khotkeys
Version  : 5.23.4
Release  : 58
URL      : https://download.kde.org/stable/plasma/5.23.4/khotkeys-5.23.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.4/khotkeys-5.23.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: khotkeys-data = %{version}-%{release}
Requires: khotkeys-lib = %{version}-%{release}
Requires: khotkeys-license = %{version}-%{release}
Requires: khotkeys-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : plasma-workspace-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the khotkeys package.
Group: Data

%description data
data components for the khotkeys package.


%package dev
Summary: dev components for the khotkeys package.
Group: Development
Requires: khotkeys-lib = %{version}-%{release}
Requires: khotkeys-data = %{version}-%{release}
Provides: khotkeys-devel = %{version}-%{release}
Requires: khotkeys = %{version}-%{release}

%description dev
dev components for the khotkeys package.


%package doc
Summary: doc components for the khotkeys package.
Group: Documentation

%description doc
doc components for the khotkeys package.


%package lib
Summary: lib components for the khotkeys package.
Group: Libraries
Requires: khotkeys-data = %{version}-%{release}
Requires: khotkeys-license = %{version}-%{release}

%description lib
lib components for the khotkeys package.


%package license
Summary: license components for the khotkeys package.
Group: Default

%description license
license components for the khotkeys package.


%package locales
Summary: locales components for the khotkeys package.
Group: Default

%description locales
locales components for the khotkeys package.


%prep
%setup -q -n khotkeys-5.23.4
cd %{_builddir}/khotkeys-5.23.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638360110
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
export SOURCE_DATE_EPOCH=1638360110
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/khotkeys
cp %{_builddir}/khotkeys-5.23.4/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/khotkeys/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/khotkeys-5.23.4/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/khotkeys/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/khotkeys-5.23.4/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/khotkeys/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/khotkeys-5.23.4/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/khotkeys/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang khotkeys

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.khotkeys.xml
/usr/share/khotkeys/defaults.khotkeys
/usr/share/khotkeys/kde32b1.khotkeys
/usr/share/khotkeys/konqueror_gestures_kde321.khotkeys
/usr/share/kservices5/khotkeys.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KHotKeysDBusInterface/KHotKeysDBusInterfaceConfig.cmake

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/khotkeys/groups-comment.png
/usr/share/doc/HTML/ca/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/ca/kcontrol/khotkeys/manage-export.png
/usr/share/doc/HTML/ca/kcontrol/khotkeys/settings.png
/usr/share/doc/HTML/ca/kcontrol/khotkeys/shortcuts-action-command.png
/usr/share/doc/HTML/ca/kcontrol/khotkeys/shortcuts-action-dbus.png
/usr/share/doc/HTML/ca/kcontrol/khotkeys/shortcuts-action-keyboard.png
/usr/share/doc/HTML/ca/kcontrol/khotkeys/shortcuts-trigger-keyboard.png
/usr/share/doc/HTML/ca/kcontrol/khotkeys/shortcuts-trigger-mouse.png
/usr/share/doc/HTML/de/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/en/kcontrol/khotkeys/document-open.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/groups-comment.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/en/kcontrol/khotkeys/manage-export.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/oxygen-22x22-edit-clear-locationbar-rtl.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/settings.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/shortcuts-action-command.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/shortcuts-action-dbus.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/shortcuts-action-keyboard.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/shortcuts-trigger-keyboard.png
/usr/share/doc/HTML/en/kcontrol/khotkeys/shortcuts-trigger-mouse.png
/usr/share/doc/HTML/fr/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/id/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/id/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/it/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/nl/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/pt/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/ru/kcontrol/khotkeys/groups-comment.png
/usr/share/doc/HTML/ru/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/ru/kcontrol/khotkeys/manage-export.png
/usr/share/doc/HTML/ru/kcontrol/khotkeys/settings.png
/usr/share/doc/HTML/ru/kcontrol/khotkeys/shortcuts-action-command.png
/usr/share/doc/HTML/ru/kcontrol/khotkeys/shortcuts-action-dbus.png
/usr/share/doc/HTML/ru/kcontrol/khotkeys/shortcuts-action-keyboard.png
/usr/share/doc/HTML/ru/kcontrol/khotkeys/shortcuts-trigger-keyboard.png
/usr/share/doc/HTML/ru/kcontrol/khotkeys/shortcuts-trigger-mouse.png
/usr/share/doc/HTML/sv/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/uk/kcontrol/khotkeys/groups-comment.png
/usr/share/doc/HTML/uk/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/khotkeys/index.docbook
/usr/share/doc/HTML/uk/kcontrol/khotkeys/manage-export.png
/usr/share/doc/HTML/uk/kcontrol/khotkeys/settings.png
/usr/share/doc/HTML/uk/kcontrol/khotkeys/shortcuts-action-command.png
/usr/share/doc/HTML/uk/kcontrol/khotkeys/shortcuts-action-dbus.png
/usr/share/doc/HTML/uk/kcontrol/khotkeys/shortcuts-action-keyboard.png
/usr/share/doc/HTML/uk/kcontrol/khotkeys/shortcuts-trigger-keyboard.png
/usr/share/doc/HTML/uk/kcontrol/khotkeys/shortcuts-trigger-mouse.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkhotkeysprivate.so.5
/usr/lib64/libkhotkeysprivate.so.5.23.4
/usr/lib64/qt5/plugins/kcm_hotkeys.so
/usr/lib64/qt5/plugins/kf5/kded/khotkeys.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/khotkeys/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/khotkeys/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/khotkeys/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f khotkeys.lang
%defattr(-,root,root,-)

