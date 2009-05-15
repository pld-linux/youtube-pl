Summary:	youtube-pl plays Youtube videos from the commandline
Summary(hu.UTF-8):	youtube-pl Youtube videókat játszik a parancssorból
Name:		youtube-pl
Version:	20090321
Release:	0.1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://ronja.twibright.com/utils/%{name}
# Source0-md5:	175c386ca7418d68f8164508f3f84d56
URL:		http://ronja.twibright.com/youtube-pl.php
Requires:	mplayer >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
youtube-pl plays Youtube videos from the commandline. No download
takes place, the video is streamed. Limited seeking and all operations
mplayer allows with them - speed up down, brightness contrast
adjustment, A/V delay adjustment, fast forward.

%description -l hu.UTF-8
youtube-pl Youtube videókat játszik le parancssorból. Nincs letöltött
fájl, ami foglalná a helyet, ugyanis a videó stream-elt. Korlátozott
tekerés és minden lehetséges, amelyet az mplayer megenged velük:
sebeség növelés/csökkentés, fényesség és kontraszt állítás, A/V
késleltetés állítása, gyors előretekerés.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
# /usr/bin/env python  ->  /usr/bin/python
sed -i "1 s@.*@#!%{_bindir}/python@" $RPM_BUILD_ROOT%{_bindir}/%{name}
# we don't want default mplayer fullscreen
sed -i "s@mplayer \(.*\)-fs\(.*\)@mplayer \1 \2@" $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
