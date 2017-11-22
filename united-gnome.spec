%global gitdate 20171122
%global commit0 bfb20eb828f489e863d3f2c7877c1a1e5fc737ee
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           united-gnome
Version:        2.2
Release:        3%{gver}%{dist}
Summary:        GTK2/3 + GNOME Shell theme based on a Unity 8 design concept.

License:        GPLv3
URL:            https://github.com/godlyranchdressing/United-GNOME
Source0: 	https://github.com/godlyranchdressing/United-GNOME/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
#BuildRequires:	sassc
Requires:	united-theme 
Requires:	united-dark-theme 
Requires:	united-darker-theme
Recommends:	united-light-gnome-shell-theme

%description
GTK2/3 + GNOME Shell pack theme based on a Unity 8 design concept.

%package -n united-theme
Summary:        United GTK+2/GTK3-3 and Shell themes
Requires: 	united-gtk2-theme united-gtk3-theme united-metacity-theme united-gnome-shell-theme

%description -n united-theme
United GTK+2/GTK3-3 and Shell themes

%package -n united-gtk2-theme
Summary:        United GTK+2 themes
Requires:       gtk-murrine-engine >= 0.98.1.1 gtk2-engines

%description -n united-gtk2-theme
Themes for GTK+2 as part of the United theme.


%package -n united-gtk3-theme
Summary:        United GTK+3 themes

%description -n united-gtk3-theme
Themes for GTK+3 as part of the United theme.


%package -n united-metacity-theme
Summary:        United Metacity themes
Requires:       metacity

%description -n united-metacity-theme
Themes for Metacity as part of the United theme.

%package -n united-gnome-shell-theme
Summary:        United Shell theme
Requires:       gnome-shell

%description -n united-gnome-shell-theme
United Shell theme

###

%package -n united-light-gnome-shell-theme
Summary:        United Light Shell theme
Requires:       gnome-shell

%description -n united-light-gnome-shell-theme
United Light Shell theme

###

%package -n united-dark-theme
Summary:        United Dark GTK+2/GTK3-3 and Shell themes
Requires: 	united-dark-gtk2-theme united-dark-gtk3-theme united-dark-metacity-theme united-dark-gnome-shell-theme

%description -n united-dark-theme
United Dark GTK+2/GTK3-3 and Shell themes

%package -n united-dark-gtk2-theme
Summary:        United Dark GTK+2 themes
Requires:       gtk-murrine-engine >= 0.98.1.1 gtk2-engines

%description -n united-dark-gtk2-theme
Themes for GTK+2 as part of the United Dark  theme.


%package -n united-dark-gtk3-theme
Summary:        United Dark GTK+3 themes

%description -n united-dark-gtk3-theme
Themes for GTK+3 as part of the United Dark theme.


%package -n united-dark-metacity-theme
Summary:        United Dark Metacity themes
Requires:       metacity

%description -n united-dark-metacity-theme
Themes for Metacity as part of the United Dark theme.

%package -n united-dark-gnome-shell-theme
Summary:        United Dark Shell theme
Requires:       gnome-shell

%description -n united-dark-gnome-shell-theme
United Dark Shell theme


###

%package -n united-darker-theme
Summary:        United Darker GTK+2/GTK3-3 themes
Requires: 	united-darker-gtk2-theme united-darker-gtk3-theme united-darker-metacity-theme

%description -n united-darker-theme
United Darker GTK+2/GTK3-3 themes

%package -n united-darker-gtk2-theme
Summary:        United Darker GTK+2 themes
Requires:       gtk-murrine-engine >= 0.98.1.1 gtk2-engines

%description -n united-darker-gtk2-theme
Themes for GTK+2 as part of the United Darker theme.


%package -n united-darker-gtk3-theme
Summary:        United Darker GTK+3 themes

%description -n united-darker-gtk3-theme
Themes for GTK+3 as part of the United Darker theme.


%package -n united-darker-metacity-theme
Summary:        United Darker Metacity themes
Requires:       metacity

%description -n united-darker-metacity-theme
Themes for Metacity as part of the United Darker theme.


%prep

%autosetup -n United-GNOME-%{commit0}
tar xmzvf United-Fedora.tar.gz -C %{_builddir}/United-GNOME-%{commit0}

%build
# changing name and avoid trademark issues
mv -f United-Fedora United
mv -f United-Fedora-Light United-Light
mv -f United-Fedora-Dark United-Dark
mv -f United-Fedora-Darker United-Darker

%install
install -d %{buildroot}%{_datadir}/themes/
cp -pr United-Light/ United/ United-Dark/ United-Darker/  %{buildroot}%{_datadir}/themes/

%files
%doc README.md TODO.md HACKING.md
%license LICENSE.md

# United
%files -n united-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
/usr/share/themes/United/index.theme

%files -n united-gtk2-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United/
%{_datadir}/themes/United/gtk-2.0/


%files -n united-gtk3-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United/
%{_datadir}/themes/United/gtk-3.0/


%files -n united-metacity-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United/
%{_datadir}/themes/United/metacity-1/


%files -n united-gnome-shell-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United/
%{_datadir}/themes/United/gnome-shell/

###
# United-Light

%files -n united-light-gnome-shell-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United-Light/
%{_datadir}/themes/United-Light/gnome-shell/

###
# United-Dark

%files -n united-dark-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
/usr/share/themes/United-Dark/index.theme

%files -n united-dark-gtk2-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United-Dark/
%{_datadir}/themes/United-Dark/gtk-2.0/


%files -n united-dark-gtk3-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United-Dark/
%{_datadir}/themes/United-Dark/gtk-3.0/


%files -n united-dark-metacity-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United-Dark/
%{_datadir}/themes/United-Dark/metacity-1/


%files -n united-dark-gnome-shell-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United-Dark/
%{_datadir}/themes/United-Dark/gnome-shell/

###
# United-Darker

%files -n united-darker-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
/usr/share/themes/United-Darker/index.theme

%files -n united-darker-gtk2-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United-Darker/
%{_datadir}/themes/United-Darker/gtk-2.0/


%files -n united-darker-gtk3-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United-Darker/
%{_datadir}/themes/United-Darker/gtk-3.0/


%files -n united-darker-metacity-theme
%doc README.md TODO.md HACKING.md
%license LICENSE.md
%dir %{_datadir}/themes/United-Darker/
%{_datadir}/themes/United-Darker/metacity-1/


%changelog

* Wed Nov 22 2017 David Vásquez <davidva AT tutanota DOT com> 2.2-3.gitbfb20eb
- Updated to 2.2-3.gitbfb20eb

* Thu Oct 26 2017 David Vásquez <davidva AT tutanota DOT com> 2.2-2.git51e76e0
- Updated to 2.2-2.git51e76e0

* Fri Aug 18 2017 David Vásquez <davidva AT tutanota DOT com> 2.2-1
- Initial build
