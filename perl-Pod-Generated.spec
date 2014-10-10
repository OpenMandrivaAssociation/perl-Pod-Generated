%define upstream_name    Pod-Generated
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Template plugin to help generate POD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::ISA)
BuildRequires:	perl(Devel::Peek)
BuildRequires:	perl(Devel::Symdump)
BuildRequires:	perl(Module::Install::Template)
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Conjunct)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(YAML)
BuildArch:	noarch

%description
This module provides support for generating POD documentation for your
modules during 'make' time. It does not itself generate the documentation -
the combination of the Module::Install::Template manpage and the
Template::Plugin::PodGenerated manpage does that.

Also see the Pod::Generated::Attributes manpage.

Modules that generate methods - such as the Class::Accessor manpage - might
want to use this module. the Class::Accessor::Complex manpage, the
Class::Accessor::Constructor manpage and the Class::Accessor::FactoryTyped
manpage do support generated documentation, or will do so shortly.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# outdated and broken, use system perl-YAML instead
rm -f inc/YAML.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 654285
- rebuild for updated spec-helper

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 474652
- update to 0.05

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 444072
- import perl-Pod-Generated


* Thu Sep 17 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
