%define upstream_name    Dist-Zilla-Plugin-CheckChangeLog
Name:		perl-%{upstream_name}
Version:	0.05
Release:	2

Summary:	Dist::Zilla with Changes check
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/fayland/dist-zilla-plugin-checkchangelog
Source0:	https://cpan.metacpan.org/authors/id/F/FA/FAYLAND/Dist-Zilla-Plugin-CheckChangeLog-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildArch:	noarch

%description
The code is mostly a copy-paste of the ShipIt::Step::CheckChangeLog manpage.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

