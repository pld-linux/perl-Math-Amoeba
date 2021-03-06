#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Amoeba
Summary:	Math::Amoeba - multidimensional function minimalization
Summary(pl.UTF-8):	Math::Amoeba - minimalizacja funkcji w wielu wymiarach
Name:		perl-Math-Amoeba
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df05eeaef4794cc56e8ed71fb8b5c483
URL:		http://search.cpan.org/dist/Math-Amoeba/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Amoeba is an implimenation of the Downhill Simpex Method in
Multidimensions (Nelder and Mead) for finding the (local) minimum of a
function.

%description -l pl.UTF-8
Moduł perla Math::Amoeba jest implementacją metody "Downhill Simplex"
w wielu wymiarach (Neldera i Meada) do znajdowania (lokalnego) minimum
funkcji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Amoeba.pm
%{_mandir}/man3/*
