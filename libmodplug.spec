%define major 1
%define libname %mklibname modplug %{major}
%define develname %mklibname -d modplug

Summary:	Modplug music player
Name:		libmodplug
Version:	0.8.8.4
Release:	3
Epoch:		1
License:	Public Domain
Group:		Sound
URL:		http://modplug-xmms.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/modplug-xmms/%{name}-%{version}.tar.gz

%description
Olivier Lapicque, author of Modplug, which is arguably the best quality
MOD-playing software available, has placed his sound rendering code in the
public domain.  This library and plugin is based on that code.

It can play 22 different mod formats, including:
MOD, S3M, XM, IT, 669, AMF (both of them), AMS, DBM, DMF, DSM, FAR,
MDL, MED, MTM, OKT, PTM, STM, ULT, UMX, MT2, PSM

%package -n %{libname}
Group:		System/Libraries
Summary:	Modplug shared library

%description -n %{libname}
This is the shared library part of the Modplug music player.

%package -n %{develname}
Group:		Development/C++
Summary:	Header files for compiling against Modplug library
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
This is the development package of libmodplug. Install it if you want to 
compile programs using this library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc README COPYING
%{_libdir}/libmodplug.so.%{major}*

%files -n %{develname}
%doc AUTHORS TODO ChangeLog
%{_libdir}/libmodplug.so
%{_includedir}/libmodplug/
%{_libdir}/pkgconfig/*.pc



%changelog
* Tue Jan 03 2012 Götz Waschk <waschk@mandriva.org> 1:0.8.8.4-2mdv2012.0
+ Revision: 748812
- remove libtool archive

* Thu Aug 18 2011 Götz Waschk <waschk@mandriva.org> 1:0.8.8.4-1
+ Revision: 695120
- update to new version 0.8.8.4

* Wed May 11 2011 Götz Waschk <waschk@mandriva.org> 1:0.8.8.3-1
+ Revision: 673501
- update to new version 0.8.8.3

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.8.8.2-2
+ Revision: 662382
- mass rebuild

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 1:0.8.8.2-1
+ Revision: 650154
- new version

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 1:0.8.8.1-1mdv2011.0
+ Revision: 550265
- new version
- new major

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.8.7-2mdv2010.1
+ Revision: 520885
- rebuilt for 2010.1

* Mon Apr 27 2009 Götz Waschk <waschk@mandriva.org> 1:0.8.7-1mdv2010.0
+ Revision: 369048
- update to new version 0.8.7

* Mon Apr 20 2009 Götz Waschk <waschk@mandriva.org> 1:0.8.6-1mdv2009.1
+ Revision: 368354
+ rebuild (emptylog)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1:0.8.4-4mdv2009.0
+ Revision: 222932
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.8.4-3mdv2008.1
+ Revision: 178966
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 16 2007 Götz Waschk <waschk@mandriva.org> 1:0.8.4-1mdv2008.0
+ Revision: 27216
- new version
- drop merged patch


* Sat Dec 30 2006 Götz Waschk <waschk@mandriva.org> 0.8-1mdv2007.0
+ Revision: 102883
- new version
- Import libmodplug

* Sat Dec 30 2006 G�tz Waschk <waschk@mandriva.org> 0.7-8mdv2007.1
- security fix for CVE-2006-4192

* Wed Dec 28 2005 Götz Waschk <waschk@mandriva.org> 0.7-7mdk
- Rebuild
- use mkrel

* Mon Dec 27 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.7-6mdk
- from Michael Collard some x86_64 fixes

* Sat Jun 05 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.7-5mdk
- source URL
- new g++

* Tue Mar 02 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.7-4mdk
- support mdk 9.0

* Thu Feb 26 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.7-3mdk
- fix deps of the devel package

