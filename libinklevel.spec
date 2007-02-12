Summary:	Library for checking ink level of a printer
Summary(pl.UTF-8):   Biblioteka do sprawdzania poziomu atramentu drukarki
Name:		libinklevel
Version:	0.6.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libinklevel/%{name}-%{version}.tar.gz
# Source0-md5:	2bc2dd1e0b08de28d110355adcee8b22
Patch0:		%{name}-build_fixes.patch
URL:		http://libinklevel.sourceforge.net/
BuildRequires:	libieee1284-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libinklevel is a library for checking the ink level of printer. It
supports printers attached via parallel port or USB.
Supported printers list can be found here:
http://libinklevel.sourceforge.net/index.html#supported

%description -l pl.UTF-8
Libinklevel jest biblioteką wykorzystywaną do sprawdzania poziomu
atramentu w drukarce. Wspierane są drukarki podłączone za
pośrednictwem portu równoległego oraz USB.
Listę aktualnie obsługiwanych drukarek można znaleźć tutaj:
http://libinklevel.sourceforge.net/index.html#supported

%package devel
Summary:	Header files for libinklevel
Summary(pl.UTF-8):   Pliki nagłówkowe dla libinklevel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libinklevel.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libinklevel.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

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
