%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Math-Amoeba perl module
Summary(pl):	Modu³ perla Math-Amoeba
Name:		perl-Math-Amoeba
Version:	0.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-Amoeba-%{version}.tar.gz
Patch:		perl-Math-Amoeba-man.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Math-Amoeba is an implimenation of the Downhill Simpex Method 
in Multidimensions (Nelder and Mead) for finding the (local) minimum 
of a function.

%description -l pl
Modu³ perla Math-Amoeba.

%prep
%setup -q -n Math-Amoeba-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Math/Amoeba
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Math/Amoeba.pm
%{perl_sitearch}/auto/Math/Amoeba

%{_mandir}/man3/*
