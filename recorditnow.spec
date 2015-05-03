%define	libname		%mklibname recorditnow
%define	joschylib	%mklibname joschycore
%define	joschydevel	%mklibname -d joschycore

Name:		recorditnow
Version:	0.8.1
# use 69.x release for 0.8.1 to allow updates for MIB users
Release:	%mkrel 69.5
Summary:	Desktop session recorder for KDE 4
License:	GPLv2+
Group:		Video
URL:		http://recorditnow.sourceforge.net/
Source0:	http://sourceforge.net/projects/recorditnow/files/%{name}-%{version}.tar.bz2
Patch0:		recorditnow-0.8.1-ru.patch
Patch1:		recorditnow-0.8.1-linking.patch
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6
BuildRequires:	gettext
BuildRequires:	qt4-devel
BuildRequires:	kdelibs4-devel >= 4.4.0
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11)
BuildRequires:	ffmpeg-devel >= 2.5.4
BuildRequires:	ffmpeg >= 2.5.4
BuildRequires:	mencoder
BuildRequires:	recordmydesktop >= 0.3.8.1

Requires:	kdelibs4-core >= 4.4.0
Requires:	ffmpeg
Requires:	mencoder
Requires:	recordmydesktop >= 0.3.8.1

%description
RecordItNow is a plug-in based desktop recorder for KDE SC 4.
Features:
    Record your desktop;
    Make screen-shots;
    Automatically encode your videos in a desired format;
    Zoom;
    Show mouse activity;
    Keyboard monitor;
    Time-line;
    Upload your videos to YouTube or blip.tv.

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING DEPENDENCIES
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/libexec/%{name}_helper
%{_kde_libdir}/kde4/*.so
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}/*
%{_kde_datadir}/config.kcfg/%{name}*.kcfg
%{_kde_iconsdir}/hicolor/*/apps/*.png
%{_kde_services}/%{name}_*.desktop
%{_kde_servicetypes}/%{name}_*.desktop
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/dbus-1/system-services/*.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/*.conf

#------------------------------------------------------------

%package -n	%{libname}
Summary:	Library package for recorditnow
Group:		System/Libraries
Requires:	%{name} = %{version}

%description -n %{libname}
This package contains the dynamic libraries needed for recorditnow.

%files -n %{libname}
%defattr(-,root,root)
%{_kde_libdir}/librecordit*.so

#------------------------------------------------------------

%package -n	%{joschylib}
Summary:	Support library for recorditnow
Group:		System/Libraries
Requires:	%{name} = %{version}

%description -n %{joschylib}
This package contains the dynamic libraries needed for recorditnow.

%files -n %{joschylib}
%defattr(-,root,root)
%{_kde_libdir}/libjoschycore.so
%{_kde_libdir}/joschy/*

#------------------------------------------------------------

%package -n	%{joschydevel}

Summary:	Development files for the joschycore library
Group:		Development/C++
Provides:	joschycore-devel = %{version}
Provides:	%{joschydevel} = %{version}
Requires:	%{joschylib} = %{version}

%description -n %{joschydevel}
This package contains the header files needed when building applications
based on the joschycore library.

%files -n %{joschydevel}
%defattr(-,root,root)
%{_kde_includedir}/joschycore/*.h

#------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .ru
%patch1 -p1 -b .linking

%build
%cmake_kde4 ..	-DCMAKE_BUILD_TYPE=release \
		-DLINGUAS="de;hu;pt_BR;cs;fr;ru;tr"
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%post
kbuildsycoca4

%postun
kbuildsycoca4





