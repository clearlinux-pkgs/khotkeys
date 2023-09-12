#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : khotkeys
Version  : 5.27.8
Release  : 88
URL      : https://download.kde.org/stable/plasma/5.27.8/khotkeys-5.27.8.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.8/khotkeys-5.27.8.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.8/khotkeys-5.27.8.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0
Requires: khotkeys-data = %{version}-%{release}
Requires: khotkeys-lib = %{version}-%{release}
Requires: khotkeys-license = %{version}-%{release}
Requires: khotkeys-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kglobalaccel-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : plasma-workspace-dev
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n khotkeys-5.27.8
cd %{_builddir}/khotkeys-5.27.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694546548
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1694546548
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/khotkeys
cp %{_builddir}/khotkeys-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/khotkeys/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/khotkeys-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/khotkeys/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/khotkeys-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/khotkeys/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/khotkeys-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/khotkeys/20079e8f79713dce80ab09774505773c926afa2a || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang khotkeys
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/share/doc/HTML/tr/kcontrol/khotkeys/index.cache.bz2
/usr/share/doc/HTML/tr/kcontrol/khotkeys/index.docbook
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
/V3/usr/lib64/libkhotkeysprivate.so.5.27.8
/V3/usr/lib64/qt5/plugins/kcm_hotkeys.so
/V3/usr/lib64/qt5/plugins/kf5/kded/khotkeys.so
/usr/lib64/libkhotkeysprivate.so.5
/usr/lib64/libkhotkeysprivate.so.5.27.8
/usr/lib64/qt5/plugins/kcm_hotkeys.so
/usr/lib64/qt5/plugins/kf5/kded/khotkeys.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/khotkeys/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/khotkeys/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/khotkeys/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f khotkeys.lang
%defattr(-,root,root,-)

