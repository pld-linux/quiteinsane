#
%bcond_with	kde	# integrate with KDE to use KDE styles
#
Summary:	QuiteInsane - Qt-based graphical frontend for SANE
Summary(pl.UTF-8):   QuiteInsane - oparty na Qt graficzny interfejs do SANE
Name:		quiteinsane
Version:	0.10
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/quiteinsane/%{name}-%{version}.tar.gz
# Source0-md5:	f07006e5de95a6c326166696638ca3b5
Source1:	http://dl.sourceforge.net/quiteinsane/%{name}_cs.qm.gz
# Source1-md5:	685234aba48c8bf58b07c581df98a836
Source2:	http://dl.sourceforge.net/quiteinsane/%{name}_fr.qm.gz
# Source2-md5:	68f9f2be094903df01d6c2134e806cce
Patch0:		%{name}-qtstyle.patch
URL:		http://quiteinsane.sourceforge.net/index.shtml
%{?with_kde:BuildRequires:	kdelibs-devel}
BuildRequires:	qt-devel >= 3.0.1
BuildRequires:	sane-backends-devel >= 1.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QuiteInsane is a graphical frontend for SANE ("Scanner Access Now
Easy"). The intention behind SANE is to provide a standard application
programming interface to access raster scanner hardware.

%description -l pl.UTF-8
QuiteInsane to graficzny interfejs do SANE (projektu mającego na celu
dostarczenie standardowego interfejsu programistycznego do dostępu do
skanerów rastrowych).

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-mt \
	%{?with_kde:--enable-kde-app}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -dc %{SOURCE1} > $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/%{name}_cs.qm
gzip -dc %{SOURCE2} > $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/%{name}_fr.qm

# TODO: check if our qt can read translations from its own de/LC_MESSAGES/qt.qm
#rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/qt_de.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog PROBLEMS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/doc
%dir %{_datadir}/%{name}/locale
%lang(cs) %{_datadir}/%{name}/locale/*cs.qm
%lang(de) %{_datadir}/%{name}/locale/*de.qm
%lang(es) %{_datadir}/%{name}/locale/*es.qm
%lang(fr) %{_datadir}/%{name}/locale/*fr.qm
%lang(ru) %{_datadir}/%{name}/locale/*ru.qm
