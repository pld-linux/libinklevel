Summary:	Library for checking ink level of a printer
Summary(pl):	Biblioteka do sprawdzania poziomu atramentu drukarki
Name:		libinklevel
Version:	0.6
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://home.arcor.de/markusheinz/%{name}-%{version}.tar.gz
Patch0:		%{name}-build_fixes.patch
URL:		http://home.arcor.de/markusheinz/libinklevel.html
BuildRequires:	libieee1284-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libinklevel is a library for checking the ink level of printer. It
supports printers attached via parallel port or USB.

%description -l pl
Libinklevel jest bibliotek± wykorzystywan± do sprawdzania poziomu
atramentu w drukarce. Wspierane s± drukarki pod³±czone za
po¶rednictwem portu równoleg³ego oraz USB.

%package devel
Summary:	Header files for libinklevel
Summary(pl):	Pliki nag³ówkowe dla libinklevel
Group:		Development
Requires:	%{name} = %{version}

%description devel
Header files for libinklevel.

%description devel -l pl
Pliki nag³ówkowe dla libinklevel.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h
