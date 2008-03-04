%define	name	libmodplug
%define	version	0.8.4
%define epoch 1 
%define major 0
%define mdkversion		%(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandriva-release)
%if %mdkversion > 900
%define libname %mklibname modplug %major
%else
%define libname libmodplug%major
%endif
Name:		%{name}
Summary:	Modplug music player
Version:	%{version}
Release:	%mkrel 3
License:	Public Domain
Group:		Sound
URL:		http://modplug-xmms.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/modplug-xmms/%name-%{version}.tar.bz2
Epoch: %epoch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%package -n %{libname}-devel
Group:		Development/C++
Summary:	Header files for compiling against Modplug library
Provides:	%name-devel = %epoch:%version-%release
Requires:	%{libname} = %epoch:%version-%release

%description -n %{libname}-devel
This is the development package of libmodplug. Install it if you want to 
compile programs using this library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/libmodplug.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS TODO ChangeLog
%{_libdir}/libmodplug.la
%{_libdir}/libmodplug.so
%{_includedir}/libmodplug/
%_libdir/pkgconfig/*.pc


