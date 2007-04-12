%define name gnome-nettool
%define version 2.18.0
%define release %mkrel 1

Summary: GNOME interface for networking tools
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: scrollkeeper
BuildRequires:  gnome-doc-utils libxslt-proc
BuildRequires: ImageMagick
BuildRequires:  perl-XML-Parser
BuildRequires:  desktop-file-utils
Conflicts: gnome-network <= 1.99.5
Provides: gnome-netinfo
Obsoletes: gnome-netinfo
#gw for dig
Requires: bind-utils
#gw for ping, ping6
Requires: iputils
Requires: whois
Requires: traceroute
Requires(post)  : scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3

%description
This is a GNOME gui for the basic networking tools like ping, whois,
traceroute and dig.

%prep
%setup -q

%build
%configure2_5x --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??.omf;do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name.lang
done

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF >> $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): title="Network information" longtitle="GNOME Network Information" command="%{_bindir}/%name" icon="%name.png" needs="x11" section="Internet/Other" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Internet-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


mkdir -p %buildroot{%_iconsdir,%_liconsdir,%_miconsdir}
ln -s %_datadir/icons/hicolor/48x48/apps/gnome-nettool.png %buildroot%_liconsdir/%name.png
convert -scale 32x32 %buildroot%_datadir/icons/hicolor/48x48/apps/gnome-nettool.png %buildroot%_iconsdir/%name.png
convert -scale 16x16 %buildroot%_datadir/icons/hicolor/48x48/apps/gnome-nettool.png %buildroot%_miconsdir/%name.png


%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%update_scrollkeeper
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_scrollkeeper
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,root,root)
%doc README TODO NEWS AUTHORS ChangeLog
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/%name
%{_menudir}/*
%_datadir/icons/hicolor/48x48/apps/gnome-nettool.png
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%dir %_datadir/omf/*
%_datadir/omf/*/*-C.omf

