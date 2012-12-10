%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Network information tool for GNOME
Name:		gnome-nettool
Version:	3.2.0
Release:	%mkrel 1
URL:		http://projects.gnome.org/gnome-network/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
License:	GPLv2+ and GFDL
Group:		Graphical desktop/GNOME
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90.4
BuildRequires:  pkgconfig(gio-2.0) >= 2.25.10
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(libgtop-2.0)

Requires:	whois
Requires:	traceroute

%description
GNOME Nettool is a frontend to various networking commandline
tools, like ping, netstat, ifconfig, whois, traceroute, finger.

%prep
%setup -q

%build
%configure2_5x \
	--disable-scrollkeeper \
	--disable-schemas-compile \
	--disable-static
%make

%install
%makeinstall_std

desktop-file-install \
	--vendor "" \
	--delete-original \
	--dir %{buildroot}%{_datadir}/applications \
	--remove-category Network \
	--add-category GNOME \
	--add-category System \
	--add-category Utility \
		%{buildroot}%{_datadir}/applications/gnome-nettool.desktop

%find_lang %{name} --with-gnome

#for omf in %{buildroot}%{_datadir}/omf/%{name}/%{name}-??*.omf;do 
#echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%{buildroot}!!)" >> %{name}.lang
#done

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/pixmaps/*.xpm
%{_datadir}/%{name}/pixmaps/*.png
%{_datadir}/%{name}/ui/%{name}.ui
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-nettool.gschema.xml


%changelog
* Wed Apr 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.2.0-1mdv2012.0
+ Revision: 791753
- version update 3.2.0

* Thu Sep 29 2011 Götz Waschk <waschk@mandriva.org> 2.32.0-2
+ Revision: 701909
- rebuild

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581639
- update to new version 2.32.0

* Thu Aug 05 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 566150
- new version
- update build deps

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528966
- update to new version 2.30.0

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447375
- update to new version 2.28.0

* Thu Jul 16 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 396538
- update to new version 2.27.4

* Wed May 20 2009 Götz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 377929
- update to new version 2.26.2

* Tue Mar 31 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 363038
- new version
- fix omf file list

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356492
- new version
- update file list

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315824
- fix build deps
- update to new version 2.25.3

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 287329
- new version
- update license
- update build deps

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-3mdv2009.0
+ Revision: 246418
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183718
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89471
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 63296
- new version
- drop legacy menu
- update file list

