# TODO
# - python bindings
Summary:	SynCE RAPI library
Summary(pl.UTF-8):	Biblioteka SynCE RAPI
Name:		synce-librapi2
Version:	0.10.0
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	321632a4319690f1bffc9d1a5f7e4f00
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	python-Pyrex
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-libsynce-devel >= %{version}
%requires_eq_to synce-libsynce synce-libsynce-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RAPI library is an open source implementation that works like
RAPI.DLL, available on Microsoft operating systems. The library makes
it possible to make remote calls to a computer running Pocket PC.

%description -l pl.UTF-8
Biblioteka RAPI to otwarta implementacja działająca tak jak RAPI.DLL
dostępna w systemach operacyjnych Microsoftu. Biblioteka umożliwia
wykonywanie zdalnych odwołań do komputera Pocket PC.

%package devel
Summary:	Header files for RAPI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RAPI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	synce-libsynce-devel

%description devel
Header files for RAPI library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RAPI.

%package static
Summary:	Static RAPI library
Summary(pl.UTF-8):	Statyczna biblioteka RAPI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static RAPI library.

%description static -l pl.UTF-8
Statyczna biblioteka RAPI.

%prep
%setup -q -n librapi2-%{version}

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
%doc README* TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/librapi.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librapi.so
%{_libdir}/librapi.la
%{_includedir}/rapi.h
%{_pkgconfigdir}/librapi2.pc
#%{py_sitedir}/pyrapi2.a
#%{py_sitedir}/pyrapi2.la
#%{py_sitedir}/pyrapi2.so

%files static
%defattr(644,root,root,755)
%{_libdir}/librapi.a
