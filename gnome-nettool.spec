%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Network information tool for GNOME
Name:		gnome-nettool
Version:	42.0
Release:	1
Url:		http://projects.gnome.org/gnome-network/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
License:	GPLv2+ and GFDL
Group:		Graphical desktop/GNOME
BuildRequires:	meson
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	rarian
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90.4
BuildRequires:	pkgconfig(gio-2.0) >= 2.25.10
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	itstool
Requires:	whois
Requires:	traceroute

%description
GNOME Nettool is a frontend to various networking commandline
tools, like ping, netstat, ifconfig, whois, traceroute, finger.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_ install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*.xpm
%{_datadir}/%{name}/pixmaps/*.png
%{_datadir}/%{name}/ui/%{name}.ui
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-nettool.gschema.xml

