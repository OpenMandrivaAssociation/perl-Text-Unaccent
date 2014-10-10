%define upstream_name    Text-Unaccent
%define upstream_version 1.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.80.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 556178
- rebuild for perl 5.12

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 408090
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.08-12mdv2009.0
+ Revision: 258622
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.08-11mdv2009.0
+ Revision: 246641
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.08-9mdv2008.1
+ Revision: 152331
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Nov 25 2007 Olivier Thauvin <nanardon@mandriva.org> 1.08-8mdv2008.1
+ Revision: 111836
- fix int/size_t usage, making the module to work on 64bits arch

* Sun Sep 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-5mdv2008.0
+ Revision: 88620
- exclude x86_64, test don't pass (see #http://rt.cpan.org//Ticket/Display.html?id=29390)
- rebuild


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:23:54 (54159)
- rebuild

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:21:24 (54156)
Import perl-Text-Unaccent

* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.08-3mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Mon Oct 10 2005 Nicolas L�cureuil <neoclust@mandriva.org> 1.08-2mdk
- Fix BuildRequires

* Mon Sep 05 2005 Olivier Thauvin <nanardon@mandriva.org> 1.08-1mdk
- First mandriva package (require by bins)

