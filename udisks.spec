Summary:	Disk Management Service
Name:		udisks
Version:	1.0.4
Release:	4
License:	GPL v2+
Group:		Libraries
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	86c63b2b5484f2060499a052b5b6256b
Source1:	%{name}.tmpfiles
URL:		http://www.freedesktop.org/wiki/Software/udisks
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.82
BuildRequires:	device-mapper-devel >= 1.02
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.36.0
BuildRequires:	libatasmart-devel >= 0.14
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	parted-devel >= 2.3
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	sg3_utils-devel
BuildRequires:	udev-devel >= 147
BuildRequires:	udev-glib-devel >= 147
Requires:	dbus >= 1.0.0
Requires:	polkit >= 0.97
Requires:	udev-core >= 147
Suggests:	dosfstools
Suggests:	e2fsprogs
Suggests:	mdadm
Suggests:	mount
Suggests:	mtools
Suggests:	ntfsprogs
Suggests:	util-linux
Suggests:	xfsprogs
Obsoletes:	DeviceKit-disks
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
udisks provides a daemon, D-Bus API and command line tools for
managing disks and storage devices.

%package devel
Summary:	D-Bus interface definitions for udisks
Summary(pl.UTF-8):	Definicje interfejsu D-Bus dla udisks
Group:		Development/Libraries
Obsoletes:	DeviceKit-disks-devel

%description devel
D-Bus interface definitions for udisks.

%description devel -l pl.UTF-8
Definicje interfejsu D-Bus dla udisks.

%package apidocs
Summary:	D-Bus interface documentation for udisks
Summary(pl.UTF-8):	Dokumentacja interfejsu D-Bus dla udisks
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	DeviceKit-disks-apidocs

%description apidocs
D-Bus interface documentation for udisks.

%description apidocs -l pl.UTF-8
Dokumentacja interfejsu D-Bus dla udisks.

%package -n bash-completion-udisks
Summary:	bash-completion for udisks
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla udisks
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-udisks
This package provides bash-completion for udisks.

%description -n bash-completion-udisks -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla udisks.

%package avahi
Summary:	udisks service configuration for avahi
Summary(pl.UTF-8):	Konfiguracja serwisu udisks dla avahi
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	avahi

%description avahi
udisks service configuration for avahi.

%description avahi -l pl.UTF-8
Konfiguracja serwisu udisks dla avahi.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# see https://bugs.freedesktop.org/show_bug.cgi?id=24265
install -d $RPM_BUILD_ROOT/var/run/udisks \
	$RPM_BUILD_ROOT/etc/bash_completion.d \
	$RPM_BUILD_ROOT/usr/lib/tmpfiles.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{_sysconfdir}/profile.d/udisks-bash-completion.sh,/etc/bash_completion.d/udisks}

install %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/%{name}.conf

%find_lang udisks

%clean
rm -rf $RPM_BUILD_ROOT

%files -f udisks.lang
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README
%attr(755,root,root) %{_bindir}/udisks
%attr(755,root,root) %{_bindir}/udisks-tcp-bridge
%attr(755,root,root) %{_libexecdir}/udisks-daemon
%attr(755,root,root) %{_libexecdir}/udisks-helper-ata-smart-collect
%attr(755,root,root) %{_libexecdir}/udisks-helper-ata-smart-selftest
%attr(755,root,root) %{_libexecdir}/udisks-helper-change-filesystem-label
%attr(755,root,root) %{_libexecdir}/udisks-helper-change-luks-password
%attr(755,root,root) %{_libexecdir}/udisks-helper-create-partition
%attr(755,root,root) %{_libexecdir}/udisks-helper-create-partition-table
%attr(755,root,root) %{_libexecdir}/udisks-helper-delete-partition
%attr(755,root,root) %{_libexecdir}/udisks-helper-drive-benchmark
%attr(755,root,root) %{_libexecdir}/udisks-helper-drive-detach
%attr(755,root,root) %{_libexecdir}/udisks-helper-drive-poll
%attr(755,root,root) %{_libexecdir}/udisks-helper-fstab-mounter
%attr(755,root,root) %{_libexecdir}/udisks-helper-linux-md-check
%attr(755,root,root) %{_libexecdir}/udisks-helper-linux-md-remove-component
%attr(755,root,root) %{_libexecdir}/udisks-helper-mdadm-expand
%attr(755,root,root) %{_libexecdir}/udisks-helper-mkfs
%attr(755,root,root) %{_libexecdir}/udisks-helper-modify-partition
%attr(755,root,root) /sbin/umount.udisks
%attr(755,root,root) /lib/udev/udisks-dm-export
%attr(755,root,root) /lib/udev/udisks-part-id
%attr(755,root,root) /lib/udev/udisks-probe-ata-smart
%attr(755,root,root) /lib/udev/udisks-probe-sas-expander
/lib/udev/rules.d/80-udisks.rules
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.freedesktop.UDisks.conf
%{_datadir}/polkit-1/actions/org.freedesktop.udisks.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks.service
%attr(700,root,root) /var/lib/udisks
%attr(700,root,root) /var/run/udisks
/usr/lib/tmpfiles.d/%{name}.conf
%{_mandir}/man1/udisks-tcp-bridge.1*
%{_mandir}/man1/udisks.1*
%{_mandir}/man7/udisks.7*
%{_mandir}/man8/udisks-daemon.8*

%files devel
%defattr(644,root,root,755)
%{_datadir}/dbus-1/interfaces/org.freedesktop.UDisks.Adapter.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UDisks.Device.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UDisks.Expander.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UDisks.Port.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UDisks.xml
%{_npkgconfigdir}/udisks.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/udisks

%files -n bash-completion-udisks
%defattr(644,root,root,755)
/etc/bash_completion.d/udisks

%files avahi
%defattr(644,root,root,755)
%{_sysconfdir}/avahi/services/udisks.service
