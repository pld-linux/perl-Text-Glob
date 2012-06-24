#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Glob
Summary:	Text::Glob perl module - match globbing patterns against text
Summary(pl):	Modu� perla Text::Glob - dopasowywanie tekstu do wzorc�w
Name:		perl-Text-Glob
Version:	0.06
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	800d5a40b2f0c7514c58d736d21f616c
BuildRequires:	perl-devel >= 5.6
%if %{with tests}
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
Text::Glob jest implementacj� dopasowywania w stylu glob(3), kt�re
mo�e by� u�ywane do dopasowywania tekstu, a nie nazw plik�w. Je�li
potrzeba pe�nej implementacji glob dla plik�w, nale�y u�y� modu�u
File::Glob zamiast tego.

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
%doc Changes
%{perl_vendorlib}/Text/*.pm
%{_mandir}/man3/*
