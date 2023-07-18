#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-IO-Prompter
Version  : 0.005001
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/IO-Prompter-0.005001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/IO-Prompter-0.005001.tar.gz
Summary  : 'Prompt for input, read it, clean it, return it.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-IO-Prompter-perl = %{version}-%{release}
Requires: perl(Contextual::Return)
Requires: perl(Scalar::Util)
Requires: perl(match::smart)
BuildRequires : buildreq-cpan
BuildRequires : perl(Contextual::Return)
BuildRequires : perl(Want)
BuildRequires : perl(match::smart)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
IO::Prompter version 0.005001
Prompt for, read, vet, chomp, and encapsulate input.
Like so:

%package dev
Summary: dev components for the perl-IO-Prompter package.
Group: Development
Provides: perl-IO-Prompter-devel = %{version}-%{release}
Requires: perl-IO-Prompter = %{version}-%{release}

%description dev
dev components for the perl-IO-Prompter package.


%package perl
Summary: perl components for the perl-IO-Prompter package.
Group: Default
Requires: perl-IO-Prompter = %{version}-%{release}

%description perl
perl components for the perl-IO-Prompter package.


%prep
%setup -q -n IO-Prompter-0.005001
cd %{_builddir}/IO-Prompter-0.005001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Prompter.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
