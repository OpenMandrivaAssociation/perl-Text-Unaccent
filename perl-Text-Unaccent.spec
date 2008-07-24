%define real_name Text-Unaccent
%define name perl-%{real_name}
%define version 1.08
%define release %mkrel 11

Summary:	Remove accents from a string
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text//%{real_name}-%{version}.tar.bz2
Patch0:      Text-Unaccent-size_t.patch
URL:		http://search.cpan.org/dist/%{real_name}/
BuildRequires:  perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
A module that remove accents from a string. unac_string converts the input
string from the specified charset to UTF-16 and call unac_string_utf16 to
return the unaccented equivalent. The conversion from and to UTF-16 is done
with iconv(1).

%prep
%setup -q -n %{real_name}-%{version}
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


