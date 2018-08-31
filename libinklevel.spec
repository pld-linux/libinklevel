#
# Conditional build:
%bcond_without	parport	# parallel port (IEEE 1284) support

Summary:	Library for checking ink level of a printer
Summary(pl.UTF-8):	Biblioteka do sprawdzania poziomu atramentu drukarki
Name:		libinklevel
Version:	0.9.3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libinklevel/%{name}-%{version}.tar.gz
# Source0-md5:	572eda08cc561414673fd798b6c7bc2a
Patch0:		%{name}-parport.patch
URL:		http://libinklevel.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_parport:BuildRequires:	libieee1284-devel}
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 1.0.17
BuildRequires:	pkgconfig >= 1:0.26
Requires:	libusb >= 1.0.17
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
Summary:	Header file for libinklevel
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libinklevel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_parport:Requires:	libieee1284-devel}
Requires:	libusb-devel >= 1.0

%description devel
Header file for libinklevel.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libinklevel.

%package static
Summary:	Static libinklevel library
Summary(pl.UTF-8):	Statyczna biblioteka libinklevel
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libinklevel library.

%description static -l pl.UTF-8
Statyczna biblioteka libinklevel.

%prep
%setup -q
%if %{with parport}
%patch0 -p1
%endif

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libinklevel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinklevel.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinklevel.so
%{_libdir}/libinklevel.la
%{_includedir}/inklevel.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libinklevel.a
