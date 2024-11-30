#define snapshot 20220107

Name:		strike
Version:	2.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Strike is a simple minimal IDE for the Linux phones. Code, build, and run from the phone.
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/strike/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/maui-%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(MauiKitTextEditor4)
BuildRequires:  cmake(MauiKitTerminal4)
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)

%description
Strike is a simple minimal IDE for the Linux phones. Code, build, and run from the phone.

%prep
%autosetup -p1 -n maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang strike

%files -f strike.lang
%{_bindir}/strike
%{_datadir}/applications/org.kde.strike.desktop
%{_datadir}/metainfo/org.kde.strike.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/strike.svg
