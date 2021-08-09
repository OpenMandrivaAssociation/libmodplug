%define major	1
%define libname %mklibname modplug %{major}
%define devname %mklibname -d modplug

%define date 20210809

Summary:	Modplug music player
Name:		libmodplug
Epoch:		1
Version:	0.8.9.1
Release:	%{?date:0.%{date}.}1
License:	Public Domain
Group:		Sound
Url:		http://modplug-xmms.sourceforge.net/
Source0:	https://github.com/Konstanty/libmodplug/archive/refs/heads/master.tar.gz

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
%autosetup -p1 -n %{name}-%{?date:master}%{!?date:%{version}}
# The cmake build files are too buggy to use for now
# no soname, no lib64, ...
%configure

%build
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libmodplug.so.%{major}*

%files -n %{devname}
%doc AUTHORS TODO ChangeLog README COPYING
%{_libdir}/libmodplug.so
%{_includedir}/libmodplug/
%{_libdir}/pkgconfig/*.pc

