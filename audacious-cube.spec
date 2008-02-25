%define name audacious-cube
%define version 1.2.2
%define release %mkrel 1

Summary: Gamecube audio plugin for Audacious
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Patch: audacious-cube-1.2.1-autoconf.patch
License: GPL
Group: Sound
Url: http://voidpointer.org/audacious-cube
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libaudacious-devel
Requires: audacious

%description
Audacious Cube is a port of the Winamp plugin in_cube. This plugin allows
you to play Gamecube streamed audio files. Supported types include
DSP, GCM, HPS, IDSP, SPT, SPD, MSS, MPDSP, ISH, YMF, ADX, ADX, RSD,
RSP, AST, and AFC.

%prep
%setup -q
%patch -p1
autoconf


%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/audacious/Input/libcube.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS README NEWS
%_libdir/audacious/Input/libcube.so
