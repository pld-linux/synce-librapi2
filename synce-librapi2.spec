Summary:	SynCE RAPI library
Summary(pl):	Biblioteka SynCE RAPI
Name:		synce-librapi2
Version:	0.9.0
Release:	1
License:	MIT
Group:		Libraries
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	f585e8d56c83d4e811197d671fd4c201
URL:		http://synce.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	synce-libsynce-devel >= 0.9.0
Requires:	synce-libsynce >= 0.9.0
ExcludeArch:	alpha amd64 ppc64 s390x sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RAPI library is an open source implementation that works like
RAPI.DLL, available on Microsoft operating systems. The library makes
it possible to make remote calls to a computer running Pocket PC.

%description -l pl
Biblioteka RAPI to otwarta implementacja dzia³aj±ca tak jak RAPI.DLL
dostêpna w systemach operacyjnych Microsoftu. Biblioteka umo¿liwia
wykonywanie zdalnych odwo³añ do komputera Pocket PC.

%package devel
Summary:	Header files for RAPI library
Summary(pl):	Pliki nag³ówkowe biblioteki RAPI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	synce-libsynce-devel >= 0.9.0

%description devel
Header files for RAPI library.

%description devel -l pl
Pliki nag³ówkowe biblioteki RAPI.

%package static
Summary:	Static RAPI library
Summary(pl):	Statyczna biblioteka RAPI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static RAPI library.

%description static -l pl
Statyczna biblioteka RAPI.

%prep
%setup -q

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
%doc BUGS LICENSE README* TODO src/README.rapi
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/librapi.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librapi.so
%{_libdir}/librapi.la
%{_includedir}/rapi.h
%{_aclocaldir}/librapi2.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/librapi.a
