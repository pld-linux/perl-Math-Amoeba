%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Amoeba
Summary:	Math-Amoeba perl module
Summary(pl):	Modu³ perla Math-Amoeba
Name:		perl-Math-Amoeba
Version:	0.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Amoeba is an implimenation of the Downhill Simpex Method in
Multidimensions (Nelder and Mead) for finding the (local) minimum of a
function.

%description -l pl
Modu³ perla Math-Amoeba.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Math/Amoeba.pm
%{_mandir}/man3/*
