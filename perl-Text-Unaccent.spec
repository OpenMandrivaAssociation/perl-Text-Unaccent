%define upstream_name    Text-Unaccent
%define upstream_version 1.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Remove accents from a string
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text//%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:      Text-Unaccent-size_t.patch

BuildRequires:  perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
A module that remove accents from a string. unac_string converts the input
string from the specified charset to UTF-16 and call unac_string_utf16 to
return the unaccented equivalent. The conversion from and to UTF-16 is done
with iconv(1).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0 -b .size_t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"

%check
make test

%install
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/*/*
%{perl_vendorarch}/*
