%define upstream_name    Pod-Generated
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Template plugin to help generate POD
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::ISA)
BuildRequires: perl(Devel::Peek)
BuildRequires: perl(Devel::Symdump)
BuildRequires: perl(Module::Install::Template)
BuildRequires: perl(Template)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Conjunct)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(YAML)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


