Name:           deepin-compressor
Version:        5.8.0.14
Release:        1
Summary:        A fast and lightweight application for creating and extracting archives
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-devicemanager
Source0:        %{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-devel

BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(disomaster)
BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires: pkgconfig(dtkgui)
BuildRequires: pkgconfig(udisks2-qt5)
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-karchive-devel
BuildRequires: libzip-devel
BuildRequires: libarchive-devel
BuildRequires: minizip-devel

Requires: p7zip p7zip-plugins
Requires: lz4-libs
Requires: unrar
Requires: deepin-shortcut-viewer

%description
%{summary}.

%prep
%autosetup

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 ../ VERSION=%{version} DEFINES+="VERSION=%{version}"
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
/usr/lib/%{name}/plugins/*.so
%{_datadir}/deepin/dde-file-manager/oem-menuextensions/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Fri Jul 09 2021 weidong <weidong@uniontech.com> - 5.8.0.14-3
- Update 5.8.0.14

* Sat Jun 05 2021 weidong <weidong@uniontech.com> - 5.6.9-3
- Update Requires.

* Tue Sep 1 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.9-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.9-1
- Package init
