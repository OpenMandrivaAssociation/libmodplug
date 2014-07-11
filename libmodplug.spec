%define major	1
%define libname %mklibname modplug %{major}
%define devname %mklibname -d modplug

Summary:	Modplug music player
Name:		libmodplug
Epoch:		1
Version:	0.8.8.4
Release:	13
License:	Public Domain
Group:		Sound
Url:		http://modplug-xmms.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/modplug-xmms/%{name}-%{version}.tar.gz

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

%package -n %{devname}
Group:		Development/C++
Summary:	Header files for compiling against Modplug library
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
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
%{_libdir}/libmodplug.so.%{major}*

%files -n %{devname}
%doc AUTHORS TODO ChangeLog README COPYING
%{_libdir}/libmodplug.so
%{_includedir}/libmodplug/
%{_libdir}/pkgconfig/*.pc

