#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Glob
Summary:	Text::Glob perl module - match globbing patterns against text
Summary(pl):	Modu³ perla Text::Glob - dopasowywanie tekstu do wzorców
Name:		perl-Text-Glob
Version:	0.05
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6daaba2a73f3a4943f0058e4c158e318
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Glob implements glob(3) style matching that can be used to match
against text, rather than fetching names from a filesystem. If you
want to do full file globbing use the File::Glob module instead.

%description -l pl
Text::Glob jest implementacj± dopasowywania w stylu glob(3), które
mo¿e byæ u¿ywane do dopasowywania tekstu, a nie nazw plików. Je¶li
potrzeba pe³nej implementacji glob dla plików, nale¿y u¿yæ modu³u
File::Glob zamiast tego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/*.pm
%{_mandir}/man3/*
