#
# Conditional build
%bcond_with	tests	# perform "make test" (requires reader)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Perl extension for TLP and RFTLP SmartCard reader
Summary(pl):	Rozszerzenie Perla do czytników kart procesorowych TLP i RFTLP
Name:		perl-cardreader
Version:	1.0.0
Release:	1
License:	BSD-like + restricted vendor's name usage (see copyright file)
Group:		Libraries
Source0:	http://www.gemplus.com/techno/tlp_drivers/download/libtlp-perl_%{version}.tar.gz
# Source0-md5:	12caa3e41d2e5635d3274549600cd8da
URL:		http://www.gemplus.com/techno/tlp_drivers/
BuildRequires:	libtlp-devel
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension for TLP and RFTLP SmartCard reader.

%description -l pl
Rozszerzenie Perla do czytników kart procesorowych TLP i RFTLP.

%prep
# use -c, the name "perl" may be too common
%setup -q -c

%build
cd perl
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags} -I."

%{?with_tests:%{__make} test}

%install
cd perl
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc perl/{Changes,README.unix,debian/copyright}
%{perl_vendorarch}/cardreader.pm
%dir %{perl_vendorarch}/auto/cardreader
%{perl_vendorarch}/auto/cardreader/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/cardreader/*.so
%{_mandir}/man3/*
