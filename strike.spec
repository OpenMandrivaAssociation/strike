#define snapshot 20220107

Name:		strike
Version:	1.0.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Strike is a simple minimal IDE for the Linux phones. Code, build, and run from the phone.
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/strike/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(MauiKit)
BuildRequires:  cmake(MauiKitFileBrowsing)
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)

%description
Strike is a simple minimal IDE for the Linux phones. Code, build, and run from the phone.

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
