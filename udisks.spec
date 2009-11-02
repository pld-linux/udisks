Summary:	Disk Management Service
Name:		DeviceKit-disks
Version:	009
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2771769829e544e8ffb64297084b9ed9
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	device-mapper-devel >= 1.02
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.36.0
BuildRequires:	libatasmart-devel >= 0.14
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	parted-devel >= 1.8.8
BuildRequires:	polkit-devel >= 0.92
BuildRequires:	pkgconfig
BuildRequires:	sg3_utils-devel
BuildRequires:	udev-devel >= 143
BuildRequires:	udev-glib-devel >= 143
Requires:	polkit >= 0.92
Requires:	dbus >= 1.0.0
Requires:	udev >= 143
Suggests:	dosfstools
Suggests:	e2fsprogs
Suggests:	mdadm
Suggests:	mount
Suggests:	mtools
Suggests:	ntfsprogs
Suggests:	util-linux-ng
Suggests:	xfsprogs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DeviceKit-disks provides a daemon, D-Bus API and command line tools
for managing disks and storage devices.

%package devel
Summary:	D-Bus interface definitions for DeviceKit-disks
Summary(pl.UTF-8):	Definicje interfejsu D-Bus dla DeviceKit-disks
Group:		Development/Libraries

%description devel
D-Bus interface definitions for DeviceKit-disks.

%description devel -l pl.UTF-8
Definicje interfejsu D-Bus dla DeviceKit-disks.

%package apidocs
Summary:	D-Bus interface documentation for DeviceKit-disks
Summary(pl.UTF-8):	Dokumentacja interfejsu D-Bus dla DeviceKit-disks
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
D-Bus interface documentation for DeviceKit-disks.

%description apidocs -l pl.UTF-8
Dokumentacja interfejsu D-Bus dla DeviceKit-disks.

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
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/polkit-1/extensions/libdevkit-disks-action-lookup.{a,la}

%find_lang DeviceKit-disks

%clean
rm -rf $RPM_BUILD_ROOT

%files -f DeviceKit-disks.lang
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README
%attr(755,root,root) %{_bindir}/devkit-disks
%attr(755,root,root) %{_libexecdir}/devkit-disks-daemon
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-ata-smart-collect
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-ata-smart-selftest
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-change-filesystem-label
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-change-luks-password
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-create-partition
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-create-partition-table
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-delete-partition
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-drive-detach
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-drive-poll
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-fstab-mounter
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-linux-md-check
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-linux-md-remove-component
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-mkfs
%attr(755,root,root) %{_libexecdir}/devkit-disks-helper-modify-partition
%attr(755,root,root) %{_libdir}/polkit-1/extensions/libdevkit-disks-action-lookup.so
%attr(755,root,root) /sbin/umount.devkit
%attr(755,root,root) /lib/udev/devkit-disks-dm-export
%attr(755,root,root) /lib/udev/devkit-disks-part-id
%attr(755,root,root) /lib/udev/devkit-disks-probe-ata-smart
/lib/udev/rules.d/95-devkit-disks.rules
%{_sysconfdir}/profile.d/devkit-disks-bash-completion.sh
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.DeviceKit.Disks.conf
%{_datadir}/polkit-1/actions/org.freedesktop.devicekit.disks.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.DeviceKit.Disks.service
%attr(700,root,root) /var/lib/DeviceKit-disks
%attr(700,root,root) /var/run/DeviceKit-disks
%{_mandir}/man1/devkit-disks.1*
%{_mandir}/man7/DeviceKit-disks.7*
%{_mandir}/man8/devkit-disks-daemon.8*

%files devel
%defattr(644,root,root,755)
%{_datadir}/dbus-1/interfaces/org.freedesktop.DeviceKit.Disks.Device.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.DeviceKit.Disks.xml
%{_datadir}/pkgconfig/DeviceKit-disks.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/devkit-disks
