%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Amoeba
Summary:	Math::Amoeba perl module
Summary(pl):	Modu� perla Math::Amoeba
Name:		perl-Math-Amoeba
Version:	0.01
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Amoeba is an implimenation of the Downhill Simpex Method in
Multidimensions (Nelder and Mead) for finding the (local) minimum of a
function.

%description -l pl
Modu� perla Math::Amoeba jest implementacj� metody "Downhill Simplex"
w wielu wymiarach (Neldera i Meada) do znajdowania (lokalnego) minimum
funkcji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Math/Amoeba.pm
%{_mandir}/man3/*
