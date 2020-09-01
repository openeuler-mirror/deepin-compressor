%bcond_with check

%global with_debug 1
%if 0%{?with_debug}
%global debug_package   %{nil}
%endif


Name:           deepin-compressor
Version:        5.6.9
Release:        2
Summary:        Archive Manager is a fast and lightweight application for creating and extracting archives.
License:        GPLv3+
URL:            https://uos-packages.deepin.com/uos/pool/main/d/deepin-devicemanager/
Source0:        %{name}_%{version}.orig.tar.xz

BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  udisks2-qt5-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  kf5-kcodecs
BuildRequires:  kf5-kcodecs-devel
BuildRequires:  libarchive-devel
BuildRequires:  libarchive
BuildRequires:  kf5-karchive-devel
BuildRequires:  libzip-devel
BuildRequires:  qt5-linguist
BuildRequires:  libsecret-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  poppler-cpp
BuildRequires:  disomaster-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  zlib-devel

Requires: p7zip-plugins

%description
Archive Manager is a fast and lightweight application for creating and extracting archives.


%prep
%autosetup

%build
export PATH=$PATH:/usr/lib64/qt5/bin
mkdir build && cd build
%{_libdir}/qt5/bin/qmake ..
%{__make}

%install
pushd %{_builddir}/%{name}-%{version}/build
%make_install INSTALL_ROOT=%{buildroot}
popd


%files
%{_bindir}/%{name}
%{_datadir}/*
/usr/lib/*
%license LICENSE
%doc README.md


%changelog
* Tue Sep 1 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.9-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.9-1
- Package init
