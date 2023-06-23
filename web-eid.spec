%global _hardened_build 1
%define debug_package %{nil}

Name:    web-eid
Version: 2.3.1
Release: 7
Summary: Web eID browser extension helper application
License: MIT
URL:     https://github.com/web-eid/web-eid-app
Source0: %{name}-%{version}.tar.gz
Patch0:  https://github.com/web-eid/libpcsc-mock/commit/488cb42301a42d8ced964a0aaafe4be0d258126d.patch

BuildRequires: bash
BuildRequires: desktop-file-utils
BuildRequires: git
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-devel
BuildRequires: pcsc-lite
BuildRequires: pcsc-lite-devel
BuildRequires: clang
BuildRequires: git-clang-format
BuildRequires: valgrind
BuildRequires: gtest
BuildRequires: gtest-devel
BuildRequires: openssl-devel

Requires: hicolor-icon-theme
Requires: libstdc++
Requires: mozilla-filesystem
Requires: openssl-libs
Requires: pcsc-lite-libs
Requires: qt5-qtbase
Requires: qt5-qtsvg

%description
The Web eID application performs cryptographic digital signing and authentication
operations with electronic ID smart cards for the Web eID browser extension (it
is the native messaging host for the extension). Also works standalone without
the extension in command-line mode.

%prep
%autosetup -N
%patch0 -p 1 -d web-eid-app/lib/libelectronic-id/lib/libpcsc-cpp/tests/lib/libpcsc-mock

%build
pushd web-eid-app
%cmake
%cmake_build

%install
pushd web-eid-app
%cmake_install

install -m 644 -Dt %{buildroot}/%{_sysconfdir}/chromium/native-messaging-hosts %{buildroot}/%{_datadir}/web-eid/eu.webeid.json
install -m 644 -Dt %{buildroot}/%{_sysconfdir}/opt/chrome/native-messaging-hosts %{buildroot}/%{_datadir}/web-eid/eu.webeid.json

rm -f %{buildroot}/%{_datadir}/web-eid/eu.webeid.json

%check
pushd web-eid-app
export QT_QPA_PLATFORM='offscreen' # needed for running headless tests
%ctest

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_sysconfdir}/chromium/native-messaging-hosts/
%{_sysconfdir}/opt/chrome/native-messaging-hosts/
%{_libdir}/mozilla/native-messaging-hosts/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/google-chrome/extensions/
%{_datadir}/mozilla/extensions/
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-7
- add desktop-file-utils to build requires (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-6
- fix desktop file validation path (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-5
- move desktop file validation to check (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-4
- fix post install script to use correct desktop file
  (arun.neelicattu@gmail.com)
- use upstream libpcsc-mock patch (arun.neelicattu@gmail.com)
- fix spec file formatting (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-3
- workaround patch file issue for tito (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-2
- fix readme typo (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-1
- new package built with tito

