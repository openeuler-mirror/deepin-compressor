%define specrelease 1

Name:           deepin-compressor
Version:        5.12.13
Release:        %{specrelease}
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
BuildRequires: dtkwidget-devel
BuildRequires: dtkcore-devel
BuildRequires: pkgconfig(dtkgui)
BuildRequires: pkgconfig(udisks2-qt5)
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-karchive-devel
BuildRequires: libzip-devel
BuildRequires: libarchive-devel
BuildRequires: minizip-devel
BuildRequires: poppler-cpp-devel
BuildRequires: gtest-devel gmock
BuildRequires: chrpath

Requires: p7zip
Requires: lz4-libs
Requires: deepin-shortcut-viewer
Requires: lzop
Recommends: unrar p7zip-plugins

%description
%{summary}.

%prep
%autosetup -p1

%build
export PATH=%{_qt5_bindir}:$PATH
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
sed -i "s|lib/|%_lib/|" CMakeLists.txt
sed -i "s|/usr/lib|%_libdir|" src/source/common/pluginmanager.cpp
mkdir build && pushd build 
%cmake -DCMAKE_BUILD_TYPE=Release ../  -DAPP_VERSION=%{version} -DVERSION=%{version} 
%make_build  
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

# remove rpath info
for file in $(find %{buildroot}/ -executable -type f -exec file {} ';' | grep "\<ELF\>" | awk -F ':' '{print $1}')
do
    if [ ! -u "$file" ]; then
        if [ -w $file ]; then
            chrpath -d $file
        fi
    fi
done

# add rpath path in ld.so.conf.d
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_bindir}/%{name}" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
echo "%{_libdir}/%{name}/plugins/" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%_libdir/%{name}/plugins/*.so
# %{_datadir}/deepin/dde-file-manager/oem-menuextensions/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/deepin-manual/manual-assets/application/deepin-compressor/archive-manager/*
%{_datadir}/applications/context-menus/*.conf
%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Fri Jul 28 2023 leeffo <liweiganga@uniontech.com> - 5.12.13-1
- upgrade to version 5.12.13

* Thu Mar 30 2023 liweiganga <liweiganga@uniontech.com> - 5.10.11-1
- update: update to 5.10.11

* Tue Mar 14 2023 liweigang <liweiganga@uniontech.com> - 5.10.5-3
- feat: remove rpath

* Fri Aug 05 2022 liweigang <liweiganga@uniontech.com> - 5.10.5-2
- fix nothing install requires

* Mon Jul 18 2022 konglidong <konglidong@uniontech.com> - 5.10.5-1
- update to 5.10.5

* Fri Feb 11 2022 liweigang <liweiganga@uniontech.com> - 5.8.0.14-2
- fix nothing install requires

* Fri Jul 09 2021 weidong <weidong@uniontech.com> - 5.8.0.14-1
- Update 5.8.0.14

* Sat Jun 05 2021 weidong <weidong@uniontech.com> - 5.6.9-3
- Update Requires.

* Tue Sep 1 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.9-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.9-1
- Package init

