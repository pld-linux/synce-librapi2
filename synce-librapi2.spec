# NOTE: for versions >= 0.16 see synce-core.spec
# TODO:
#	rm libstdc++-devel dependency - required only for tests programs
#
# Conditional build:
%bcond_without	dbus	# build without dbus support
%bcond_without	python	# build without python bindings
%bcond_with		hal 	# build without HAL support
%bcond_without	udev	# build without UDEV support
%bcond_without  odccm   # build without odccm support

%if %{without dbus}
%undefine	with_odccm
%undefine	with_hal
%undefine	with_udev
%endif

Summary:	SynCE RAPI library
Summary(pl.UTF-8):	Biblioteka SynCE RAPI
Name:		synce-librapi2
Version:	0.15.2
Release:	4
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/synce/librapi2-%{version}.tar.gz
# Source0-md5:	0a15bc22ee02794ca4714799611b4746
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.60}
BuildRequires:	gettext-tools
%{?with_hal:BuildRequires:	hal-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.559
%{?with_udev:BuildRequires:	udev-devel}
%if %{with python}
BuildRequires:	python-Pyrex
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# maybe temporaryliy, see https://bugs.launchpad.net/pld-linux/+bug/800148
BuildRequires:	python-modules
%endif
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-libsynce-devel >= 0.15
%requires_ge_to synce-libsynce synce-libsynce-devel
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

%package -n python-pyrapi2
Summary:	Python bindinding for RAPI library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki RAPI
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-pyrapi2
Python bindinding for RAPI library.

%description -n python-pyrapi2 -l pl.UTF-8
Wiązanie Pythona do biblioteki RAPI.

%prep
%setup -q -n librapi2-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_hal:--disable-hal-support}%{?with_hal:--enable-hal-support} \
	%{!?with_odccm:--disable-odccm-support}%{?with_odccm:--enable-odccm-support} \
	%{!?with_udev:--disable-udev-support}%{?with_udev:--enable-udev-support} \
	%{!?with_python:--disable-python-bindings}%{?with_python:--enable-python-bindings}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/pyrapi2.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README* TODO
%attr(755,root,root) %{_bindir}/pcp
%attr(755,root,root) %{_bindir}/pkillall
%attr(755,root,root) %{_bindir}/pls
%attr(755,root,root) %{_bindir}/pmkdir
%attr(755,root,root) %{_bindir}/pmv
%attr(755,root,root) %{_bindir}/prm
%attr(755,root,root) %{_bindir}/prmdir
%attr(755,root,root) %{_bindir}/prun
%attr(755,root,root) %{_bindir}/psettime
%attr(755,root,root) %{_bindir}/pshortcut
%attr(755,root,root) %{_bindir}/pstatus
%attr(755,root,root) %{_bindir}/rapiconfig
%attr(755,root,root) %{_bindir}/synce-database
%attr(755,root,root) %{_bindir}/synce-install-cab
%attr(755,root,root) %{_bindir}/synce-list-programs
%attr(755,root,root) %{_bindir}/synce-registry
%attr(755,root,root) %{_bindir}/synce-remove-program
%attr(755,root,root) %{_libdir}/librapi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librapi.so.2
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librapi.so
%{_libdir}/librapi.la
%{_includedir}/irapistream.h
%{_includedir}/rapi.h
%{_includedir}/rapi2.h
%{_includedir}/rapitypes.h
%{_includedir}/rapitypes2.h
%{_pkgconfigdir}/librapi2.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/librapi.a

%if %{with python}
%files -n python-pyrapi2
%defattr(644,root,root,755)
%{py_sitedir}/pyrapi2.so
%endif
