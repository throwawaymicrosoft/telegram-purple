Name:       purple-telegram
Version:    1.3.1
Release:    1%{?dist}
Summary:    Adds support for Libpurple based messengers
Group:      Applications/Internet
License:    GPLv2+
URL:        https://github.com/majn/telegram-purple
Source0:    https://codeload.github.com/majn/telegram-purple/tar.gz/v%{version}.tar.gz

BuildRequires:  gettext, libgcrypt-devel >= 1.6, pkgconfig(zlib), pkgconfig(purple), pkgconfig(libwebp)
BuildRequires:  pkgconfig(appstream-glib)

%description
Adds support for Telegram to Pidgin, Adium, Finch
and other Libpurple based messengers.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
%make_install
chmod 755 %{buildroot}/%{_libdir}/purple-2/telegram-purple.so
%find_lang telegram-purple

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/telegram-purple.metainfo.xml

%files -f telegram-purple.lang
%doc README* CHANGELOG*
%{_libdir}/purple-2/telegram-purple.so
%config %{_sysconfdir}/telegram-purple/*
%{_datadir}/appdata/telegram-purple.metainfo.xml
%{_datadir}/pixmaps/pidgin/protocols/16/telegram.png
%{_datadir}/pixmaps/pidgin/protocols/22/telegram.png
%{_datadir}/pixmaps/pidgin/protocols/48/telegram.png
%{_datadir}/appdata/telegram-purple.metainfo.xml

%changelog
* Sun Apr 9 2017 mjentsch 1.3.1-1
- Build for 1.3.1

* Thu Dec 10 2015 tuxmaster 1.3.0-1
- Build for 1.3.0

* Sat Jan 23 mjentsch 1.2.5-1
- build for 1.2.5

* Thu Dec 10 2015 tuxmaster 1.2.4-2
- Fix build for appdata. 

* Thu Dec 10 2015 mjentsch 1.2.4-1
- build for 1.2.4

* Thu Dec 10 2015 tuxmaster 1.2.4-2
- Fix build for appdata.

* Wed Nov 18 2015 tuxmaster 1.2.2-3
- Add required version for libgcrypt.

* Wed Oct 14 2015 tuxmaster 1.2.2-2
- Use the better pkconfig for build requires.
- Add translations.
- Switch to libgcrypt from openssl.

* Wed Oct 07 2015 mjentsch 1.2.2-1
- update version to 1.2.2
