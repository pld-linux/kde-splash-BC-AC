
%define		_splash		BC-AC

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		X11/Amusements
Source0:	http://www.pld-look.wla.pl/pliki/BC-PLD_AC_Splash.tar.gz
# Source0-md5:	8ede9bce105acfe8d863b367b01e2a0e
Requires:	kdebase-desktop
Provides:	kde-splash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"BC-AC" KDE splash screen.

%description -l pl
Ekran startowy KDE "BC-AC".

%prep
%setup -q -n BCAC-PLD-Splash

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
